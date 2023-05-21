def clook_disk_scheduling(initial_head, disk_size, requests):
    total_head_movement = 0

    # Sort requests based on their position
    sorted_requests = sorted(requests)

    # Scan towards the right boundary
    for i in range(initial_head, disk_size + 1):
        if i in sorted_requests:
            total_head_movement += abs(initial_head - i)
            initial_head = i
            sorted_requests.remove(i)

    # Move to the beginning of the disk
    total_head_movement += abs(initial_head - 0)
    initial_head = 0

    # Scan towards the right boundary again
    for i in range(initial_head, disk_size + 1):
        if i in sorted_requests:
            total_head_movement += abs(initial_head - i)
            initial_head = i
            sorted_requests.remove(i)

    return total_head_movement


# Test the C-LOOK disk scheduling algorithm
if __name__ == "__main__":
    initial_head_position = 50
    disk_size = 200
    request_queue = [82, 170, 43, 140, 24, 16, 190]

    total_movement = clook_disk_scheduling(initial_head_position, disk_size, request_queue)
    print("Total head movement:", total_movement)
