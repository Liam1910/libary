from time import sleep as delay
import random as rng

class Calculating():

    def FullCalc():
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
    
    def DecimalCalc():
        num1Decimal = float(input("Type in the First of the Two Decemal Numbers: "))
        num2Decimal = float(input("Type in the Second of the Two Decemal Numbers: "))
        operation = input("And now type in the Operation (+, -, *, /): ")

        # multiplying methode
        if operation == '*':
            print("You chosed * mow we will multiplie your inputs")
            delay(0.5)
            print("Heres your output: ", num1Decimal * num2Decimal)
        # deviding methode
        if operation == '/':
            print("You chosed / mow we will Divide your inputs")
            delay(0.5)
            print("Heres your output: ", num1Decimal / num2Decimal)
        # subtracting methode
        if operation == '-':
            print("You chosed - mow we will subtract your inputs")
            delay(0.5)
            print("Heres your output: ", num1Decimal - num2Decimal)
        # adding methode
        if operation == '+':
            print("You chosed + mow we will add your inputs")
            delay(0.5)
            print("Heres your output: ", num1Decimal + num2Decimal)
        delay(1)
        print("We hope everything worket...")
        input("")

class RandomPasswordGenerating():

    def Generator():
        lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
        upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!§%&/()=?`*';:,.-_²³{[]}\~@€<>|"


        string = lower_case_letters + upper_case_letters + numbers + symbols
        length = 10
        password = "".join(rng.sample(string, length))

        print("Your New Password is: " + password)


def help():
    print("Thanks for Downloading the Libary... You want Help I see...")
    print("So to make it easy... You have two Options to Choose (Actualy three)...")
    delay(1)
    print("1. :")
    print("        Libary.Calculating.FullCalc()")
    print("        Can Calculate Full Numbers... If You Type in that line of code you can enter numbers and the operation in the console then it will calculate...")
    print("")
    delay(1)
    print("2. :")
    print("        Libary.Calculating.DecimalCalc()")
    print("       Its Actualy the same but it doesnt Calculate with full numbers it (Like the name Says) Calculates Decimal Numbers (Example: 1.98)")
    print("")
    delay(1)
    print("3. :")
    print("        Libary.RandomPasswordGenerating.Genarator()")
    print("        It Basicly generates a password with lower and upper case letters, numbers and symbols.")
