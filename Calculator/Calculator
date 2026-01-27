class Calculator:
    def __init__(self):
        #Initialize the result attribute to 0
        self.result = 0

    def add(self, number):
        #Add the number to result and return the new result
        self.result += number
        return self.result

    def subtract(self, number):
        #Subtract the number from result and return the new result
        self.result -= number
        return self.result

    def multiply(self, number):
        #Multiply result by the number and return the new result
        self.result *= number
        return self.result

    def divide(self, number):
        # Check if number is 0
        # If it is, print error message and return unchanged result
        # Otherwise, divide result by the number and return the new result
        if number == 0:
            print("Error: Division by zero")
            return self.result
        self.result /= number
        return self.result

    def clear(self):
        #Reset result to 0 and return it
        self.result = 0
        return self.result

    def get_result(self):
        #Return the current value of result
        return self.result
