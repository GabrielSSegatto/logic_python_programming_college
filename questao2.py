def calcular_idade(nascimento):
    return 2025 - nascimento
if __name__ == "__main__":
    nascimento = int(input("Digite p ano de nascimento: "))
    idade = calcular_idade(nascimento)
    print("você tem:", idade, "anos")