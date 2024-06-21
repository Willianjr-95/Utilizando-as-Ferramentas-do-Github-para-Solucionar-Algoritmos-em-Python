
# vamos solicitar uma string e um numero inteiro como entrada. depois retorne a string repetida o numero de vezes informado em python

def repetir_string():
    # Solicitando a entrada da string
    string_input = input("Digite uma string: ")
    
   
    numero_input = int(input("Digite um número inteiro: "))
    
   
    resultado = string_input * numero_input
    
    return resultado


resultado = repetir_string()
print("Resultado:", resultado)
