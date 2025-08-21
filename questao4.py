
'''
Enunciado:Realizar um programa que leia um número inteiro e verifique 
se ele é par ou ímpar. Caso o número seja par, deve-se imprimir
a mensagem "O número é par". Caso contrário, deve-se imprimir a
 mensagem "O número é ímpar".
'''
continuar = True
while continuar == True:    
    def par_ou_impar(numero):
        if numero % 2 == 0:
            return "O número é par"
        else:
            return "O número é ímpar"
    if __name__ == "__main__":
        numero = int(input("Digite um número inteiro: "))
        resultado = par_ou_impar(numero)
        print(resultado)
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            continuar = False
            print("Programa encerrado.")
        else:
            continuar = True
