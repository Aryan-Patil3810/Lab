import time

def fractional_knapsack():
    # User input
    n = int(input("Enter number of items: "))
    weights = list(map(float, input("Enter weights (space-separated): ").split()))
    values = list(map(float, input("Enter values (space-separated): ").split()))
    capacity = float(input("Enter knapsack capacity: "))

    if len(weights) != n or len(values) != n:
        print("Error: Number of weights and values must match number of items!")
        return

    res = 0.0  # Result (maximum value)

    # Start timing
    start_time = time.time()

    # Pair (weight, value) sorted by value/weight ratio (descending)
    for pair in sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True):
        if capacity <= 0:  # Knapsack full
            break
        w, v = pair
        if w > capacity:  # Take fraction of the item
            res += capacity * (v / w)
            capacity = 0
        else:  # Take the whole item
            res += v
            capacity -= w

    # End timing
    end_time = time.time()

    print(f"\n💰 Maximum value in knapsack = {res:.2f}")
    print(f"⏱️ Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    fractional_knapsack()
