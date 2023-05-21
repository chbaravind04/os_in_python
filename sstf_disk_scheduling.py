def sstf_disk_scheduling(initial_head, requests):
    total_head_movement = 0

    while requests:
        # Find the request with the shortest seek time
        shortest_seek_time = float('inf')
        next_request = None

        for request in requests:
            seek_time = abs(request - initial_head)
            if seek_time < shortest_seek_time:
                shortest_seek_time = seek_time
                next_request = request

        # Calculate head movement and update total head movement
        head_movement = shortest_seek_time
        total_head_movement += head_movement

        # Update initial head position and remove the processed request from the queue
        initial_head = next_request
        requests.remove(next_request)

    return total_head_movement


# Test the SSTF disk scheduling algorithm
if __name__ == "__main__":
    initial_head_position = 50
    request_queue = [82, 170, 43, 140, 24, 16, 190]

    total_movement = sstf_disk_scheduling(initial_head_position, request_queue)
    print("Total head movement:", total_movement)
