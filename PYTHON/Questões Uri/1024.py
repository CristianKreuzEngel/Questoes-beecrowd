def criptografar(texto):
    firstString = ''
    for char in texto:
        if char.isalpha():
            firstString += chr(ord(char) + 3)
        else:
            firstString += char
    secondString = firstString[::-1]
    n = len(secondString)
    metade = n // 2
    bronzeString = secondString[:metade]
    for i in range(metade, n):
        bronzeString += chr(ord(secondString[i]) - 1)

    return bronzeString


qtd = int(input())
for i in range(qtd):
    texto = input()
    print(criptografar(texto))
