# Estrutura para armazenar os dados de cada habitante
habitantes = [
    {"sexo": "feminino", "olhos": "azuis", "cabelos": "louros", "idade": 25},
    {"sexo": "masculino", "olhos": "castanhos", "cabelos": "pretos", "idade": 40},
    {"sexo": "feminino", "olhos": "verdes", "cabelos": "louros", "idade": 30},
    {"sexo": "feminino", "olhos": "castanhos", "cabelos": "castanhos", "idade": 20},
    {"sexo": "masculino", "olhos": "verdes", "cabelos": "louros", "idade": 22},
    {"sexo": "feminino", "olhos": "verdes", "cabelos": "louros", "idade": 35},
    {"sexo": "feminino", "olhos": "azuis", "cabelos": "louros", "idade": 19},
    {"sexo": "masculino", "olhos": "verdes", "cabelos": "louros", "idade": 29},
]

# a) Determinar a maior e a menor idade e a média das idades
idades = [habitante["idade"] for habitante in habitantes]
maior_idade = max(idades)
menor_idade = min(idades)
media_idades = sum(idades) / len(idades)

# b) Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive
feminino_18_35 = len([habitante for habitante in habitantes if habitante["sexo"] == "feminino" and 18 <= habitante["idade"] <= 35])

# c) Quantidade de indivíduos com olhos verdes e cabelos louros
olhos_verdes_cabelos_louros = len([habitante for habitante in habitantes if habitante["olhos"] == "verdes" and habitante["cabelos"] == "louros"])

# Exibição dos resultados
print(f"a) Maior idade: {maior_idade}")
print(f"a) Menor idade: {menor_idade}")
print(f"a) Média das idades: {media_idades:.2f}")

print(f"b) Quantidade de mulheres entre 18 e 35 anos: {feminino_18_35}")

print(f"c) Quantidade de indivíduos com olhos verdes e cabelos louros: {olhos_verdes_cabelos_louros}")

