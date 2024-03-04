print("Informe o dia da semana:\n")
print("1 - Segunda a Sexta.")
print("2 - Sabado ou Domingo.\n")

resposta = input("Sua resposta: ")

if resposta == "1":
    print("\nVocê precisa trabalhar!")
elif resposta == "2":
    print("\nHoje é dia de descanso")
else:
    print("\nResposta invalida.")
