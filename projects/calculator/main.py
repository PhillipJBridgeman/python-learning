"""A simple calculator class to perform basic arithmetic operations."""

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with a result attribute."""
        self.result = 0

    def validate_list(self, numbers):
        """Check if all elements are int or float."""
        return all(isinstance(num, (int, float)) for num in numbers)

    def add(self, numbers):
        """Add a list of numbers."""
        if self.validate_list(numbers):
            self.result = sum(numbers)
            return self.result
        raise ValueError("Invalid input. Please provide a list of numbers (int or float only).")

    def subtract(self, numbers):
        """Subtract numbers from the first element."""
        if self.validate_list(numbers):
            self.result = numbers[0]
            for num in numbers[1:]:
                self.result -= num
            return self.result
        raise ValueError("Invalid input. Please provide a list of numbers (int or float only).")

    def multiply(self, numbers):
        """Multiply a list of numbers."""
        if self.validate_list(numbers):
            self.result = 1
            for num in numbers:
                self.result *= num
            return self.result
        raise ValueError("Invalid input. Please provide a list of numbers (int or float only).")

    def divide(self, numbers):
        """Divide numbers sequentially."""
        if self.validate_list(numbers):
            if 0 in numbers[1:]:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.result = numbers[0]
            for num in numbers[1:]:
                self.result /= num
            return self.result
        raise ValueError("Invalid input. Please provide a list of numbers (int or float only).")

    def clear(self):
        """Reset the calculator result."""
        self.result = 0
        return self.result

if __name__ == "__main__":
    calc = Calculator()

    try:
        print(calc.add([1, 2, 3, 4, 5]))
        print(calc.subtract([10, 2, 3]))
        print(calc.multiply([2, 3, 4]))
        print(calc.divide([10, 2, 5]))
    except (ValueError, ZeroDivisionError) as e:
        print(e)
