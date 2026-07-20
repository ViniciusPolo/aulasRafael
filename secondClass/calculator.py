from utils.calculatorUtils import addToHistory, checkOperation, performOperation, getHistory, checkIsNumber
history = []

def calculatorMain():
    status = input("Deseja iniciar a calculadora? (on/off): ")
    while status == "on":
        valor1 = input("Digite o primeiro valor: ")
        if not checkIsNumber(valor1):
            continue
        operation = input("Digite a operação desejada: ")
        valor2 = input("Digite o segundo valor: ")
        if not checkIsNumber(valor2):
            continue
        calculator(operation, valor1, valor2)
        
    print("Calculador desligada")

def calculator(operation, valor1, valor2):
    validOperation = checkOperation(operation)

    if validOperation:
        result = performOperation(valor1, valor2, operation)
        history.append(addToHistory(valor1, valor2, operation, result))
        print(f"O resultado de {valor1} {operation} {valor2} é: {result}")
    else:   
        print("Operação inválida. Por favor, use +, -, * ou /.")
        return
    print("Deseja ver o histórico? (yes/no): ")
    seeHistory = input()
    if seeHistory == "yes":
        getHistory(history)
    else:
        print("Histórico não exibido.")
    status = input("Deseja continuar? (on/off): ")
    return status