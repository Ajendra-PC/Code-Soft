# =====================================
# I am Create a CALCULATOR (CODE SOFT)
# =====================================

# Ask user how many times they want to use the calculator
limit = int(input("How many calculations do you want to perform = "))

for i in range(limit):
    print(f"\n--- Calculation {i+1} of {limit} ---")

    # Step 1: Input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Step 2: Show menu (What will you do?)
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1/2/3/4): ")

    # Step 3: Perform calculation
    if choice == '1':
        print(f"✅ Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"✅ Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"✅ Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"✅ Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("❌ Error: Division by zero is not allowed.")
    else:
        print("❌ Invalid choice! Please select 1, 2, 3, or 4.")

print("\n Goodbye, You are Completed your Limit, Please RestartS!")
