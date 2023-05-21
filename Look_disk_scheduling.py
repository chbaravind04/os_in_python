def look_disk_scheduling(initial_head, direction, disk_size, requests):
    total_head_movement = 0

    # Sort requests based on their position
    sorted_requests = sorted(requests)

    if direction == "left":
        # Scan towards the left boundary
        for i in range(initial_head, -1, -1):
            if i in sorted_requests:
                total_head_movement += abs(initial_head - i)
                initial_head = i
                sorted_requests.remove(i)

        # Reverse direction and scan towards the right boundary
        direction = "right"

    else:
        # Scan towards the right boundary
        for i in range(initial_head, disk_size + 1):
            if i in sorted_requests:
                total_head_movement += abs(initial_head - i)
                initial_head = i
                sorted_requests.remove(i)

        # Reverse direction and scan towards the left boundary
        direction = "left"

    # Scan in the reversed direction until no more requests are left
    for i in range(initial_head, -1, -1):
        if i in sorted_requests:
            total_head_movement += abs(initial_head - i)
            initial_head = i
            sorted_requests.remove(i)

    return total_head_movement


# Test the LOOK disk scheduling algorithm
if __name__ == "__main__":
    initial_head_position = 50
    scan_direction = "left"
    disk_size = 200
    request_queue = [82, 170, 43, 140, 24, 16, 190]

    total_movement = look_disk_scheduling(initial_head_position, scan_direction, disk_size, request_queue)
    print("Total head movement:", total_movement)
