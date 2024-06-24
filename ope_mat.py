# Operações matematicas simples com python 



def realizar_operacoes(num1, num2):
   
    adicao = num1 + num2
    
   
    subtracao = num1 - num2
    
   
    multiplicacao = num1 * num2
    
    
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Erro: Divisão por zero não é permitida"
    
    return adicao, subtracao, multiplicacao, divisao


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando as operações
adicao, subtracao, multiplicacao, divisao = realizar_operacoes(num1, num2)


print(f"Adição: {adicao}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")