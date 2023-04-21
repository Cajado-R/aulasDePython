
excesso = 0.0
while True:
    pesoDoPeixe = float(input('Peso: '))
    if pesoDoPeixe < 50:
        print(f'O peso do peixe não excedeu 50KG, o peso do seu peixe é: {pesoDoPeixe}KG')
        break
    else:
        excesso = (pesoDoPeixe - 50.0) * 4.00
        print(f'O valor a pagar será de: R${excesso}')
        break
