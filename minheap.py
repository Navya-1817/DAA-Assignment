class MinHeap:
    def __init__(self):
        self.heap = []
        self.pos = {}  # value to index mapping for fast deletion

    def insert(self, val):
        self.heap.append(val)
        self.pos[val] = len(self.heap) - 1
        self._sift_up(len(self.heap) - 1)

    def delete(self, val):
        idx = self.pos[val]
        last = self.heap[-1]
        self.heap[idx] = last
        self.pos[last] = idx
        self.heap.pop()
        del self.pos[val]
        if idx < len(self.heap):
            self._sift_down(idx)
            self._sift_up(idx)

    def get_min(self):
        return self.heap[0]

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] > self.heap[idx]:
                # swap
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                self.pos[self.heap[parent]] = parent
                self.pos[self.heap[idx]] = idx
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != idx:
                self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
                self.pos[self.heap[smallest]] = smallest
                self.pos[self.heap[idx]] = idx
                idx = smallest
            else:
                break

import sys

if __name__ == "__main__":
    Q = int(sys.stdin.readline())
    heap = MinHeap()
    for _ in range(Q):
        parts = sys.stdin.readline().strip().split()
        if parts[0] == "1":
            heap.insert(int(parts[1]))
        elif parts[0] == "2":
            heap.delete(int(parts[1]))
        elif parts[0] == "3":
            print(heap.get_min())
