def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


while True:
    try:
        x, y = map(int, input().split())
        total = fatorial(x) + fatorial(y)
        print(total)
    except EOFError:
        break
