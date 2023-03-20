# calculadora que soma, diminui, multiplica, divide
# e calcula raiz quadrada

def calculator(a, b):
    return a + b, a - b, a * b, a / b, a**0.5, b**0.5

while True:
    try:
         n1 = int(input("Digite um número: "))
         n2 = int(input("Digite outro número: "))
         calc1 = calculator(n1, n2)        
         print(f"Soma: {n1+n2}\nSubtração: {n1-n2}\nMultiplicação: {n1*n2}\nDivisão: {n1/n2:.1f}")
         print(f"1a raiz quadrada: {n1**0.5:.1f}\n2a raiz quadrada: {n2**0.5:.1f}")
         break
    except ValueError:
         print("Digite um número válido.")