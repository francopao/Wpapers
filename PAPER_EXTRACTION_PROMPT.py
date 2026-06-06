# ═══════════════════════════════════════════════════════════════════════════════
# INVEST MEMORIA — MASTER PROMPT DE EXTRACCIÓN DE PAPERS
# ═══════════════════════════════════════════════════════════════════════════════
#
# USO: Copia este prompt completo en Claude, ChatGPT o Gemini.
# Luego pega el texto del paper (abstract + secciones clave) al final.
# Output: bloque Python listo para pegar en content/invest_cards.py
#
# RECOMENDACIÓN: Usa Claude Opus o GPT-4o para mayor calidad.
# ═══════════════════════════════════════════════════════════════════════════════

MASTER_PROMPT = """
Eres un experto en inversiones institucionales y en diseño de sistemas de aprendizaje activo.
Tu tarea es leer el siguiente working paper o research report y extraer entre 4 y 8 flashcards
de alta calidad para la plataforma Invest Memoria.

═══════════════════════════
CONTEXTO DEL USUARIO
═══════════════════════════
Soy analista de inversiones en una AFP. Necesito dominar los conceptos más valiosos de este paper
para aplicarlos a: (1) construir o mejorar views de inversión, (2) generar ideas de portafolio,
(3) comunicar insights a comités institucionales. Prioriza lo que sea ACCIONABLE y DIFERENCIADOR.

═══════════════════════════
DOMINIOS DISPONIBLES (elige el más apropiado)
═══════════════════════════
"Equity Investing" | "Fixed Income" | "Alternatives" | "Thematic Investing" |
"ESG" | "Asset Allocation" | "Trading Strategy"

═══════════════════════════
NIVELES DE DIFICULTAD
═══════════════════════════
"Foundational" → definición y concepto básico
"Intermediate" → aplicación, comparación, implicancias
"Advanced"     → derivación, limitaciones, síntesis crítica
"Expert"       → juicio profesional, casos edge, debate académico

═══════════════════════════
MODO TAGS
═══════════════════════════
"bus"  → sin papel/calculadora, respuesta conceptual o numérica mental
"home" → permite derivaciones largas, código, análisis detallado
["bus", "home"] → apto para ambos modos

═══════════════════════════
ESTRUCTURA OBLIGATORIA POR CARTA
═══════════════════════════
Cada carta DEBE tener como mínimo: id, domain, topic, difficulty, mode_tags, source, front, back.
Y DEBE incluir AL MENOS DOS de estos elementos enriquecedores:

1. mcq: Pregunta de opción múltiple con 4 alternativas, respuesta correcta (A/B/C/D) y explicación detallada
2. true_false: Afirmación verdadera o falsa con explicación (preferir afirmaciones NO triviales, diseñadas para revelar malentendidos comunes)
3. fill_blank: Completar la oración con template y lista de respuestas aceptadas
4. numerical_problem: Para problemas cuantitativos. Incluye question, steps (lista), answer, y bus_hint (versión resumida para hacer en la cabeza en el bus — sin calculadora, usando aproximaciones redondas)
5. graph_type: Tipo de gráfico conceptual relevante (ver lista abajo)
6. intuition: Explicación en lenguaje simple de POR QUÉ funciona el mecanismo — la analogía o insight que hace que "haga click"
7. derivation: Pasos matemáticos clave si aplica
8. code_python: Snippet de 10-20 líneas que ilustra el concepto (numpy/pandas/scipy)
9. connections: Lista de conceptos relacionados dentro del ecosistema de inversiones
10. latex: Fórmula LaTeX del concepto principal (sin los signos $)

═══════════════════════════
TIPOS DE GRÁFICO DISPONIBLES (graph_type)
═══════════════════════════
Usa exactamente uno de estos strings cuando la carta se beneficie de una visualización:

EQUITY:
  "momentum_decile_returns"     → retornos por decil, formación 12M
  "gordon_sensitivity"          → sensibilidad precio vs. g y r en DDM
  "hml_cumulative"              → retorno acumulado HML factor
  "accruals_returns"            → retornos por quintil de accruals
  "earnings_surprise_drift"     → PEAD: precio alrededor de earnings surprise
  "pe_ratio_vs_growth"          → P/E vs. crecimiento esperado de earnings

FIXED INCOME:
  "price_yield_convexity"       → curva precio-yield con tangente y convexidad
  "yield_curve_shapes"          → curvas: normal, invertida, flat, humped
  "duration_risk_ladder"        → ladder de vencimientos con duration
  "credit_spread_history"       → spread IG vs HY en el tiempo (con recesiones)
  "oas_vs_zspread"             → comparación OAS vs Z-spread por tipo de bono

ALTERNATIVES:
  "pe_cashflow_j_curve"         → J-curve de flujos PE: llamadas, distribuciones, NAV
  "hedge_fund_dispersion"       → dispersión de retornos por estrategia
  "real_assets_correlation"     → matriz de correlación multi-activo incluyendo reales

THEMATIC:
  "ai_value_chain"              → cadena de valor IA: infra → modelos → apps
  "theme_adoption_s_curve"      → curva S de adopción tecnológica
  "sector_rotation_cycle"       → rotación sectorial por fase del ciclo

ESG:
  "esg_score_return_scatter"    → scatter ESG score vs retorno por sector
  "carbon_intensity_by_sector"  → intensidad carbono por sector
  "esg_materiality_matrix"      → matriz materialidad SASB por industria

ASSET ALLOCATION:
  "efficient_frontier_bl"       → frontera eficiente con portafolios MVO vs BL
  "risk_parity_contributions"   → contribuciones al riesgo: 60/40 vs risk parity
  "correlation_matrix_regimes"  → correlaciones en régimen normal vs crisis

TRADING:
  "vwap_execution_profile"      → perfil de volumen intradía con ejecución VWAP
  "bid_ask_spread_components"   → descomposición del spread en componentes
  "pairs_spread_zscore"         → z-score del spread en pairs trading con señales

═══════════════════════════
CRITERIOS DE CALIDAD — OBLIGATORIOS
═══════════════════════════

✅ PRIORIZA insights que NO son obvios o que contradicen el conocimiento convencional
✅ Para numerical_problem en modo bus: usa números redondos y pasos de cálculo mental
   Ejemplo bus_hint correcto: "10%×100 = 10 → 10/0.05 = 200" (no requiere calculadora)
✅ Para true_false: diseña afirmaciones que PARECEN verdaderas pero son falsas, o viceversa
   — el objetivo es revelar y corregir malentendidos comunes del campo
✅ Para mcq: los distractores deben ser plausibles (errores que un analista real cometería)
   — no opciones absurdas o trivialmente incorrectas
✅ Para fill_blank: úsalo para conceptos donde la terminología exacta importa
✅ El campo "intuition" debe ser una analogía o metáfora memorable, NO una repetición del "back"
✅ El campo "source" debe incluir: Autores (año) — Journal/Institución; y si hay paper SSRN/DOI, inclúyelo
✅ Las cartas de nivel Advanced/Expert deben incluir limitaciones del modelo o hallazgos que lo contradicen

❌ NO incluyas definiciones que aparecerían en cualquier manual básico de finanzas
❌ NO repitas la misma idea en múltiples cartas (varía el ángulo: formulación, aplicación, crítica, extensión)
❌ NO uses números que requieran calculadora compleja en bus_hint — approximaciones del 1-5% de error son aceptables

═══════════════════════════
FORMATO DE OUTPUT EXACTO
═══════════════════════════
Responde ÚNICAMENTE con un bloque Python válido, listo para pegar en invest_cards.py.
No incluyas texto introductorio, no incluyas markdown adicional.
Usa IDs únicos con formato: [3 letras dominio]_[3 letras tema]_[número].
Ejemplo: "eq_mom_001", "fi_dur_001", "alt_pe_001", "th_ai_001", "esg_mat_001", "aa_bl_001", "ts_vwap_001"

TEMPLATE PARA CADA CARTA:
{
    "id": "XX_XXX_001",
    "domain": "Asset Allocation",          # uno de los 7 dominios
    "topic": "Nombre del Tema",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Autor (año) — Journal; DOI si disponible",

    # SIEMPRE presentes:
    "front": "Pregunta clara, específica, orientada a comprensión profunda. Evita preguntas de definición pura.",
    "back": "Respuesta completa, técnicamente rigurosa, con matices importantes. 3-5 oraciones.",
    "latex": r"Formula\\ si\\ aplica",      # omitir si no aplica

    # MÍNIMO 2 de los siguientes:
    "mcq": {
        "question": "Pregunta específica del concepto de esta carta (puede diferir del front).",
        "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
        "answer": "B",
        "explanation": "Por qué B es correcto Y por qué los otros distractores son incorrectos o incompletos."
    },
    "true_false": {
        "statement": "Afirmación diseñada para revelar un malentendido común. Evitar trivialidades.",
        "answer": True,   # o False
        "explanation": "Explicación rigurosa de por qué es V o F, con el matiz importante."
    },
    "fill_blank": {
        "template": "Oración con _______ donde va el término o concepto clave.",
        "answers": ["respuesta1", "respuesta2", "sinónimo aceptable"]
    },
    "numerical_problem": {
        "question": "Problema cuantitativo con datos concretos. Usa números redondos.",
        "steps": ["Paso 1: ...", "Paso 2: ...", "Paso 3: ..."],
        "answer": "Resultado con unidades",
        "bus_hint": "Versión ultra-condensada: operaciones que se hacen mentalmente sin calculadora"
    },
    "graph_type": "nombre_del_grafico",     # de la lista aprobada, omitir si no aplica
    "intuition": "Analogía o metáfora memorable que hace 'click' el mecanismo. Max 3 oraciones.",
    "derivation": "Pasos matemáticos si el paper tiene modelo formal relevante.",
    "code_python": '''
import numpy as np
# Snippet corto que ilustra el concepto (10-20 líneas)
    ''',
    "connections": ["Concepto relacionado 1", "Concepto relacionado 2", "Paper relacionado"],
},

═══════════════════════════
PAPER A PROCESAR
═══════════════════════════
[PEGA AQUÍ EL TEXTO DEL PAPER: abstract, introducción, secciones de resultados principales,
y conclusiones. Si el paper es largo, prioriza: abstract + tabla de resultados + conclusiones.
Mínimo 500 palabras para que la IA tenga suficiente contexto.]

"""

# ═══════════════════════════════════════════════════════════════════════════════
# INSTRUCCIONES ADICIONALES PARA CASOS ESPECIALES
# ═══════════════════════════════════════════════════════════════════════════════

PROMPT_ADDENDUM_GRAFICO = """
INSTRUCCIÓN ADICIONAL — CARTAS CON GRÁFICO:
Para cartas con graph_type, el front debe ser una pregunta que REQUIERA interpretar un gráfico.
Ejemplos de buenas preguntas gráficas:
- "Observa la curva precio-yield de un bono callable vs. bullet. ¿Qué diferencia notable tiene la curva del callable y qué explica esa diferencia?"
- "El gráfico muestra la J-curve típica de un fondo PE. Identifica en qué fase está un fondo que lleva 3 años activo y tiene NAV por debajo de capital invertido."
- "La curva de yields se invierte como muestra el gráfico. ¿Qué implica esto para una posición long duration según la teoría de expectativas puras?"
El back debe guiar cómo LEER e INTERPRETAR el gráfico, no solo describir el concepto.
"""

PROMPT_ADDENDUM_IDEAS = """
INSTRUCCIÓN ADICIONAL — CARTA DE IDEAS DE INVERSIÓN:
Incluye al menos 1 carta del tipo "investment implication" que cierre el loop entre la teoría
del paper y una decisión de portafolio concreta. Formato sugerido para el front:
"¿Cómo aplicarías el hallazgo principal de [paper] para mejorar el posicionamiento en [contexto actual]?"
Back: debe incluir: (1) la señal/variable a monitorear, (2) el asset class afectado,
(3) la posición/tilt a implementar, (4) el riesgo de implementación.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# EJEMPLO DE CARTA BIEN CONSTRUIDA (para que la IA entienda el estándar)
# ═══════════════════════════════════════════════════════════════════════════════

EXAMPLE_CARD = """
EJEMPLO DE CARTA DE ALTA CALIDAD:
{
    "id": "aa_rp_001",
    "domain": "Asset Allocation",
    "topic": "Risk Parity — Contribución al Riesgo",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Qian (2005) — Panagora Asset Management White Paper",
    "front": "En un portafolio 60/40, ¿qué porcentaje del riesgo total aporta la renta variable asumiendo vol equity=15% y vol bonos=5% con correlación cero?",
    "back": "Aproximadamente el 95% del riesgo total proviene de equity. Var_p = (0.6×0.15)²+(0.4×0.05)² = 0.0081+0.0004 = 0.0085. Contribución equity = 0.0081/0.0085 ≈ 95%. Esto demuestra que un 60/40 es esencialmente un portafolio 100% equity en términos de riesgo — la diversificación por peso de capital es ilusoria.",
    "latex": r"RC_{equity} = \frac{w^2_{eq}\sigma^2_{eq}}{w^2_{eq}\sigma^2_{eq} + w^2_b\sigma^2_b}",
    "numerical_problem": {
        "question": "Mismo portafolio 60/40 con vol equity=15%, vol bonos=5%, correlación=0. ¿Qué pesos daría un portafolio risk parity (igual contribución de riesgo)?",
        "steps": [
            "Para igual RC: w_eq×σ_eq = w_b×σ_b (con correlación 0)",
            "w_eq×0.15 = w_b×0.05 → w_eq/w_b = 0.05/0.15 = 1/3",
            "w_eq + w_b = 1 → w_eq = 25%, w_b = 75%",
            "Verificación: 0.25×0.15 = 0.0375; 0.75×0.05 = 0.0375 ✓"
        ],
        "answer": "25% equity, 75% bonos (sin apalancamiento)",
        "bus_hint": "RC iguales → w×vol iguales → w_eq×15 = w_b×5 → ratio 1:3 → 25%/75%"
    },
    "true_false": {
        "statement": "Risk Parity siempre requiere apalancamiento para alcanzar retornos comparables al 60/40.",
        "answer": False,
        "explanation": "Risk Parity sin apalancamiento puede tener menor retorno absoluto que 60/40 en mercados alcistas de equity, pero el apalancamiento es opcional. Bridgewater All Weather usa apalancamiento para targetear un nivel de volatilidad específico, pero no es inherente al concepto."
    },
    "intuition": "Imagina que el portafolio 60/40 es como un equipo de fútbol donde 11 jugadores cargan el balón pero 10 de ellos lo llevan todo el partido. Risk Parity redistribuye la carga para que todos contribuyan igual — aunque para que el equipo sea igual de rápido (mismo retorno), algunos jugadores necesitan correr más (apalancamiento).",
    "connections": ["Black-Litterman", "Máximo Diversification (Choueifaty)", "Minimum Variance Portfolio"],
},
"""
