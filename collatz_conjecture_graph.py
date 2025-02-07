import matplotlib.pyplot as plt
import math

def collatz(n):
    sequence = []  # List to store the sequence
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)  # Include the final 1
    return sequence

def generate_collatz_graph(min_n, max_n):
    plt.figure(figsize=(12, 8))
    
    # Loop through each value of n in the given range
    for n in range(min_n, max_n + 1):
        sequence = collatz(n)  # Get the Collatz sequence for the current n
        steps = list(range(1, len(sequence) + 1))  # Steps for the x-axis
        
        # Scatter plot each sequence with small points and transparency for the dot matrix effect
        plt.scatter(steps, sequence, color='red', s=5, alpha=0.5)
    
    # Customizing the plot
    plt.title(f"Collatz Sequences for n in range {min_n} to {max_n}")
    plt.xlabel('Step Number')
    plt.ylabel('Value of n')
    plt.yscale('log')  # Logarithmic scale to capture the behavior better
    plt.grid(True)
    plt.show()

# Example usage: Generate the graph for n values between 1 and n
generate_collatz_graph(1, 500)
