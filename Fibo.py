def fibonacci():   
    numinp = int(input("Digite o número que deseja saber se faz parte da sequência de Fibonacci: "))

    fibo0 = 0
    fibo1 = 1
    fibo = 0

    while fibo <= numinp:
        if numinp == fibo:
            print(numinp, " foi o número digitado por você, ele pertence a sequência de Fibonacci.")
            break
        fibo = fibo0 + fibo1
        fibo0 = fibo1
        fibo1 = fibo
    else:
        print(numinp, " foi o número digitado por você, ele não pertence a sequência de Fibonacci.")

if __name__ == "__main__":
    fibonacci()