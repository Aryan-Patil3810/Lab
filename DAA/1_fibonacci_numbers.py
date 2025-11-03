import time

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def non_recursive_fibonacci(n):
    first = 0
    second = 1
    print(first)
    print(second)
    while n - 2 > 0:
        third = first + second
        first = second
        second = third
        print(third)
        n -= 1

if __name__ == "__main__":
    # ✅ User input
    n = int(input("Enter the number of terms: "))

    # 🕒 Time the recursive version
    start_time = time.time()
    print("\nRecursive Fibonacci Sequence:")
    for i in range(n):
        print(recursive_fibonacci(i))
    end_time = time.time()
    print(f"Time taken by recursive method: {end_time - start_time:.6f} seconds\n")

    # 🕒 Time the non-recursive version
    start_time = time.time()
    print("Non-Recursive Fibonacci Sequence:")
    non_recursive_fibonacci(n)
    end_time = time.time()
    print(f"Time taken by non-recursive method: {end_time - start_time:.6f} seconds")
