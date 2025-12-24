import math    
class Calculator:
    def __init__(self):
        print("🧮 Welcome to OOP Calculator!")

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "You can't divide by zero"
        return a / b
    
    def power(self,a,b):
        return math.pow(a,b)
    
    def root(self,a):
        if a<0:
            return "❌ Cannot take square root of negative number"
        return math.sqrt(a)

    def run(self):

        while True:
         

            num1_input = input("Enter 1st number (or 'q' to quit): ")
            if num1_input.lower() == "q":
                print("👋 Exiting calculator...")
                break

            num2_input = input("Enter 2nd number (or 'q' to quit): ")
            if num2_input.lower() == "q":
                print("👋 Exiting calculator...")
                break

            try:
                num1 = float(num1_input)
                num2 = float(num2_input)
            except ValueError:
                print("❌ Invalid input, please enter numbers only.")
                continue

            print("\nSelect operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exit")

            choice = input("Enter choice (1/2/3/4/5): ")

            ans = None
            if choice == "1":
                ans = self.add(num1, num2)
            elif choice == "2":
                ans = self.sub(num1, num2)
            elif choice == "3":
                ans = self.mul(num1, num2)
            elif choice == "4":
                ans = self.divide(num1, num2)
            elif choice == "5":
                print("👋 Exiting calculator...")
                break
            else:
                print("❌ Invalid choice")
                continue

            print(f"✅ Ans: {ans}\n")

# To run the calculator, create an instance and call the run method
calc = Calculator()
calc.run()