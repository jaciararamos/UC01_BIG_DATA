def registrar_temperaturas():
    temperaturas = []  # Vetor para armazenar as temperaturas

    while True:
        try:
            # Receber a temperatura do usuário
            temp = float(input("Digite uma temperatura (ou digite 'sair' para finalizar): "))
            temperaturas.append(temp)
        except ValueError:
            # Caso o usuário digite 'sair', interrompe o laço
            break

    if temperaturas:
        menor = min(temperaturas)
        maior = max(temperaturas)
        media = sum(temperaturas) / len(temperaturas)

        print(f"\nMenor temperatura registrada: {menor}°C")
        print(f"Maior temperatura registrada: {maior}°C")
        print(f"Média das temperaturas: {media:.2f}°C")
    else:
        print("Nenhuma temperatura foi registrada.")

registrar_temperaturas()

