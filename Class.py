class Calculator:
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor
    
    def add(self, value1: float, value2: float) -> float: 
        return value1 + value2
