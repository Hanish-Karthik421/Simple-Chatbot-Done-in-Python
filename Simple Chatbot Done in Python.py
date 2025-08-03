import math

# Greeting
print("Hello! Welcome to 'Simple Chatbot' 😊😊")
name = input("What is your name?: ")
print(f"Hello {name}, how are you?")

user_condition = input().lower()
if user_condition == "fine!":
    print("Good to hear that!")
else:
    print("I can't understand what you're trying to say, please repeat it again.")
    exit("Please start the Chatbot Again")

# Question asking
ask = input("Do you want to ask any questions? (Y/N): ").lower()
if ask == "y":
    math_q = input("I specialize in square roots. Do you want to ask a math question? (Y/N): ").lower()
    if math_q == "y":
        num = input("What number do you want to find the square root of?: ")
        try:
            root = math.sqrt(float(num))
            print(f"The square root of {num} is {root}")
        except ValueError:
            print("That’s not a valid number.")
        print("Goodbye!")
    else:
        print("Okay, goodbye!")
elif ask == "n":
    print("Okay, goodbye! 👋👋")
else:
    print("Sorry, I can't understand what you're saying. Please try again.")
