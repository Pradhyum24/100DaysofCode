from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    num1=float(input("What's the first number?: "))
    should_accumulate= True
    while should_accumulate is  True:
        print("+\n-\n*\n/")
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result=operations[operator](num1,num2)
        print(f"{num1} {operator} {num2} = {result}")
        continue_calc=input((f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")).lower()
        if continue_calc == "y":
            num1 = result

        else:
            should_accumulate=False
            calculator()
calculator()






