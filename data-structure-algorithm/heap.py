import heapq

# Create an empty "max heap" using negation
max_heap = []

# Add elements (negate the values for max heap behavior)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)

# Remove and return the largest element (remember to negate it back)
largest = -heapq.heappop(max_heap)
print("The largest element is:", largest)

# The remaining heap (remember the elements are negated)
print("The remaining negated heap:", max_heap)
print("The actual values in the max heap:", [-x for x in max_heap])


