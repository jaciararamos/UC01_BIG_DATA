usuarios = ["pedro","maria","duda","dirceu","elvis"]
senhas = ["123","345","567","@@@$$$","8910"]
usuario = input("Informe o nome de acesso ao sistema: ")
for i in range(len(usuarios)):
    if usuarios[i] == usuario:
        senha = input("Informe a senha de acesso: ")
        if senhas[i] == senha:
            resp = "Acesso Liberado"
        else:
            resp = "Senha não Confere"
        break
    else:
        resp = "Usuário não Encontrado"
print(resp)