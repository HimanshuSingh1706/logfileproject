# Log Monitoring and Analysis Script

## Overview
This script is designed to monitor a log file (`server.log`), extract specific information from each log line, and provide a summary report in tabular format using pandas.

## Prerequisites
- Python 3.x installed on your system
- Pandas library installed (`pip install pandas`)

## How to Use
1. **Download the Script:** Download the provided Python script (`log_monitor.py`) to your local machine.

2. **Ensure Log File Existence:** Make sure the log file `server.log` exists in the same directory as the script. If not, create one or specify the correct path to an existing log file in the script.

3. **Run the Script:** Open a terminal or command prompt, navigate to the directory containing the script, and run the script using the following command:

```console
python log_monitor.py

```


4. **Monitor Log Activity:** Once the script is running, it will continuously monitor the log file for new entries. It will extract relevant information from each log line, including IP address, success requests, and failed requests, and display the log line itself. Additionally, it will print a summary report showing the aggregated data in a tabular format.

5. **Stop Monitoring:** To stop monitoring and exit the script, press `Ctrl + C` in the terminal/command prompt.

## Sample Log Line
There is no log file provide by you so I pick this one from internet and makes code as per following logs, A sample log line is provided below for reference:

66.249.66.194 - - [22/Jan/2019:03:56:20 +0330] "GET /m/filter/b2,p6 HTTP/1.1" 200 19451 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "-" requestsuccessful: 56 requestfailed: 248


## Notes
- The script will automatically handle scenarios like missing log file or unexpected interruptions during execution.
