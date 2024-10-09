def calcular_salario():
    # Entrada de dados
    valor_hora = float(input("Digite quanto o funcionário recebe por hora: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

    # Cálculos
    salario_bruto = valor_hora * horas_trabalhadas
    desconto_irrf = salario_bruto * 0.11
    desconto_inss = salario_bruto * 0.08
    desconto_sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - (desconto_irrf + desconto_inss + desconto_sindicato)

    # Resultados
    print(f"\na) Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"b) Quanto pagou ao IRRF: R$ {desconto_irrf:.2f}")
    print(f"c) Quanto pagou ao INSS: R$ {desconto_inss:.2f}")
    print(f"d) Quanto pagou ao Sindicato: R$ {desconto_sindicato:.2f}")
    print(f"e) Salário Líquido: R$ {salario_liquido:.2f}")

# Chamada da função
calcular_salario()
