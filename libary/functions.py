from time import sleep as delay

def calc():
    num1 = int(input("Type in the First of the Two Numbers: "))
    num2 = int(input("Type in the Second of the Two Numbers: "))
    operation = input("And now type in the Operation (+, -, *, /): ")

    # multiplying methode
    if operation == '*':
        print("You chosed * mow we will multiplie your inputs")
        delay(0.5)
        print("Heres your output: ", num1 * num2)
    # deviding methode
    if operation == '/':
        print("You chosed / mow we will Divide your inputs")
        delay(0.5)
        print("Heres your output: ", num1 / num2)
    # subtracting methode
    if operation == '-':
        print("You chosed - mow we will subtract your inputs")
        delay(0.5)
        print("Heres your output: ", num1 - num2)
    # adding methode
    if operation == '+':
        print("You chosed + mow we will add your inputs")
        delay(0.5)
        print("Heres your output: ", num1 + num2)
    delay(1)
    print("We hope everything worket...")
    input("")