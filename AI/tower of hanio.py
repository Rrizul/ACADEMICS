def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, helper, source, destination)

# Fixed values
rings = 5
towers = 3
steps = 0   # counter

if towers == 3:
    print("Steps to solve Tower of Hanoi with 3 rings:\n")
    tower_of_hanoi(rings, 'A', 'B', 'C')
    
    print("\nTotal steps =",  2**rings - 1)
else:
    print("This solution works only for 3 towers.")