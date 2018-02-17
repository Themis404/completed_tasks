s = "Let's go"
while s != 'stop':
    a = int(input("Enter А "))
    b = int(input("Enter В "))
    operation = input("Select one from -,+,/,* ")
    def calculator():
        if operation == '*':
            print(a*b)
        elif operation == '/':
            print(a/b)
        elif operation == '-':
            print(a-b)
        elif operation == '+':
            print(a+b)
        else:
            print("sorry")
    calculator()
    s = input("well done, if it's all, then must write 'stop' ")