class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
def fcfs_scheduling(processes):
    # Sort the processes based on their arrival time
    processes.sort(key=lambda x: x.arrival_time)

    # Initialize the waiting time and turnaround time for the first process
    processes[0].waiting_time = 0
    processes[0].turnaround_time = processes[0].burst_time

    # Calculate waiting time and turnaround time for the remaining processes
    for i in range(1, len(processes)):
        previous_process = processes[i-1]
        current_process = processes[i]
        current_process.waiting_time = previous_process.turnaround_time + previous_process.arrival_time - current_process.arrival_time
        current_process.turnaround_time = current_process.waiting_time + current_process.burst_time

    # Calculate average waiting time and average turnaround time
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    average_waiting_time = total_waiting_time / len(processes)
    average_turnaround_time = total_turnaround_time / len(processes)

    # Print the results
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.process_id}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
    print(f"\nAverage waiting time: {average_waiting_time}")
    print(f"Average turnaround time: {average_turnaround_time}")


# Test the FCFS scheduling algorithm
if __name__ == "__main__":
    # Create a list of processes
    processes = [
        Process(1, 0, 10),
        Process(2, 4, 6),
        Process(3, 6, 2),
        Process(4, 8, 4),
        Process(5, 10, 8)
    ]

    # Run the FCFS scheduling algorithm
    fcfs_scheduling(processes)
