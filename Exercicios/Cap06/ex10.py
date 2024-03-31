import re

texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'
resultado = re.findall(r'Data Science (\w+)', texto)

print("A palavra após 'Data Science' é:", resultado[0])
