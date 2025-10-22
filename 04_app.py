def conversor_divisas():
    # 1. Solicitar al usuario el monto en soles (PEN)
    try:
        monto_soles = float(input("Ingrese el monto en Soles (PEN) que desea cambiar: "))
    except ValueError:
        print("Error: El monto ingresado no es un número válido.")
        return

    # 2. Preguntar la tasa de cambio actual
    # Se pide cuántos soles (PEN) equivalen a 1 dólar (USD).
    try:
        tasa_cambio = float(input("Ingrese la tasa de cambio actual (ej. si 1 USD = 3.85 PEN, ingrese 3.85): "))
        if tasa_cambio <= 0:
            print("Error: La tasa de cambio debe ser un número positivo.")
            return
    except ValueError:
        print("Error: La tasa de cambio ingresada no es un número válido.")
        return

    # 3. Calcular el equivalente en dólares (USD)
    monto_dolares = monto_soles / tasa_cambio

    # 4. Mostrar el resultado con dos decimales
    print("\n--- Resultado de la Conversión ---")
    print(f"Monto ingresado: {monto_soles:.2f} PEN")
    print(f"Tasa de cambio: 1 USD = {tasa_cambio:.2f} PEN")
    print(f"Monto convertido: {monto_dolares:.2f} USD")
    print("----------------------------------")

# Llamar a la función para ejecutar el programa
conversor_divisas()
