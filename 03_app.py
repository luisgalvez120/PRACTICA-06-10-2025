#CALCULO DE SUELDOS AUTOMATIZADO

#Datos de entrada = MES SEPTIEMBRE

vendedores = [
{"nombre": "ANA", "sueldo_base": 2500, "ventas_mes": 10000},
{"nombre": "BETO", "sueldo_base": 2300, "ventas_mes": 7500},
{"nombre": "CARLA", "sueldo_base": 2400, "ventas_mes": 8200}]

#CALCULO PARA PAGO FINAL
def calcular_sueldo(vendedor):
    ventas = vendedor["ventas_mes"]
    sueldo_base = vendedor["sueldo_base"]

#REGLA 1: Comisión Base (8% sobre ventas)
    comision = 0.08 * ventas

#REGLA 2: Bono por Rendimiento (S/ 300 si ventas > 8000)
    bono = 300 if ventas > 8000 else 0

#REGLA 3: Impuesto (8% sobre comision + bono)
    impuesto = 0.08 * (comision + bono)

#REGLA 4: Sueldo Final Neto
    sueldo_final = sueldo_base + comision + bono - impuesto

#DATOS DETALADOS
    return {
        "nombre": vendedor["nombre"],
        "sueldo_base": sueldo_base,
        "ventas_mes": ventas,
        "comision": comision,
        "bono": bono,
        "impuesto": impuesto,
        "sueldo_final": sueldo_final
    }

#CALCULO PARA LOS TRABAJAORES
resultados = [calcular_sueldo(v) for v in vendedores]

# REPORTE DETALLADO
print("REPORTE DE SUELDOS - MES DE SETIEMBRE\n")
for r in resultados:
    print(f"REPORTE FIN DE MES: {r['nombre']}")
    print(f"  Sueldo Base:           S/ {r['sueldo_base']:.2f}")
    print(f"  Ventas del Mes:        S/ {r['ventas_mes']:.2f}")
    print(f"  Comisión (8%):         S/ {r['comision']:.2f}")
    print(f"  Bono por Rendimiento:  S/ {r['bono']:.2f}")
    print(f"  Impuesto (8%):         S/ {r['impuesto']:.2f}")
    print(f"  Sueldo Final Neto:     S/ {r['sueldo_final']:.2f}")
    print("-" * 45)
