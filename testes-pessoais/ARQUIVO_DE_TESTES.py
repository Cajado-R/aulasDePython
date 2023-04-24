salario = float(input('Valor a Receber: R$ '))

impostoDeRenda = 0.11 * salario
inss = 0.08 * salario
sindicato = 0.05 * salario
descontos = impostoDeRenda + inss + sindicato
salarioLiquido = salario - descontos
print(f'Salario Bruto R${salario:.2f} \n'
      f'- IR R${impostoDeRenda :.2f} \n'
      f'- INSS R${inss :.2f} \n'
      f'- Sindicato R${sindicato :.2f} \n'
      f'+ Salario Liquido R${salarioLiquido :.2f}')
