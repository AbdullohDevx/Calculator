print()

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

deystyie = input("Select action: + - * / :\t")

if deystyie == "+":
    print('equals =',num1 + num2)
elif deystyie == "-":
    print('equals =',num1 - num2)
elif deystyie == "*":
    print('equals =',num1 * num2)
elif deystyie == "/":
    print('equals =',num1 / num2)
else:
    print("Invalid input")
print()

