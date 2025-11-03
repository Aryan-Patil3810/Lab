import time

def n_queens(n):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)
    res = []
    board = [["0"] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            # If attacking positions already used, skip
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # Place queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "1"

            backtrack(r + 1)

            # Remove queen (backtrack)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "0"

    # 🕒 Start measuring time
    start_time = time.time()

    backtrack(0)

    # 🕒 End time
    end_time = time.time()

    # 🖨️ Display results
    print(f"\n✅ Total solutions for {n}-Queens: {len(res)}\n")
    for idx, sol in enumerate(res, start=1):
        print(f"Solution {idx}:")
        for row in sol:
            print(row)
        print()

    print(f"⏱️ Time taken: {end_time - start_time:.6f} seconds")

# Main program
if __name__ == "__main__":
    n = int(input("Enter number of queens (N): "))
    n_queens(n)
