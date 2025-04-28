"""A simple calculator class to perform basic arithmetic operations.

Returns:
    result: The result of the arithmetic operation.
"""

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
        else:
            print("Invalid input. Please enter a list of numbers (int or float only).")
            return None

    def subtract(self, numbers):
        """Subtract a list of numbers."""
        if self.validate_list(numbers):
            self.result = numbers[0] - sum(numbers[1:])
            return self.result
        else:
            print("Invalid input. Please enter a list of numbers (int or float only).")
            return None

    def multiply(self, numbers):
        """Multiply a list of numbers."""
        if self.validate_list(numbers):
            self.result = 1
            for num in numbers:
                self.result *= num
            return self.result
        else:
            print("Invalid input. Please enter a list of numbers (int or float only).")
            return None

    def divide(self, numbers):
        """Divide a list of numbers."""
        if self.validate_list(numbers):
            if 0 in numbers[1:]:
                print("Division by zero is not allowed.")
                return None
            self.result = numbers[0]
            for num in numbers[1:]:
                self.result /= num
            return self.result
        else:
            print("Invalid input. Please enter a list of numbers (int or float only).")
            return None

    def clear(self):
        """Reset the calculator result."""
        self.result = 0
        return self.result        

# Example usage
calc = Calculator()

print(calc.add([1, 2, 3, 4, 5]))
print(calc.add([2.5, 3.5, 4.0]))
print(calc.add([1, 2, 3]))
print(calc.subtract([10, 2, 3]))
print(calc.multiply([2, 3, 4]))
print(calc.divide([10, 2, 5]))
print(calc.divide([10, 0]))
print(calc.multiply([2, 3, 'a']))
print(calc.subtract([10, 2, 'b']))
print(calc.add([1, 2, 3, 4, 5]))
print(calc.subtract([10, 2, 3]))
print(calc.multiply([2, 3, 4]))
print(calc.divide([10, 2, 5]))
print(calc.divide([10, 0]))
print(calc.multiply([2, 3, 'a']))
print(calc.subtract([10, 2, 'b']))
print(calc.add([1, 2, 3, 4, 5]))
print(calc.subtract([10, 2, 3]))
print(calc.multiply([2, 3, 4]))
