def calculate(a, operators, b):
    if operators == "+":
       return a + b
    elif operators == "-":
       return a - b
    elif operators == "*":
       return a * b
    elif operators == "/":
       return a / b
    
#example
print(calculate(6, "*" , 4))
print(calculate(6, "+" , 4))
print(calculate(6, "-" , 4))
print(calculate(6, "/" , 4))
