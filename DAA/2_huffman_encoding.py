import heapq
import time

# Creating Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq      # frequency of symbol
        self.symbol = symbol  # symbol name (character)
        self.left = left      # left child
        self.right = right    # right child
        self.huff = ''        # tree direction (0/1)

    # Compare nodes based on frequency (for heapq)
    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Function to print Huffman codes
def print_nodes(node, val=''):
    newval = val + str(node.huff)
    # If node is not a leaf node, traverse deeper
    if node.left:
        print_nodes(node.left, newval)
    if node.right:
        print_nodes(node.right, newval)

    # If node is a leaf node, print its Huffman code
    if not node.left and not node.right:
        print("{} -> {}".format(node.symbol, newval))

# Main program
if __name__ == "__main__":
    # User Input
    chars = list(input("Enter the characters (no spaces, e.g., abcdef): "))
    freq = list(map(int, input("Enter their frequencies (space-separated): ").split()))

    if len(chars) != len(freq):
        print("Error: Number of characters and frequencies must be same!")
        exit()

    # Start measuring time
    start_time = time.time()

    # Create list of nodes
    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    # Combine nodes until one tree remains
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        # Combine two smallest nodes
        newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newnode)

    print("\n🔢 Huffman Codes:")
    print_nodes(nodes[0])

    # 🕒 End measuring time
    end_time = time.time()
    print(f"\n⏱️ Time taken: {end_time - start_time:.6f} seconds")
