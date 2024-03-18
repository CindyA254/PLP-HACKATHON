# Functions & Fibonacci Sequence
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.

# Your program should:
# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with the first two terms of the Fibonacci sequence

    # Generate the Fibonacci sequence up to the specified term n
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence[:n]  # Return the first n terms of the Fibonacci sequence


def main():
    # Ask the user to input the value of n
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))

    # Generate the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(n)

    # Print the generated Fibonacci sequence
    print("Fibonacci sequence up to term", n, "is:", fibonacci_sequence)


if __name__ == "__main__":
    main()


