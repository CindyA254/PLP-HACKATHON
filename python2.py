# 2. Python Conditional Statements
# Example code is here

# Create a Python program that:
# Prompts a user to enter their age.
# Uses a conditional statement to check if the age is greater than or equal to 18.
# Prints You are eligible to vote if true, otherwise You are not eligible to vote

def main():
    # Prompt the user to enter their age
    age = int(input("Enter your age: "))

    # Check if the age is greater than or equal to 18
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")


if __name__ == "__main__":
    main()
