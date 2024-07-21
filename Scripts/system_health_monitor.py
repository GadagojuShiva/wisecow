import psutil
import logging

# Set thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.info(f"High CPU usage detected: {cpu_usage}%")
        print(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.info(f"High memory usage detected: {memory_usage}%")
        print(f"High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.info(f"High disk usage detected: {disk_usage}%")
        print(f"High disk usage detected: {disk_usage}%")
    return disk_usage

def check_processes():
    process_count = len(psutil.pids())
    logging.info(f"Number of running processes: {process_count}")
    print(f"Number of running processes: {process_count}")
    return process_count

if __name__ == "__main__":
    cpu_usage = check_cpu()
    memory_usage = check_memory()
    disk_usage = check_disk()
    process_count = check_processes()

    logging.info(f"System Health Report - CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%, Processes: {process_count}")
    print(f"System Health Report - CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%, Processes: {process_count}")
