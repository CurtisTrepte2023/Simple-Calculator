firstNum = float(input("Fist Number: "))
symbol = input("*, /, +, -: ")
secondNum = float(input("Second Number: "))

if symbol == "+":
    answer = firstNum + secondNum
elif symbol == "-":
    answer = firstNum - secondNum
elif symbol == "*":
    answer = firstNum * secondNum
elif symbol == "/":
    answer = firstNum / secondNum
else:
    print("There was an error, please try again")

print(answer)