# Calculadora Python
import re

print('Olá!')

# Loop infinito para manter a calculadora rodando
while True:

    # Solicita ao usuário que digite uma operação
    operação = input('Digite uma operação:')

    # Substitui vírgulas por pontos, para aceitar números decimais com vírgula
    operação = operação.replace(',', '.')
    
    # Expressão regular para extrair os dois números e o operador, ignorando espaços
    conta = re.search(r'^\s*([0-9]+(?:\.[0-9]+)?)\s*([\+\-\*/])\s*([0-9]+(?:\.[0-9]+)?)\s*$', operação)

    if conta:
        a = float(conta.group(1))
        b = str(conta.group(2))
        c = float(conta.group(3))

# Executa a operação com base no operador encontrado
        if b == '+':
            resultado = a + c

        elif b == '-':
            resultado = a - c

        elif b == '*':
            resultado = a * c

        else:
            resultado = a / c
# Exibe resultado
        print(round(resultado, 2))
