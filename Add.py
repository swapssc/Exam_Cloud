# Define a function to add two numbers
def add_two_numbers(a, b):
    return a + b

# Main function
if __name__ == "__main__":
    # Take two numbers as input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Add the two numbers
        result = add_two_numbers(num1, num2)
        
        # Print the result
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Please enter valid numbers.")
