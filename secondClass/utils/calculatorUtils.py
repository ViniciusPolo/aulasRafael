from math import sqrt

operations = ["+", "-", "*", "/"]

def checkOperation(operation):
    for op in operations:
        if operation in op:
            return True

def performOperation(valor1, valor2, operation):
    if operation == "+":
        return sum(valor1, valor2)
    elif operation == "-":
        return subtract(valor1, valor2)
    elif operation == "*":
        return multiply(valor1, valor2)
    elif operation == "/":
        return divide(valor1, valor2)
    else:
        raise ValueError("Operação inválida. Por favor, use +, -, * ou /.")
    
def addToHistory( valor1, valor2, operation, result):
    values = []
    values.append(valor1)
    values.append(valor2)
    values.append(operation)
    values.append(result)
    return values

def getHistory(history):
    print("Histórico de operações:")
    for i, entry in enumerate(history):
        print(f"{i+1}: {entry[0]} {entry[2]} {entry[1]} = {entry[3]}")

def checkIsNumber(value):
    try:
        float(value) or int(value)
        return True
    except ValueError:
        print("Erro: O valor digitado não é um número válido.")
        return False
    
def sum(valor1, valor2):
    return float(valor1) + float(valor2)

def subtract(valor1, valor2):
    return float(valor1) - float(valor2)

def multiply(valor1, valor2):
    return float(valor1) * float(valor2)

def divide(valor1, valor2):
    if float(valor2) != 0:
        return float(valor1) / float(valor2)
    else:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    
def squareRoot(valor1):
    if float(valor1) >= 0:
        return sqrt(float(valor1))
    else:
        raise ValueError("Erro: Raiz quadrada de número negativo não é permitida.")