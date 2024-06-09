import psutil 

# Define thresholds
cpu_threshold = 80  # in percentage
mem_threshold = 80  # in percentage
disk_threshold = 80  # in percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > cpu_threshold:
        print(f"CPU usage is high: {cpu_usage}%")
    with open("alert_log.txt", "a") as log_file:
        print(f"Alert: High CPU usage detected! ({cpu_usage}%)\n")
        

def check_memory_usage():
    mem_usage = psutil.virtual_memory().percent
    if mem_usage > mem_threshold:
        print(f"Memory usage is high: {mem_usage}%")
    with open("alert_log.txt", "a") as log_file:
        print(f"Alert: High Memory usage detected! ({mem_usage}%)\n")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > disk_threshold:
        print(f"Disk usage is high: {disk_usage}%")
    with open("alert_log.txt", "a") as log_file:
        print(f"Alert: Disk usage detected! ({disk_usage}%)\n")

def check_running_processes():
    num_processes = len(psutil.pids())
    print(f"Number of running processes: {num_processes}")

# Main function to check system health
def main():
    print("Checking system health...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    print("Health check complete.")

if __name__ == "__main__":
    main()
