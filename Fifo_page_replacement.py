from collections import deque

def fifo_page_replacement(pages, capacity):
    memory = deque(maxlen=capacity)  # Using deque as a circular queue
    
    page_faults = 0
    
    for page in pages:
        if page not in memory:
            page_faults += 1
            
            if len(memory) == capacity:
                memory.popleft()  # Remove the oldest page
            
            memory.append(page)  # Add the new page to memory
    
    return page_faults

# Example usage
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 3

faults = fifo_page_replacement(pages, capacity)
print("Total page faults:", faults)
