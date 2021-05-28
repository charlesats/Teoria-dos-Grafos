salario = input("Informe o salário do funcionário!\n$")
salario = float(salario)

if salario <= 1903.98:
    print("Isento")
elif salario <= 2826.65:
    print("Alíquota: 7.5 \t Dedução: $%.2f" % 142.80)
elif salario <= 3751.05:
    print("Alíquota: 15.0 \t Dedução: $%.2f" % 354.80)
elif salario <= 4664.68:
    print("Alíquota: 22.5 \t Dedução: $%.2f" % 636.13)
else:
    print("Alíquota: 27.5 \t Dedução: $%.2f" % 869.36)
