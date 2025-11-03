import time

def solve_knapsack():
    # ✅ User input
    n = int(input("Enter number of items: "))
    val = list(map(int, input("Enter values (space-separated): ").split()))
    wt = list(map(int, input("Enter weights (space-separated): ").split()))
    W = int(input("Enter maximum knapsack capacity: "))

    if len(val) != n or len(wt) != n:
        print("Error: Number of values and weights must match number of items!")
        return

    # Recursive function for 0/1 Knapsack
    def knapsack(W, n):
        # Base case
        if n < 0 or W <= 0:
            return 0
        # If weight of current item > available capacity
        if wt[n] > W:
            return knapsack(W, n - 1)
        # Return max of including or excluding current item
        else:
            return max(
                val[n] + knapsack(W - wt[n], n - 1),
                knapsack(W, n - 1)
            )

    # 🕒 Measure time
    start_time = time.time()
    max_value = knapsack(W, n - 1)
    end_time = time.time()

    # 💰 Output
    print(f"\n💰 Maximum value that can be carried: {max_value}")
    print(f"⏱️ Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    solve_knapsack()
