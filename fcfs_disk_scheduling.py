def fcfs_disk_scheduling(initial_head, requests):
    total_head_movement = 0

    # Calculate head movement for each request
    for i in range(len(requests)):
        current_request = requests[i]
        head_movement = abs(current_request - initial_head)
        total_head_movement += head_movement
        initial_head = current_request

    return total_head_movement


# Test the FCFS disk scheduling algorithm
if __name__ == "__main__":
    initial_head_position = 50
    request_queue = [82, 170, 43, 140, 24, 16, 190]

    total_movement = fcfs_disk_scheduling(initial_head_position, request_queue)
    print("Total head movement:", total_movement)
