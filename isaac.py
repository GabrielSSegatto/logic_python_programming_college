def age(a,b,c):
    if a>=360:
        quantidade_anos = a//360
        a = a - (360 * quantidade_anos)
    else:
        quantidade_anos = 0
    if a>=30:
        quantidade_meses = a//30
        a = a - (30 * quantidade_meses) 
    else:
        quantidade_meses = 0
    print(f"{quantidade_anos} ano(s), {quantidade_meses} mes(es), {a} dia(s)")

    if b>=360:
        quantidade_anos = b//360
        b = b - (360 * quantidade_anos) 
    else: 
        quantidade_anos = 0
    if b>=30:
        quantidade_meses = b//30
        b = b - (30 * quantidade_meses) 
    else: quantidade_meses = 0
    print(f"{quantidade_anos} ano(s), {quantidade_meses} mes(es), {b} dia(s)")

    if c>=360:
        quantidade_anos = c//360
        c = c - (360 * quantidade_anos) 
    else:
        quantidade_anos = 0
    if c>=30:
        quantidade_meses = c//30
        c = c - (30 * quantidade_meses)
    else:
        quantidade_meses = 0
    print(f"{quantidade_anos} ano(s), {quantidade_meses} mes(es), {c} dia(s)")


mellin = input().split()
a = int(mellin[0])
b = int(mellin[1])
c = int(mellin[2])
age(a, b, c)

