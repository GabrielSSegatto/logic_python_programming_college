def mostra_valor(valor):
    print("recebi:", valor)
def mostra_dois_valores(num1, num2):
    print("recebi:",num1, num2)
def dobro(numero):
    return numero*2
def triplo(numero):
    return numero*3
def soma(numero1, numero2):
    return numero1+numero2
continuar = 's'
if __name__ == '__main__':
   
    '''a = int(input("Digite  o primeiro valor: "))
    b = int(input("Digite  o segundo valor: "))
    c = int(input("Digite  o terceiro valor: "))
    mostra_valor(a)
    mostra_valor(b)
    mostra_valor(c)

    mostra_dois_valores(20,500)'''

    while continuar == 's':
        toud = input("Digite 'd' pra calcular o dobro, e 't' pra calcular o triplo, s pra somar: ")
        while toud != 'd' and toud != 't' and toud != 's':
            toud = input("Digite 'd' pra calcular o dobro, e 't' pra calcular o triplo, s pra somar: ")
        if toud =='s':
             valor = int(input("Dê um valor inteiro: "))
             valor2 = int(input("Dê outro valor inteiro: "))
             soma_ = soma(valor, valor2)
             print("Resultado da soma:",soma_)
        elif toud == 'd':
             valor = int(input("Dê um valor inteiro: "))
             dobro_ = dobro(valor)
             print("O dobro é",dobro_)
        elif toud =='t':
             valor = int(input("Dê um valor inteiro: "))
             triplo_ = triplo(valor)
             print("O triplo é:", triplo_)
        continuar = input("deseja continuar o programa? s/n")
        while continuar != 's' and continuar != 'n':
             continuar = input("deseja continuar o programa? s/n ")
