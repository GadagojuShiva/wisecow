# System Health Monitoring and Log File Analyzer

This repository contains two Python scripts: `system_health_monitor.py` for monitoring the health of a Linux system and `log_file_analyzer.py` for analyzing Nginx web server logs.

## Prerequisites

- Python 3.6 or higher
- Virtual environment tools (python3-venv)
- Nginx web server (for log file analysis)

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/gadagojushiva/wisecow.git
cd wisecow/Scripts
```
### Step 2: Install Virtual Environment Tools

Ensure you have the virtual environment tools installed:

```bash
sudo apt update
sudo apt install python3-venv -y
```
### Step 3: Create and Activate a Virtual Environment
Create a virtual environment in your project directory:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Required Packages

With the virtual environment activated, install the required packages:

```bash
pip install psutil
```

## Scripts

1. System Health Monitoring Script
This script monitors CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds, the script sends an alert to the console and logs it to a file.

Running the Script
```bash 
python system_health_monitor.py
```

2. Log File Analyzer Script
This script analyzes Nginx web server logs for common patterns such as the number of 404 errors, the most requested pages, and IP addresses with the most requests. The script outputs a summarized report.

Configuring the Log File Path
Ensure that the log file path in `log_file_analyzer.py` is correct. By default, it is set to `/var/log/nginx/access.log`. Update the `log_file_path` variable if your log file is located elsewhere:
```bash
log_file_path = '/path/to/your/nginx/access.log'
```
3. Running the Script
```bash
python log_file_analyzer.py
```
4. Deactivating the Virtual Environment
Once you are done, you can deactivate the virtual environment by running:

```bash
deactivate
```