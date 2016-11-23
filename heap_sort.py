from random import *

small = 0


def buildheap(heap, list_size):
    for i in range(int(list_size/2)-1, -1, -1):
        heapify(heap, i, list_size)

def heapify(heap, root, list_size):
    global small
    left_leaf = 2*root+1
    right_leaf = 2*root
    if right_leaf < list_size:
        if heap[left_leaf] < heap[right_leaf]:
            small = left_leaf
        else:
            small = right_leaf
    elif left_leaf < list_size:
        small = left_leaf
    else:
        return
    if heap[small] < heap[root]:
        temp = heap[small]
        heap[small] = heap[root]
        heap[root] = temp
        heapify(heap, small, list_size)


def heapsort(heap, list_size):
    buildheap(heap, list_size)
    for i in range(list_size-1, 0, -1):
        temp = heap[0]
        heap[0] = heap[i]
        heap[i] = temp
        heapify(heap, 0, i-1)


def main():
    heap = []
    for _ in range(10):
        heap.append(randint(1, 100))
    print(heap)
    heapsort(heap,len(heap))
    print(heap)

if __name__ == "__main__":
    main()

