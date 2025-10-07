# Datos de entrada (Mes de Setiembre)
vendedores = [
    {"nombre": "Ana", "sueldo_base": 2500, "ventas_mes": 9500},
    {"nombre": "Beto", "sueldo_base": 2200, "ventas_mes": 7800},
    {"nombre": "Carla", "sueldo_base": 2800, "ventas_mes": 12000}
]

# Constantes del negocio
COMISION = 0.08
BONO = 300
BONO_MIN_VENTAS = 8000
IMPUESTO = 0.08

# Procesamiento de datos
for v in vendedores:
    comision = v["ventas_mes"] * COMISION
    bono = BONO if v["ventas_mes"] > BONO_MIN_VENTAS else 0
    impuesto = (comision + bono) * IMPUESTO
    sueldo_final = v["sueldo_base"] + comision + bono - impuesto

    # Reporte detallado
    print("=" * 55)
    print(f"Reporte para {v['nombre']}")
    print("=" * 55)
    print(f"Sueldo Base      : S/ {v['sueldo_base']:.2f}")
    print(f"Ventas del Mes   : S/ {v['ventas_mes']:.2f}")
    print("-" * 55)
    print(f"+ Comisi��n (8%)  : S/ {comision:.2f}")
    print(f"+ Bono           : S/ {bono:.2f}")
    print(f"- Impuesto (8%)  : S/ {impuesto:.2f}")
    print("=" * 55)
    print(f"Sueldo Final Neto: S/ {sueldo_final:.2f}")
    print("=" * 55, "\n")