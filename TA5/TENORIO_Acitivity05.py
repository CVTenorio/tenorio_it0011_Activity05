#TENORIO CARL VINCENT IT0011 Actvitiy 05 v1.00

def divide(numerator, denominator):
    if denominatior == 0:
        print("Error: Divide by 0 is not allowed.")
        return None
    return numerator / denominator
def exponentiation(base, exponent):
    return base ** exponent        
    
def remainder(numerator, denominator):
    if denominator == 0:
        print("Error: Modulo by 0 is not allowed.")
        return None
    return numerator % denominator

def summation(start, end):
    if end < start:
        print("Error: The second number must be greater than or equal to the first number.")
        return None
    return sum(range(start, end +1))

def main():
    while True:
        print("\nTenorio's Mathematical Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice from the Menu: ").upper()
        
        if choice == 'D':
            try:
                num1 = float(input("Enter numerator:"))
                num2 = float(input("Enter denominator:"))
                result = divide(num1,num2)
                if result is not None:
                    print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter numbers.")
                
        elif choice == 'E':
            try:
                
                