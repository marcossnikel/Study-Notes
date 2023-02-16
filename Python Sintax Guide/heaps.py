#heaps
import heapq
#find min and max
#under the hood arrays
#by default minHeaps
heap = []
heapq.heappush(heap,3)
heapq.heappush(heap,2)
heapq.heappush(heap,4)

#min is always at index 0
print(heap[0])

#loop through heap -> while len is not 0 keep doing
while len(heap):
    print(heapq.heappop(heap))

#don´t have max heaps by default 
    #solution is multiply all values by -1 when pushes and again multiply by -1 when it pop

maxHeap = []
heapq.heappush(maxHeap , -3)
heapq.heappush(maxHeap , -2)
heapq.heappush(maxHeap , -4)
print( -1  * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

#build heap from initial values
arr = [2,1,8,4,5] #linear time to transform into heap
heapq.heapify(arr)
print(arr)