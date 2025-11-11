from queue import Queue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

def calculate_bound(u, W, items):
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    while j < len(items) and total_weight + items[j].weight <= W:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    if j < len(items):
        profit_bound += (W - total_weight) * items[j].value / items[j].weight

    return profit_bound

def knapsack_branch_bound(W, items):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    q = Queue()
    q.put(Node(-1, 0, 0, 0))
    max_profit = 0

    while not q.empty():
        u = q.get()

        if u.level == len(items) - 1:
            continue

        next_level = u.level + 1
        v = Node(next_level, u.profit + items[next_level].value, 
                 0, u.weight + items[next_level].weight)

        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit

        v.bound = calculate_bound(v, W, items)
        if v.bound > max_profit:
            q.put(v)

        v = Node(next_level, u.profit, 0, u.weight)
        v.bound = calculate_bound(v, W, items)
        if v.bound > max_profit:
            q.put(v)

    return max_profit

def display_menu():
    print("\n" + "=" * 40)
    print("    0/1 Knapsack - Branch and Bound")
    print("=" * 40)
    print("1. Add item\n2. Remove last item\n3. Display items")
    print("4. Solve knapsack\n5. Clear all\n6. Exit")
    print("=" * 40)

def main():
    print("0/1 Knapsack Problem Solver")
    items = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        try:
            if choice == '1':
                weight = float(input("Enter item weight: "))
                value = float(input("Enter item value: "))
                
                if weight <= 0 or value <= 0:
                    print("Error: Weight and value must be positive.")
                else:
                    items.append(Item(weight, value))
                    print(f"Added: weight={weight}, value={value} (Total: {len(items)})")
            
            elif choice == '2':
                if items:
                    removed = items.pop()
                    print(f"Removed: weight={removed.weight}, value={removed.value}")
                else:
                    print("Error: No items to remove.")
            
            elif choice == '3':
                if items:
                    print(f"\n{'Item':<6} {'Weight':<10} {'Value':<10} {'Ratio':<10}")
                    print("-" * 40)
                    for i, item in enumerate(items, 1):
                        print(f"{i:<6} {item.weight:<10.2f} {item.value:<10.2f} {item.value/item.weight:<10.2f}")
                else:
                    print("No items added yet.")
            
            elif choice == '4':
                if not items:
                    print("Error: Please add items first.")
                else:
                    capacity = float(input("Enter knapsack capacity: "))
                    if capacity <= 0:
                        print("Error: Capacity must be positive.")
                    else:
                        items_copy = [Item(item.weight, item.value) for item in items]
                        max_profit = knapsack_branch_bound(capacity, items_copy)
                        print(f"\nCapacity: {capacity}, Items: {len(items)}, Max Profit: {max_profit:.2f}")
            
            elif choice == '5':
                items.clear()
                print("All items cleared." if items == [] else "No items to clear.")
            
            elif choice == '6':
                print("Program terminated.")
                break
            
            else:
                print("Invalid choice. Enter a number between 1-6.")
        
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            break
        except Exception as e:
            print(f"Error: {e}")
        
        print("-" * 50)

if __name__ == '__main__':
    main()
