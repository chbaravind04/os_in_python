def scan_disk_scheduling(initial_head, direction, disk_size, requests):
    total_head_movement = 0

    # Sort requests based on their position
    sorted_requests = sorted(requests)

    # Determine the boundary positions
    if direction == "left":
        left_boundary = 0
        right_boundary = initial_head
    else:
        left_boundary = initial_head
        right_boundary = disk_size

    # Scan towards the right boundary
    for i in range(initial_head, right_boundary + 1):
        if i in sorted_requests:
            total_head_movement += abs(initial_head - i)
            initial_head = i
            sorted_requests.remove(i)

    # Reverse direction and scan towards the left boundary
    direction = "left" if direction == "right" else "right"

    for i in range(initial_head, left_boundary - 1, -1):
        if i in sorted_requests:
            total_head_movement += abs(initial_head - i)
            initial_head = i
            sorted_requests.remove(i)

    return total_head_movement


# Test the SCAN disk scheduling algorithm
if __name__ == "__main__":
    initial_head_position = 50
    scan_direction = "right"
    disk_size = 200
    request_queue = [82, 170, 43, 140, 24, 16, 190]

    total_movement = scan_disk_scheduling(initial_head_position, scan_direction, disk_size, request_queue)
    print("Total head movement:", total_movement)
