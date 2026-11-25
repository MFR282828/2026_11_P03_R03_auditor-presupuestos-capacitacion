# Auditor de Presupuestos de Capacitación

Aplicación de consola (CLI) desarrollada en Python para auditar un conjunto de capacitaciones empresariales, calcular sus costes reales, clasificar el estado presupuestario individual y emitir un informe consolidado mediante composición de funciones.

---

## Objetivo académico

Consolidar el **Principio 3: Funciones, parámetros y alcance de variables** en un escenario de nivel avanzado:
- Distribución limpia de responsabilidades entre funciones de cálculo, procesamiento y presentación.
- Transmisión explícita de datos mediante parámetros y valores de retorno (`float`, `tuple`, `dict`, `list`), eliminando dependencias de variables globales.
- Uso combinado de argumentos posicionales, argumentos por nombre (*keyword arguments*) y parámetros con valores predeterminados.
- Composición de funciones donde el resultado de operaciones atómicas alimenta análisis individuales y agregaciones consolidadas.
- Control estricto del alcance local (*local scope*) de cada variable.

---

## Principio trabajado

- **Principio Principal:** **Principio 3. Funciones, parámetros y alcance de variables** (Nivel: Avanzado)

### Mapa de Principios de la Saga Python 2026

- [X] **Principio 1. Fundamentos del lenguaje Python**
- [X] **Principio 2. Control de flujo y estructuras de datos básicas**
- [X] **Principio 3. Funciones, parámetros y alcance de variables**
- [ ] Principio 4. Manejo de errores y excepciones
- [ ] Principio 5. Comprensiones y código idiomático de Python
- [ ] Principio 6. Calidad del código y convenciones profesionales
- [ ] Principio 7. Programación Orientada a Objetos (POO)
- [ ] Principio 8. Complejidad algorítmica y análisis de eficiencia
- [ ] Principio 9. Módulos, paquetes y reutilización de código
- [ ] Principio 10. PIP, entornos virtuales y dependencias
- [ ] Principio 11. Aplicaciones CRUD y persistencia de datos
- [ ] Principio 12. Testing y validación automatizada
- [ ] Principio 13. Estadística computacional, simulación y programación dinámica
- [ ] Principio 14. Arquitectura de proyectos y distribución de paquetes
- [ ] Principio 15. Principios SOLID y patrones de diseño

---

## Funcionalidades

1. **Cálculo financiero unitario:** Obtención independiente del coste bruto, descuento aplicado, coste final y coste unitario real por participante.
2. **Clasificación presupuestaria:** Evaluación automática de cada capacitación en *Dentro del presupuesto*, *Presupuesto agotado* o *Exceso presupuestario*.
3. **Informe individual:** Desglose detallado de métricas, saldos y estados por cada capacitación analizada.
4. **Resumen consolidado:** Agregación de participantes, costes acumulados, conteos por estado presupuestario y balance financiero global.

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3 (Biblioteca estándar exclusivamente).
- **Entorno de desarrollo:** VS Code / Terminal PowerShell.
- **Control de versiones:** Git & GitHub.

---

## Estructura del repositorio

```text
2026_11_P03_R03_auditor-presupuestos-capacitacion/
├── .gitignore
├── main.py
└── README.md