def calculator(operation, a, b):
    if operation == '*':
        return a*b
    elif operation == '/':
        return a/b
    elif operation == '-':
        return a-b
    elif operation == '+':
        return a+b
    else:
        return "sorry"

def main():
    s = "Let's go"
    while s != 'stop':
        a = int(input("Enter А "))
        b = int(input("Enter В "))
        operation = input("Select one from -,+,/,* ")
        print (calculator(operation,a, b))
        s = input("well done, if it's all, then must write 'stop' ")

if __name__ == '__main__':
    main()