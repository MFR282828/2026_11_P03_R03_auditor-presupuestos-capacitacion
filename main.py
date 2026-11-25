# ==============================================================================
# SAGA DE REPOSITORIOS PYTHON 2026
# Repositorio: 2026_11_P03_R03_auditor-presupuestos-capacitacion
# Principio 3: Funciones, parámetros y alcance de variables (Nivel: Avanzado)
# ==============================================================================


# --- FUNCIONES PURAS DE CÁLCULO UNITARIO ---

def calcular_coste_bruto(coste_participante, participantes):
    """Calcula el coste bruto multiplicando el coste unitario por los participantes."""
    coste_bruto = coste_participante * participantes
    return coste_bruto


def calcular_descuento(coste_bruto, porcentaje_descuento=0.0):
    """Calcula el importe del descuento a partir del coste bruto y un porcentaje."""
    importe_descuento = coste_bruto * (porcentaje_descuento / 100.0)
    return importe_descuento


def calcular_coste_final(coste_bruto, importe_descuento=0.0):
    """Calcula el coste neto final descontando la rebaja al coste bruto."""
    coste_final = coste_bruto - importe_descuento
    return coste_final


def calcular_coste_por_participante(coste_final, participantes):
    """Calcula el coste final real por participante evitando divisiones por cero."""
    if participantes <= 0:
        return 0.0
    coste_unitario_final = coste_final / participantes
    return coste_unitario_final


def evaluar_presupuesto(coste_final, presupuesto):
    """
    Clasifica el estado presupuestario y calcula la diferencia frente al presupuesto.
    Retorna una tupla (estado, diferencia), donde:
    - diferencia > 0: saldo disponible
    - diferencia == 0: presupuesto agotado exactamente
    - diferencia < 0: exceso presupuestario
    """
    diferencia = presupuesto - coste_final

    if coste_final < presupuesto:
        estado = "Dentro del presupuesto"
    elif coste_final == presupuesto:
        estado = "Presupuesto agotado"
    else:
        estado = "Exceso presupuestario"

    return estado, diferencia


# --- FUNCIONES DE COMPOSICIÓN Y PROCESAMIENTO ---

def analizar_capacitacion(capacitacion):
    """
    Coordina los cálculos individuales de una capacitación componiendo
    las funciones puras de cálculo y retorna un diccionario con el análisis completo.
    """
    nombre = capacitacion["nombre"]
    coste_participante = capacitacion["coste_participante"]
    participantes = capacitacion["participantes"]
    descuento_pct = capacitacion["descuento"]
    presupuesto = capacitacion["presupuesto"]

    # Llamadas con argumentos posicionales
    coste_bruto = calcular_coste_bruto(coste_participante, participantes)

    # Llamadas con argumentos por nombre (keyword arguments)
    importe_descuento = calcular_descuento(
        coste_bruto=coste_bruto,
        porcentaje_descuento=descuento_pct
    )
    coste_final = calcular_coste_final(
        coste_bruto=coste_bruto,
        importe_descuento=importe_descuento
    )

    # Llamada con argumentos posicionales
    coste_unitario_final = calcular_coste_por_participante(coste_final, participantes)

    # Desempaquetado de retorno múltiple (str, float)
    estado, diferencia = evaluar_presupuesto(
        coste_final=coste_final,
        presupuesto=presupuesto
    )

    return {
        "nombre": nombre,
        "participantes": participantes,
        "coste_bruto": coste_bruto,
        "descuento_pct": descuento_pct,
        "importe_descuento": importe_descuento,
        "coste_final": coste_final,
        "coste_por_participante": coste_unitario_final,
        "presupuesto": presupuesto,
        "diferencia": diferencia,
        "estado": estado
    }


def procesar_capacitaciones(lista_capacitaciones):
    """Procesa una lista de capacitaciones y retorna una lista con sus análisis."""
    resultados_analizados = []
    for cap in lista_capacitaciones:
        resultado = analizar_capacitacion(cap)
        resultados_analizados.append(resultado)
    return resultados_analizados


def calcular_resumen_consolidado(resultados_analizados):
    """
    Agrega las métricas globales de todas las capacitaciones analizadas
    y retorna un diccionario con el informe consolidado.
    """
    total_capacitaciones = len(resultados_analizados)
    total_participantes = 0
    coste_bruto_acumulado = 0.0
    descuento_acumulado = 0.0
    coste_final_acumulado = 0.0
    presupuesto_acumulado = 0.0

    dentro_presupuesto = 0
    presupuesto_agotado = 0
    exceso_presupuestario = 0

    for item in resultados_analizados:
        total_participantes += item["participantes"]
        coste_bruto_acumulado += item["coste_bruto"]
        descuento_acumulado += item["importe_descuento"]
        coste_final_acumulado += item["coste_final"]
        presupuesto_acumulado += item["presupuesto"]

        if item["estado"] == "Dentro del presupuesto":
            dentro_presupuesto += 1
        elif item["estado"] == "Presupuesto agotado":
            presupuesto_agotado += 1
        elif item["estado"] == "Exceso presupuestario":
            exceso_presupuestario += 1

    balance_acumulado = presupuesto_acumulado - coste_final_acumulado

    return {
        "total_capacitaciones": total_capacitaciones,
        "total_participantes": total_participantes,
        "coste_bruto_acumulado": coste_bruto_acumulado,
        "descuento_acumulado": descuento_acumulado,
        "coste_final_acumulado": coste_final_acumulado,
        "presupuesto_acumulado": presupuesto_acumulado,
        "dentro_presupuesto": dentro_presupuesto,
        "presupuesto_agotado": presupuesto_agotado,
        "exceso_presupuestario": exceso_presupuestario,
        "balance_acumulado": balance_acumulado
    }


# --- FUNCIONES DE PRESENTACIÓN ---

def mostrar_resultados_individuales(resultados, moneda="S/"):
    """Presenta en consola el desglose individual de cada capacitación."""
    print("\n======================================================================")
    print("         INFORME INDIVIDUAL DE CAPACITACIONES EMPRESARIALES           ")
    print("======================================================================")

    for item in resultados:
        print(f"Capacitación:                 {item['nombre']}")
        print(f"Número de participantes:      {item['participantes']}")
        print(f"Coste bruto:                  {moneda} {item['coste_bruto']:,.2f}")
        print(f"Descuento aplicado:           {item['descuento_pct']:.2f} %")
        print(f"Importe descontado:          -{moneda} {item['importe_descuento']:,.2f}")
        print(f"Coste final:                  {moneda} {item['coste_final']:,.2f}")
        print(f"Coste por participante:       {moneda} {item['coste_por_participante']:,.2f}")
        print(f"Presupuesto asignado:         {moneda} {item['presupuesto']:,.2f}")

        if item["diferencia"] >= 0:
            print(f"Saldo disponible:             {moneda} {item['diferencia']:,.2f}")
        else:
            print(f"Exceso presupuestario:        {moneda} {abs(item['diferencia']):,.2f}")

        print(f"Estado presupuestario:        {item['estado']}")
        print("----------------------------------------------------------------------")


def mostrar_resumen_consolidado(resumen, moneda="S/"):
    """Presenta en consola el balance general acumulado de todas las capacitaciones."""
    print("\n======================================================================")
    print("               RESUMEN PRESUPUESTARIO CONSOLIDADO                     ")
    print("======================================================================")
    print(f"Capacitaciones analizadas:          {resumen['total_capacitaciones']}")
    print(f"Total de participantes:             {resumen['total_participantes']}")
    print("----------------------------------------------------------------------")
    print(f"Coste bruto acumulado:              {moneda} {resumen['coste_bruto_acumulado']:,.2f}")
    print(f"Descuento total acumulado:         -{moneda} {resumen['descuento_acumulado']:,.2f}")
    print(f"Coste final total:                  {moneda} {resumen['coste_final_acumulado']:,.2f}")
    print(f"Presupuesto total asignado:         {moneda} {resumen['presupuesto_acumulado']:,.2f}")
    print("----------------------------------------------------------------------")
    print(f"Dentro del presupuesto:             {resumen['dentro_presupuesto']}")
    print(f"Presupuesto agotado:                {resumen['presupuesto_agotado']}")
    print(f"Exceso presupuestario:              {resumen['exceso_presupuestario']}")
    print("----------------------------------------------------------------------")

    balance = resumen["balance_acumulado"]
    if balance > 0:
        print(f"Balance presupuestario acumulado:   {moneda} {balance:,.2f} (Saldo a favor)")
    elif balance == 0:
        print(f"Balance presupuestario acumulado:   {moneda} 0.00 (Presupuesto exacto)")
    else:
        print(f"Balance presupuestario acumulado:   {moneda} {abs(balance):,.2f} (Exceso)")

    print("======================================================================\n")


# --- FUNCIÓN COORDINADORA PRINCIPAL ---

def main():
    """Coordina la carga de datos locales, el análisis y la emisión de informes."""
    capacitaciones_programadas = [
        {
            "nombre": "Excel avanzado",
            "coste_participante": 120.0,
            "participantes": 15,
            "descuento": 10.0,
            "presupuesto": 2000.0
        },
        {
            "nombre": "Seguridad industrial",
            "coste_participante": 85.0,
            "participantes": 20,
            "descuento": 0.0,
            "presupuesto": 1700.0
        },
        {
            "nombre": "Liderazgo",
            "coste_participante": 250.0,
            "participantes": 8,
            "descuento": 15.0,
            "presupuesto": 1800.0
        },
        {
            "nombre": "Power BI",
            "coste_participante": 180.0,
            "participantes": 12,
            "descuento": 5.0,
            "presupuesto": 2000.0
        }
    ]

    analisis_individuales = procesar_capacitaciones(capacitaciones_programadas)
    resumen_general = calcular_resumen_consolidado(analisis_individuales)

    mostrar_resultados_individuales(resultados=analisis_individuales, moneda="S/")
    mostrar_resumen_consolidado(resumen=resumen_general, moneda="S/")


if __name__ == "__main__":
    main()