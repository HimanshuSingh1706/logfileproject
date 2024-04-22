import time
import pandas as pd
import pprint

ip_list=[]
success_list=[]
failed_list=[]

# defining fuction just for showing output as an table
def update_dataframe():
    df = pd.DataFrame(columns=['IP Address', 'Success Request', 'Failed Request'])
    df['IP Address'] = ip_list
    df['Failed Request'] = failed_list
    df['Success Request'] = success_list
    print("\n New log entries:")
    pprint.pprint(df)

try:
    with open("server.log","r") as logfile:
        while True:
            log = logfile.readline()
            if not log:
                # If there's no new content, sleep for a while to avoid high CPU usage
                time.sleep(1)
                continue
            print(log, end='')  # Print the log without adding a newline
            x=log.split(" ")
            failed_list.append(int(x[-1]))
            success_list.append(int(x[-4]))
            ip_list.append(x[0])
            print("\n\n")
            print("please find summary report ..")
            update_dataframe()
            print("\n")
            print("please enter Ctrl+c for stop monitoring and analysis")
except FileNotFoundError:
    print("Error: The log file 'server.log' does not exist.")
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
  
