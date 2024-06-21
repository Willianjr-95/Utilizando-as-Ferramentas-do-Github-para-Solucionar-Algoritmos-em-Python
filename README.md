# Algoritimo em python que vai recebe dois dados diferentes e concatena-los em uma única string 

ef concatenar_dados(dado1, dado2):
   
    dado1_str = str(dado1)
    dado2_str = str(dado2)
    
   
    resultado = dado1_str + dado2_str
    
    return resultado


    dado1 = "Olá"
    dado2 = 123
     resultado = concatenar_dados(dado1, dado2)
    print("Resultado da concatenação:", resultado)
