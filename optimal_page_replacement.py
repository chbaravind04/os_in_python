def optimal_page_replacement(pages, capacity):
    cache = []
    page_faults = 0

    for page in pages:
        if page not in cache:
            if len(cache) < capacity:
                cache.append(page)
            else:
                # Find the page in the cache that won't be used for the longest period
                # of time in the future
                future_indices = [i for i in range(len(pages)) if pages[i] in cache]
                future_indices = future_indices[future_indices.index(pages.index(page)) + 1:]
                if future_indices:
                    page_to_replace = max(future_indices, key=future_indices.index)
                else:
                    page_to_replace = cache[-1]

                cache[cache.index(page_to_replace)] = page
            page_faults += 1

    return page_faults

# Example usage:
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 3
faults = optimal_page_replacement(pages, capacity)
print("Page Faults:", faults)
