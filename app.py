from operaciones import sumar, restar, multiplicar, dividir

def main():
    print("🧮 Calculadora sencilla de Omar 🧮")
    a = 10
    b = 5

    print(f"Suma: {a} + {b} = {sumar(a, b)}")
    print(f"Resta: {a} - {b} = {restar(a, b)}")
    print(f"Multiplicación: {a} * {b} = {multiplicar(a, b)}")
    print(f"División: {a} / {b} = {dividir(a, b)}")

if __name__ == "__main__":
    main()
