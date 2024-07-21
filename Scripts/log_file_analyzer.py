import re
from collections import Counter

# Path to the Nginx log file
log_file_path = '/var/log/nginx/access.log'

def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

def analyze_logs(logs):
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[.*\] "GET (.*?) HTTP/.*" (\d+) .*')
    ip_counter = Counter()
    page_counter = Counter()
    error_404_counter = 0

    for log in logs:
        match = pattern.match(log)
        if match:
            ip, page, status = match.groups()
            ip_counter[ip] += 1
            page_counter[page] += 1
            if status == '404':
                error_404_counter += 1

    return ip_counter, page_counter, error_404_counter

def print_report(ip_counter, page_counter, error_404_counter):
    print("Log File Analysis Report")
    print("========================")
    print(f"Total 404 Errors: {error_404_counter}")
    print("\nTop 5 Most Requested Pages:")
    for page, count in page_counter.most_common(5):
        print(f"{page}: {count} requests")
    print("\nTop 5 IP Addresses with Most Requests:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} requests")

if __name__ == "__main__":
    logs = parse_log(log_file_path)
    ip_counter, page_counter, error_404_counter = analyze_logs(logs)
    print_report(ip_counter, page_counter, error_404_counter)
