class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)
    
    def bubble_up(self, index):
        while index > 0:
            parent_idx = (index - 1) // 2
            if self.heap[parent_idx] >= self.heap[index]:
                break
            self.heap[parent_idx], self.heap[index] = \
                self.heap[index], self.heap[parent_idx]
            index = parent_idx
            
    def extract_max(self):
        if not self.heap:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self.heapify_down(0)
        return max_val
    
    def heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):
            larger_child = 2 * index + 1
            if (2 * index + 2 < len(self.heap) and 
                self.heap[2 * index + 2] > self.heap[larger_child]):
                larger_child = 2 * index + 2
            
            if self.heap[index] >= self.heap[larger_child]:
                break
            self.heap[index], self.heap[larger_child] = \
                self.heap[larger_child], self.heap[index]
            index = larger_child
    
    def peek(self):
        """Return the maximum element without removing it"""
        return self.heap[0] if self.heap else None
    
    def size(self):
        """Return the number of elements in the heap"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if the heap is empty"""
        return len(self.heap) == 0
    
    def display(self):
        """Display the heap as a list"""
        return self.heap.copy()


def display_menu():
    """Display the menu options"""
    print("\n" + "=" * 35)
    print("        MaxHeap Operations Menu")
    print("=" * 35)
    print("1. Insert a value")
    print("2. Extract maximum")
    print("3. Peek (view maximum)")
    print("4. Display heap")
    print("5. Check if empty")
    print("6. Get heap size")
    print("7. Exit")
    print("=" * 35)

def main():
    """Interactive driver code for MaxHeap operations"""
    print("MaxHeap Implementation")
    print("Perform various operations on the heap data structure.")
    
    # Create a new MaxHeap instance
    max_heap = MaxHeap()
    display_menu()
    
    while True:
        
        try:
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                # Insert operation
                try:
                    value = int(input("Enter value to insert: "))
                    max_heap.insert(value)
                    print(f"Successfully inserted {value}")
                    print(f"Current heap: {max_heap.display()}")
                except ValueError:
                    print("Error: Please enter a valid integer.")
            
            elif choice == '2':
                # Extract maximum operation
                max_val = max_heap.extract_max()
                if max_val is not None:
                    print(f"Extracted maximum value: {max_val}")
                    print(f"Current heap: {max_heap.display()}")
                else:
                    print("Error: Heap is empty. Cannot extract maximum.")
            
            elif choice == '3':
                # Peek operation
                max_val = max_heap.peek()
                if max_val is not None:
                    print(f"Maximum value: {max_val}")
                else:
                    print("Error: Heap is empty. No maximum value available.")
            
            elif choice == '4':
                # Display heap
                heap_contents = max_heap.display()
                if heap_contents:
                    print(f"Current heap: {heap_contents}")
                else:
                    print("Heap is empty.")
            
            elif choice == '5':
                # Check if empty
                is_empty = max_heap.is_empty()
                if is_empty:
                    print("Heap is empty.")
                else:
                    print(f"Heap contains {max_heap.size()} elements.")
            
            elif choice == '6':
                # Get heap size
                size = max_heap.size()
                print(f"Heap size: {size} elements")
            
            elif choice == '7':
                # Exit
                print("Program terminated.")
                print(f"Final heap state: {max_heap.display()}")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1-7.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print(f"Final heap state: {max_heap.display()}")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Add separator for better readability
        print("-" * 50)


if __name__ == "__main__":
    main()