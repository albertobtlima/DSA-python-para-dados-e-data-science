"""
def temperatura(arg1):
    global Fahrenheit
    for _ in arg1:
        Fahrenheit = map(lambda x: (float(1.8)) * x + 32, Celsius)
    print(list(Fahrenheit))
"""

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(1.8)) * x + 32, Celsius)
print(list(Fahrenheit))
