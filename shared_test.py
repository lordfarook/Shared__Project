age = int(input("wht is your age? "))
while age <= 0:
    print("Error, an age cannot be negative")
    age = int(input("wht is your age? "))
print(f"your age is {age}")