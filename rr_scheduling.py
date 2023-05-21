from collections import deque

class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0


def rr_scheduling(processes, time_quantum):
    ready_queue = deque(processes)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")

    while ready_queue:
        current_process = ready_queue.popleft()

        if current_process.remaining_time <= time_quantum:
            # Process execution completes within the time quantum
            execution_time = current_process.remaining_time
            current_process.remaining_time = 0
        else:
            # Process execution is not completed within the time quantum
            execution_time = time_quantum
            current_process.remaining_time -= time_quantum
            ready_queue.append(current_process)

        current_process.waiting_time = current_time - current_process.arrival_time
        current_process.turnaround_time = current_process.waiting_time + current_process.burst_time

        total_waiting_time += current_process.waiting_time
        total_turnaround_time += current_process.turnaround_time

        print(f"{current_process.process_id}\t{current_process.arrival_time}\t\t{current_process.burst_time}"
              f"\t\t{current_process.waiting_time}\t\t{current_process.turnaround_time}")

        current_time += execution_time

    average_waiting_time = total_waiting_time / len(processes)
    average_turnaround_time = total_turnaround_time / len(processes)
    print(f"\nAverage waiting time: {average_waiting_time}")
    print(f"Average turnaround time: {average_turnaround_time}")


# Test the RR scheduling algorithm
if __name__ == "__main__":
    # Create a list of processes
    processes = [
        Process(1, 0, 10),
        Process(2, 4, 6),
        Process(3, 6, 2),
        Process(4, 8, 4),
        Process(5, 10, 8)
    ]

    # Set the time quantum
    time_quantum = 4

    # Run the RR scheduling algorithm
    rr_scheduling(processes, time_quantum)
