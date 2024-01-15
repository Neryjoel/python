peso = float(input("ingrese su peso: "))
altura= float(input("ingrese su altura: "))

imc = peso/(altura**2)
print(f"tu IMC es: {imc:.2f}")