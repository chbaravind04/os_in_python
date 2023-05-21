class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0


def sjf_scheduling(processes):
    # Sort the processes based on their burst time
    processes.sort(key=lambda x: x.burst_time)

    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

        print(f"{process.process_id}\t\t\t{process.arrival_time}\t\t\t{process.burst_time}\t\t\t\t\t{process.waiting_time}\t\t\t\t\t\t{process.turnaround_time}")

        current_time += process.burst_time

    average_waiting_time = total_waiting_time / len(processes)
    average_turnaround_time = total_turnaround_time / len(processes)
    print(f"\nAverage waiting time: {average_waiting_time}")
    print(f"Average turnaround time: {average_turnaround_time}")


# Test the SJF scheduling algorithm
if __name__ == "__main__":
    # Create a list of processes
    processes = [
        Process(1, 0, 10),
        Process(2, 4, 6),
        Process(3, 6, 2),
        Process(4, 8, 4),
        Process(5, 10, 8)
    ]

    # Run the SJF scheduling algorithm
    sjf_scheduling(processes)
