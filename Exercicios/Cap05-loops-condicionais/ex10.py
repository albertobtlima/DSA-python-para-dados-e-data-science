frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.".lower()
letraR = 0

for letra in frase:
    if letra == "r":
        letraR += 1

print(frase)
print(f"A letra 'R' aparece {letraR} vezes na frase.")
