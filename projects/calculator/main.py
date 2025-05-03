"""A simple calculator class to perform basic arithmetic operations interactively."""

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with a result attribute."""
        self.result = 0

    def add(self, numbers):
        """Add a list of numbers.
        
        Primary method: using built-in sum().
        
        Alternative method:
            result = 0
            for num in numbers:
                result += num
            return result
        """
        return sum(numbers)

    def subtract(self, numbers):
        """Subtract numbers sequentially from the first number."""
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

    def multiply(self, numbers):
        """Multiply a list of numbers.
        
        Alternative method: use math.prod(numbers) (Python 3.8+).
        """
        result = 1
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise ValueError("Invalid input. Only integers or floats are allowed.")
            result *= num
        return result

    def divide(self, numbers):
        """Divide numbers sequentially."""
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            return result
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None

    def clear(self):
        """Reset the calculator result to zero."""
        self.result = 0
        return self.result

def get_numbers():
    """Prompt user to enter numbers separated by spaces and return as a list."""
    while True:
        try:
            numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
            if not numbers:
                raise ValueError
            return numbers
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def main():
    """Main interactive loop."""
    calculator = Calculator()

    operations = {
        "add": calculator.add,
        "subtract": calculator.subtract,
        "multiply": calculator.multiply,
        "divide": calculator.divide,
    }

    print("Welcome to the Interactive Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit.")

    while True:
        choice = input("\nChoose an operation: ").lower()

        if choice == "exit":
            print("Goodbye!")
            break
        elif choice in operations:
            numbers = get_numbers()
            result = operations[choice](numbers)
            if result is not None:
                print(f"Result: {result}")
        else:
            print("Invalid operation. Please choose from: add, subtract, multiply, divide.")

if __name__ == "__main__":
    main()
