"""
INVEST MEMORIA — Master Cards
==============================
Cartas curadas con estructura rica:
  front, back, latex, mcq, true_false, fill_blank,
  graph_type, numerical_problem, intuition, derivation,
  code_python, connections, source, difficulty, mode_tags
"""

INVEST_CARDS = [

# ════════════════════════════════════════════════════════════════
# EQUITY INVESTING
# ════════════════════════════════════════════════════════════════

{
    "id": "eq_001",
    "domain": "Equity Investing",
    "topic": "Factor Investing — Momentum",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Jegadeesh & Titman (1993) — JoF; AQR Capital",
    "front": "¿Qué es el momentum cross-sectional en acciones y cuál es su horizonte típico de formación y holding?",
    "back": "Estrategia que compra acciones con mejor retorno relativo en los últimos 12M (excluyendo el último mes) y vende las peores. Horizonte de formación: 2–12 meses. Holding típico: 1–6 meses. El mes más reciente se excluye por reversión de corto plazo (microestructura).",
    "latex": r"r_{t+1} \sim \text{rank}(r_{t-12,t-1})",
    "intuition": "El momentum captura la tendencia a que 'los ganadores siguen ganando' por razones conductuales (subajuste de información) y fundamentales (aceleración de earnings). Se desvanece en 12–36 meses (reversión de largo plazo).",
    "connections": ["Value Factor", "Low Volatility", "Frog-in-pan hypothesis (Da et al.)"],
    "mcq": {
        "question": "Jegadeesh & Titman documentan que una estrategia de momentum con formación 12M y holding 3M genera un alpha anual aproximado de:",
        "options": ["A) 1–2%", "B) 3–4%", "C) 8–12%", "D) 18–20%"],
        "answer": "C",
        "explanation": "El paper original documenta ~1% mensual (≈12% anual) antes de costos de transacción para carteras decil top-bottom en NYSE/AMEX."
    },
    "true_false": {
        "statement": "En la estrategia momentum, el mes más reciente se incluye porque es donde mayor señal de continuación existe.",
        "answer": False,
        "explanation": "Se excluye el mes más reciente (t-1 a t) porque domina la reversión de corto plazo por microestructura de mercado (bid-ask bounce, efectos de liquidez)."
    },
    "fill_blank": {
        "template": "El momentum cross-sectional excluye el mes más reciente para evitar la _______ de corto plazo.",
        "answers": ["reversión", "reversal", "reversion"]
    },
    "graph_type": "momentum_decile_returns",
},

{
    "id": "eq_002",
    "domain": "Equity Investing",
    "topic": "Valoración — DDM Gordon Growth",
    "difficulty": "Foundational",
    "mode_tags": ["bus", "home"],
    "source": "Gordon & Shapiro (1956); Damodaran (Valuation textbook)",
    "front": "Fórmula del modelo de Gordon Growth y sus supuestos clave.",
    "back": "P₀ = D₁ / (r − g). Supuestos: dividendos crecen a tasa constante g perpetuamente; r > g; empresa en estado estacionario. D₁ = dividendo próximo periodo, r = tasa de descuento (ke), g = tasa de crecimiento sostenible.",
    "latex": r"P_0 = \frac{D_1}{r - g} = \frac{D_0(1+g)}{k_e - g}",
    "intuition": "Es el valor presente de una perpetuidad creciente. El spread (r-g) es el 'precio del crecimiento': cuanto más se acercan r y g, el valor explota — pequeños cambios en g tienen impacto exponencial.",
    "numerical_problem": {
        "question": "Una acción pagó un dividendo de $2.00 el año pasado. Se espera que crezca al 5% perpetuamente. El costo de equity es 10%. ¿Cuál es el precio justo?",
        "steps": ["D₁ = D₀ × (1+g) = 2.00 × 1.05 = $2.10", "P₀ = D₁ / (r-g) = 2.10 / (0.10 - 0.05)", "P₀ = 2.10 / 0.05 = $42.00"],
        "answer": "$42.00",
        "bus_hint": "D₁ = 2×1.05 = 2.1 → 2.1/(0.10-0.05) = 2.1/0.05 = 42"
    },
    "mcq": {
        "question": "Si la tasa de crecimiento g sube de 4% a 5% (y r=10%), ¿cuál es el efecto sobre P₀?",
        "options": ["A) Sube ~16.7%", "B) Sube ~33.3%", "C) Sube ~66.7%", "D) Sube ~100%"],
        "answer": "B",
        "explanation": "Con g=4%: P=D₁/0.06. Con g=5%: P=D₁/0.05. Ratio = 0.06/0.05 = 1.20 → sube 20%... pero si D₁ también ajusta (D₀×1.05 vs D₀×1.04), el efecto combinado es mayor. En la versión pura (D₁ fijo): sube 33.3%."
    },
    "fill_blank": {
        "template": "En el modelo Gordon Growth, el denominador (r − g) representa el _______ entre la tasa requerida y el crecimiento perpetuo.",
        "answers": ["spread", "diferencial", "diferencia"]
    },
    "graph_type": "gordon_sensitivity",
},

{
    "id": "eq_003",
    "domain": "Equity Investing",
    "topic": "Factor Investing — Value",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Fama & French (1992) JoF; Asness, Moskowitz & Pedersen (2013)",
    "front": "¿Por qué el factor Value (HML) genera retornos positivos históricos? Resume el debate riesgo vs. anomalía conductual.",
    "back": "Perspectiva de riesgo (Fama-French): value stocks son empresas en distress con mayor riesgo sistemático no capturado por beta; la prima compensa riesgo real. Perspectiva conductual (Lakonishok et al.): extrapolación excesiva de crecimiento pasado lleva a sobrevaluar growth y subvaluar value; la corrección genera alfa. Debate no resuelto.",
    "intuition": "HML = High minus Low (book-to-market). Compra baratas (alto B/M), vende caras (bajo B/M). En crisis, value cae más que growth — consistente con la historia de riesgo. Pero la prima persiste incluso tras ajustar por riesgo macroeconómico.",
    "fill_blank": {
        "template": "HML significa _______ minus Low en términos de ratio book-to-market, y es el factor value del modelo Fama-French.",
        "answers": ["High", "high"]
    },
    "true_false": {
        "statement": "Fama & French argumentan que la prima value es evidencia de ineficiencia de mercado causada por sesgos conductuales de los inversores.",
        "answer": False,
        "explanation": "Fama-French sostienen que la prima value es compensación por riesgo sistemático real (distress risk). La explicación conductual es de Lakonishok, Shleifer & Vishny (1994) y otros académicos conductuales."
    },
    "graph_type": "hml_cumulative",
},

{
    "id": "eq_004",
    "domain": "Equity Investing",
    "topic": "Earnings Quality — Accruals",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "Sloan (1996) TAR — 'Do Stock Prices Fully Reflect Information in Accruals and Cash Flows?'",
    "front": "¿Qué es la anomalía de accruals de Sloan (1996) y cómo se construye la señal?",
    "back": "Empresas con altos accruals contables tienen menores retornos futuros. Señal: Accruals = (ΔActivo Corriente − ΔCaja) − (ΔPasivo Corriente − ΔDeuda CP) − Depreciación, escalado por activos totales. Estrategia: short high-accruals, long low-accruals (cash earners). Alpha ≈ 10% anual en el paper original.",
    "latex": r"\text{Accruals} = \frac{\Delta CA - \Delta Cash - \Delta CL + \Delta STD - Dep}{TA}",
    "fill_blank": {
        "template": "Según Sloan (1996), las empresas con accruals altos tienen _______ retornos futuros porque el mercado sobreestima la persistencia de las ganancias.",
        "answers": ["menores", "bajos", "inferiores", "lower"]
    },
    "graph_type": "accruals_returns",
},


# ════════════════════════════════════════════════════════════════
# FIXED INCOME
# ════════════════════════════════════════════════════════════════

{
    "id": "fi_001",
    "domain": "Fixed Income",
    "topic": "Duration y Convexidad",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Fabozzi — Fixed Income Mathematics; CFA Institute",
    "front": "¿Qué mide la Duration Modificada y cuál es la aproximación de primer orden para el cambio de precio de un bono?",
    "back": "Duration Modificada (MD) mide la sensibilidad precio-rendimiento: ante un alza de 1% en yield, el precio cae ~MD%. Aproximación: ΔP/P ≈ −MD × Δy. Para incluir curvatura se agrega convexidad: ΔP/P ≈ −MD×Δy + ½×C×(Δy)².",
    "latex": r"\frac{\Delta P}{P} \approx -MD \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2",
    "numerical_problem": {
        "question": "Un bono tiene MD = 7.5 y convexidad = 80. Si el yield sube 50 bps (0.50%), ¿cuál es el cambio % aproximado en precio?",
        "steps": [
            "Efecto duration: −7.5 × 0.005 = −0.0375 = −3.75%",
            "Efecto convexidad: +½ × 80 × (0.005)² = +½ × 80 × 0.000025 = +0.001 = +0.10%",
            "Total: −3.75% + 0.10% = −3.65%"
        ],
        "answer": "−3.65%",
        "bus_hint": "−MD×Δy = −7.5×0.005 = −3.75% | convex = +0.5×80×0.005² ≈ +0.10% | Total ≈ −3.65%"
    },
    "mcq": {
        "question": "Un bono con mayor convexidad, ante una caída de yields, generará un retorno:",
        "options": ["A) Igual a uno de menor convexidad", "B) Menor por el costo de la convexidad", "C) Mayor porque la ganancia de precio es superior", "D) Imposible de determinar sin saber el cupón"],
        "answer": "C",
        "explanation": "La convexidad es siempre positiva para bonos bullet: genera ganancia adicional cuando yields caen y amortigua pérdidas cuando suben. Más convexidad = mejor perfil asimétrico."
    },
    "true_false": {
        "statement": "La duration modificada sobreestima la caída de precio de un bono cuando los yields suben significativamente, porque ignora la convexidad positiva.",
        "answer": True,
        "explanation": "La aproximación lineal (duration) sobreestima las caídas de precio ante movimientos grandes. La convexidad positiva hace que la curva precio-yield sea menos pronunciada de lo que predice la línea tangente."
    },
    "fill_blank": {
        "template": "La relación entre Duration de Macaulay y Duration Modificada es: MD = D_Mac / (1 + _____), donde el denominador es la tasa periódica.",
        "answers": ["y/m", "yield/m", "y", "yield", "r"]
    },
    "graph_type": "price_yield_convexity",
},

{
    "id": "fi_002",
    "domain": "Fixed Income",
    "topic": "Yield Curve — Teorías",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Cochrane & Piazzesi (2005) AER; CFA Level III Fixed Income",
    "front": "Resume las 3 principales teorías de la estructura temporal de tasas y qué predicen sobre el término premium.",
    "back": "1) Expectativas Puras: forward rates = expectativas de tasas futuras, término premium = 0. 2) Preferencia por Liquidez (Hicks): inversores prefieren corto plazo → premia positiva en largo → curva normalmente positiva incluso con expectativas planas. 3) Segmentación de Mercados: oferta/demanda independiente en cada segmento, sin arbitraje entre vencimientos. La evidencia empírica favorece una combinación de expectativas + término premium positivo.",
    "mcq": {
        "question": "Según la teoría de Preferencia por Liquidez, una curva de yields invertida implica:",
        "options": [
            "A) Tasas futuras esperadas bajas + término premium negativo",
            "B) Tasas futuras esperadas tan bajas que dominan el término premium positivo",
            "C) Segmentación extrema en el mercado de corto plazo",
            "D) Expectativas de deflación permanente"
        ],
        "answer": "B",
        "explanation": "Bajo preferencia por liquidez, el término premium es positivo. Una curva invertida implica que las expectativas de bajas tasas futuras son tan fuertes que superan ese término premium, resultando en yields de largo plazo menores que los de corto."
    },
    "fill_blank": {
        "template": "La teoría de _______ de Hicks postula que los inversores requieren una compensación adicional por mantener bonos de largo plazo, generando un término premium positivo.",
        "answers": ["preferencia por liquidez", "Preferencia por Liquidez", "liquidity preference"]
    },
    "graph_type": "yield_curve_shapes",
},

{
    "id": "fi_003",
    "domain": "Fixed Income",
    "topic": "Spreads de Crédito — OAS",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "Fabozzi — Handbook of Fixed Income; Bloomberg OAS documentation",
    "front": "¿Qué es el Option-Adjusted Spread (OAS) y por qué es superior al Z-spread para bonos callable?",
    "back": "OAS = spread constante sobre la curva libre de riesgo que iguala el precio de mercado al valor presente de flujos esperados, modelando explícitamente las opciones embebidas. Z-spread ignora la optionalidad (callable, putable). OAS = Z-spread − Valor de la Opción (en bps). Para callable: OAS < Z-spread porque el emisor tiene el beneficio de recomprar.",
    "latex": r"OAS = Z\text{-spread} - \text{Option Value (bps)}",
    "fill_blank": {
        "template": "Para un bono callable, el OAS es _______ que el Z-spread porque el spread debe descontarse en el valor de la opción de compra del emisor.",
        "answers": ["menor", "más bajo", "inferior", "lower", "smaller"]
    },
    "true_false": {
        "statement": "Un OAS más alto en dos bonos similares siempre indica mayor riesgo de crédito.",
        "answer": False,
        "explanation": "El OAS puede ser alto por riesgo de crédito, riesgo de liquidez, o riesgo de modelo (errores en la modelación de opciones). Hay que descomponer el OAS en sus componentes para atribuirlo correctamente."
    },
},


# ════════════════════════════════════════════════════════════════
# ALTERNATIVES
# ════════════════════════════════════════════════════════════════

{
    "id": "alt_001",
    "domain": "Alternatives",
    "topic": "Private Equity — IRR vs MOIC",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Kaplan & Schoar (2005) JoF; Preqin PE benchmarks",
    "front": "¿Por qué el IRR puede ser una métrica engañosa en PE y qué ventaja tiene el MOIC?",
    "back": "IRR asume reinversión de flujos intermedios a la misma tasa — sesgado al alza en fondos con retornos tempranos. Puede ser manipulado con líneas de crédito (subscription facilities) que retrasan llamadas de capital. MOIC (Multiple on Invested Capital) = Valor Distribuido Total / Capital Invertido. MOIC ignora el tiempo, pero muestra la magnitud real de creación de valor. La métrica ideal combina ambas (e.g., DPI + IRR).",
    "latex": r"MOIC = \frac{DPI + RVPI}{PIC} = \frac{\text{Distribuido} + \text{NAV Residual}}{\text{Capital Llamado}}",
    "mcq": {
        "question": "Un fondo PE invierte $100M y retorna $50M al año 1 y $120M al año 5. MOIC = 1.7x. El IRR aproximado es:",
        "options": ["A) 10%", "B) 14%", "C) 20%", "D) 17%"],
        "answer": "C",
        "explanation": "El retorno temprano de $50M en año 1 eleva el IRR significativamente más de lo que el MOIC sugiere. IRR ≈ 20% (la solución a NPV=0 con esos flujos). Esto ilustra el sesgo del IRR por reinversión de flujos tempranos."
    },
    "fill_blank": {
        "template": "Las subscription facilities de los fondos PE distorsionan el IRR porque _______ el periodo de medición del retorno al retrasar las llamadas de capital.",
        "answers": ["acortan", "reducen", "comprimen", "shortens"]
    },
    "true_false": {
        "statement": "Un MOIC de 2.0x siempre implica mejor performance que un fondo con MOIC de 1.8x.",
        "answer": False,
        "explanation": "Un MOIC de 2.0x en 10 años (IRR ≈ 7%) puede ser peor que un MOIC de 1.8x en 3 años (IRR ≈ 22%). El MOIC ignora completamente el tiempo, por eso se debe usar junto con el IRR y el DPI."
    },
    "graph_type": "pe_cashflow_j_curve",
},

{
    "id": "alt_002",
    "domain": "Alternatives",
    "topic": "Hedge Funds — Replication de Estrategias",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "Hasanhodzic & Lo (2007) — 'Can Hedge-Fund Returns Be Replicated?'",
    "front": "¿Qué metodología propone Hasanhodzic & Lo para replicar retornos de hedge funds y cuáles son sus limitaciones?",
    "back": "Regresión rolling de retornos del HF contra 6 factores: S&P500, spread crédito, USD index, VIX change, gold, y cambio en pendiente de curva. Los coeficientes se usan para construir un clone sintético. Limitación: captura el beta de factores lineales pero no el alfa verdadero, estrategias no-lineales (opcionalidad), o timing dinámico. Clone cuesta menos en fees pero pierde el upside del alfa.",
    "fill_blank": {
        "template": "Los clones de hedge funds capturan la exposición a factores _______ pero fallan en replicar estrategias con perfiles de retorno no-lineales u opcionalidad.",
        "answers": ["lineales", "sistemáticos", "linear", "systematic"]
    },
},

{
    "id": "alt_003",
    "domain": "Alternatives",
    "topic": "Real Assets — Infraestructura",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "EDHEC Infrastructure Institute; Blanc-Brude et al.",
    "front": "¿Cuáles son las 3 características que hacen de la infraestructura un activo alternativo atractivo para portafolios institucionales?",
    "back": "1) Flujos de caja predecibles y regulados (concesiones, contratos take-or-pay) con protección inflacionaria vía indexación tarifaria. 2) Baja correlación con acciones y bonos en mercados secundarios (especialmente infraestructura no listada). 3) Duration larga (30-99 años) que calza con pasivos de largo plazo de pensiones y aseguradoras — atractivo para liability-matching.",
    "mcq": {
        "question": "¿Cuál tipo de infraestructura tiene menor correlación con equity público y mayor previsibilidad de flujos?",
        "options": [
            "A) Aeropuertos en mercados emergentes",
            "B) Autopistas de peaje con tráfico variable",
            "C) Redes de transmisión eléctrica reguladas",
            "D) Puertos marítimos de carga general"
        ],
        "answer": "C",
        "explanation": "La infraestructura regulada (redes eléctricas, gasoductos) tiene retornos determinados por regulación, prácticamente independientes del ciclo económico. Aeropuertos y puertos tienen alta correlación con el PIB y el comercio."
    },
},


# ════════════════════════════════════════════════════════════════
# THEMATIC INVESTING
# ════════════════════════════════════════════════════════════════

{
    "id": "th_001",
    "domain": "Thematic Investing",
    "topic": "Framework de Evaluación Temática",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "BlackRock Investment Institute; WEF Global Risks Report",
    "front": "¿Cuáles son los 4 criterios para evaluar si un tema de inversión es genuino vs. una narrativa de mercado?",
    "back": "1) Magnitud: ¿el impacto económico es suficientemente grande para mover mercados de capitales? (TAM, capex requerido). 2) Durabilidad: ¿el driver es secular (demografía, regulación, tecnología) o cíclico? 3) Monetización: ¿hay empresas públicas con exposición pura y no diluida? 4) Valuación: ¿la narrativa ya está en precio? (tema caro = menor retorno prospectivo). Sin los 4, el tema es solo moda.",
    "mcq": {
        "question": "El principal riesgo de implementar un tema de inversión popular (e.g. IA, clean energy) con ETFs temáticos es:",
        "options": [
            "A) Falta de diversificación por concentración sectorial",
            "B) Adquirir exposición a valuaciones ya infladas por la narrativa",
            "C) Riesgo regulatorio de la SEC sobre ETFs temáticos",
            "D) Baja liquidez de los ETFs temáticos en mercados secundarios"
        ],
        "answer": "B",
        "explanation": "El mayor riesgo es 'comprar el hype': cuando el tema es ampliamente conocido y popular, el precio de las acciones ya incorpora expectativas muy optimistas. Los retornos prospectivos se comprimen o se vuelven negativos aunque el tema se materialice según lo esperado."
    },
    "fill_blank": {
        "template": "El concepto de 'priced-in' implica que incluso si un tema temático se materializa según las expectativas, el retorno para el inversor puede ser _______ si el precio ya incorporaba esas expectativas.",
        "answers": ["cero", "negativo", "bajo", "nulo", "zero", "negative"]
    },
},

{
    "id": "th_002",
    "domain": "Thematic Investing",
    "topic": "Inteligencia Artificial — Cadena de Valor",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Goldman Sachs AI Research (2023); Sequoia 'AI's $600B Question'",
    "front": "¿Cuáles son las 3 capas de la cadena de valor de IA y en cuál se espera mayor captura de valor a largo plazo?",
    "back": "Capa 1 - Infraestructura: semiconductores (NVIDIA), cloud (AWS, Azure, GCP), energía. Capa 2 - Modelos: LLMs/foundational models (OpenAI, Anthropic, Google). Capa 3 - Aplicaciones: software vertical, herramientas de productividad. La mayor captura de valor a largo plazo probablemente migre a aplicaciones que tengan ventaja en datos propietarios y switching costs altos — pero a corto plazo, semiconductores han capturado el grueso (NVIDIA 2023-24).",
    "true_false": {
        "statement": "Las empresas de modelos fundacionales (LLMs) tienen ventaja competitiva estructural alta porque los pesos de los modelos son difíciles de replicar.",
        "answer": False,
        "explanation": "El riesgo es la commoditización de modelos: open-source (LLaMA, Mistral) reducen las barreras. La ventaja competitiva real requiere datos propietarios, distribución o integración vertical. Los pesos por sí solos no son moat suficiente."
    },
    "graph_type": "ai_value_chain",
},


# ════════════════════════════════════════════════════════════════
# ESG
# ════════════════════════════════════════════════════════════════

{
    "id": "esg_001",
    "domain": "ESG",
    "topic": "ESG Integration vs. Screening",
    "difficulty": "Foundational",
    "mode_tags": ["bus", "home"],
    "source": "PRI — Principles for Responsible Investment; Friede et al. (2015) meta-análisis",
    "front": "Distingue entre las 4 principales estrategias ESG: Exclusión, Best-in-Class, Integración ESG, e Impact Investing.",
    "back": "Exclusión (Screening negativo): elimina sectores/empresas por criterios normativos (tabaco, armas). Best-in-Class: selecciona líderes ESG dentro de cada sector — mantiene exposición sectorial. Integración ESG: incorpora factores E, S, G como inputs adicionales en el análisis financiero sin excluir mandatoriamente. Impact Investing: invierte con intención de generar impacto medible + retorno financiero (usualmente privado, con teoria del cambio explícita).",
    "mcq": {
        "question": "Un fondo que excluye petróleo pero sobrepondera a las mejores empresas de oil & gas en criterios ambientales dentro de ese universo reducido, está aplicando:",
        "options": [
            "A) Solo exclusión negativa",
            "B) Best-in-class dentro de un universo excluido (inconsistente)",
            "C) Integración ESG pura",
            "D) Exclusión negativa + best-in-class combinados"
        ],
        "answer": "D",
        "explanation": "Se puede combinar: primero se aplica screening negativo (excluye las peores empresas del sector) y luego best-in-class selecciona las mejores del universo resultante. Es una estrategia híbrida común en fondos ESG europeos."
    },
    "fill_blank": {
        "template": "La estrategia _______ selecciona a los mejores performers ESG dentro de cada sector, manteniendo así la neutralidad sectorial del portafolio.",
        "answers": ["best-in-class", "Best-in-Class", "best in class"]
    },
},

{
    "id": "esg_002",
    "domain": "ESG",
    "topic": "Materialidad ESG y Retornos",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "Khan, Serafeim & Yoon (2016) TAR — 'Corporate Sustainability'; SASB Materiality Map",
    "front": "¿Qué encuentra Khan, Serafeim & Yoon (2016) sobre la relación entre materialidad ESG y retornos de acciones?",
    "back": "Solo las issues ESG materiales (definidas por SASB según la industria) predicen retornos positivos. Empresas con alta performance en issues materiales para su industria outperforman; alta performance en issues inmateriales no añade valor (y puede destruirlo por asignación de recursos). La clave es la especificidad sectorial: lo que es material varía. Esto valida la integración selectiva ESG vs. el scoring genérico.",
    "fill_blank": {
        "template": "Khan et al. (2016) encuentra que solo el desempeño ESG en temas _______ para la industria predice retornos positivos, mientras que los temas inmateriales no añaden valor.",
        "answers": ["materiales", "material", "relevantes"]
    },
},

{
    "id": "esg_003",
    "domain": "ESG",
    "topic": "Carbon Footprint — Métricas Portfolio",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "TCFD Recommendations; MSCI ESG Research",
    "front": "¿Cuál es la diferencia entre Scope 1, Scope 2 y Scope 3 de emisiones de carbono? ¿Por qué Scope 3 es el más relevante para inversores?",
    "back": "Scope 1: emisiones directas del operador (combustión en plantas propias). Scope 2: emisiones indirectas por electricidad comprada. Scope 3: emisiones en la cadena de valor (proveedores upstream + uso del producto downstream). Scope 3 es 70-90% del total en la mayoría de sectores, pero también el más difícil de medir y auditar. Para inversores: Scope 3 captura el riesgo de transición real (e.g. automóviles: emissions del uso de vehículos son Scope 3 del fabricante).",
    "mcq": {
        "question": "Para una empresa de petróleo, las emisiones producidas por los consumidores al quemar su producto corresponden a:",
        "options": ["A) Scope 1 del productor", "B) Scope 2 del productor", "C) Scope 3 del productor", "D) Scope 1 del consumidor únicamente"],
        "answer": "C",
        "explanation": "Las emisiones downstream por uso del producto vendido son Scope 3 del productor. Son también Scope 1 del consumidor. El doble conteo es un problema conocido en contabilidad de carbono de portfolios."
    },
    "true_false": {
        "statement": "Un portafolio de acciones puede tener huella de carbono neta cero simplemente comprando RECs (Renewable Energy Certificates) para sus posiciones.",
        "answer": False,
        "explanation": "Los RECs solo abordan el Scope 2 de las empresas del portafolio. No eliminan Scope 1 ni Scope 3. Además, la 'adicionalidad' de muchos RECs es cuestionable. Net-zero real requiere reducción de emisiones absolutas, no solo compensaciones."
    },
},


# ════════════════════════════════════════════════════════════════
# ASSET ALLOCATION
# ════════════════════════════════════════════════════════════════

{
    "id": "aa_001",
    "domain": "Asset Allocation",
    "topic": "Frontera Eficiente — Markowitz",
    "difficulty": "Foundational",
    "mode_tags": ["bus", "home"],
    "source": "Markowitz (1952) JoF; Black & Litterman (1992)",
    "front": "¿Cuáles son las principales críticas al modelo de Markowitz MVO y cómo las aborda Black-Litterman?",
    "back": "Críticas MVO: 1) Extrema sensibilidad a inputs (pequeños cambios en retornos esperados → portafolios radicalmente diferentes). 2) Concentración excesiva (corner solutions). 3) Retornos esperados difíciles de estimar. Black-Litterman: parte del portafolio de equilibrio (CAPM implícito) como prior, y mezcla bayesianamente con las views del gestor. Resultado: portafolios más estables, diversificados e intuitivos.",
    "numerical_problem": {
        "question": "Un portafolio tiene σ_A=15%, σ_B=10%, ρ_AB=0.2, w_A=60%, w_B=40%. ¿Cuál es la volatilidad del portafolio?",
        "steps": [
            "σ_p² = wA²×σA² + wB²×σB² + 2×wA×wB×ρ×σA×σB",
            "= (0.6)²×(0.15)² + (0.4)²×(0.10)² + 2×0.6×0.4×0.2×0.15×0.10",
            "= 0.36×0.0225 + 0.16×0.01 + 2×0.6×0.4×0.2×0.015",
            "= 0.0081 + 0.0016 + 0.00144 = 0.01114",
            "σ_p = √0.01114 ≈ 10.55%"
        ],
        "answer": "≈10.55%",
        "bus_hint": "σ²=0.36×0.0225+0.16×0.01+2×0.24×0.2×0.015 = 0.0081+0.0016+0.00144 = 0.01114 → σ≈10.6%"
    },
    "mcq": {
        "question": "¿Cuál es la principal ventaja de Black-Litterman sobre MVO clásico para un portafolio multi-activo?",
        "options": [
            "A) Maximiza el Sharpe ratio por construcción",
            "B) Genera portafolios más estables ante pequeños cambios en los inputs",
            "C) Elimina completamente el riesgo de estimación",
            "D) No requiere una matriz de covarianzas"
        ],
        "answer": "B",
        "explanation": "BL usa el portafolio de equilibrio como prior bayesiano, lo que amortigua el efecto de errores de estimación en retornos esperados. El portafolio resultante es más estable e intuitivo, sin concentraciones extremas."
    },
    "fill_blank": {
        "template": "Black-Litterman parte del portafolio de _______ de mercado como prior y lo combina bayesianamente con las views del gestor.",
        "answers": ["equilibrio", "mercado", "CAPM", "market portfolio"]
    },
    "graph_type": "efficient_frontier_bl",
},

{
    "id": "aa_002",
    "domain": "Asset Allocation",
    "topic": "Risk Parity",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Qian (2005) — 'Risk Parity Portfolios'; Bridgewater All Weather",
    "front": "¿Cuál es el principio de Risk Parity y en qué difiere de la asignación por peso de capital (60/40)?",
    "back": "Risk Parity asigna igual contribución al riesgo (no igual capital) a cada clase de activo. En un portafolio 60/40, las acciones (mayor vol) contribuyen ~90% del riesgo total — no hay diversificación real. Risk Parity: sobrepesa bonos (menor vol) apalancados para igualar contribuciones. Contribución de riesgo: RC_i = w_i × (∂σ_p/∂w_i) = w_i × β_i × σ_p.",
    "latex": r"RC_i = w_i \cdot \frac{(\Sigma w)_i}{\sigma_p}; \quad \sum_i RC_i = \sigma_p",
    "true_false": {
        "statement": "En un portafolio 60% equity / 40% bonos, la contribución al riesgo de equity y bonos es aproximadamente 60%/40%.",
        "answer": False,
        "explanation": "Dada la mayor volatilidad del equity (típicamente 3-4x la de bonos), la contribución al riesgo de equity en un 60/40 es cercana al 85-95% del riesgo total. El 40% en bonos contribuye marginalmente al riesgo del portafolio."
    },
    "numerical_problem": {
        "question": "Un portafolio 60/40 tiene σ_equity=15%, σ_bonds=5%, correlación=0. ¿Qué % del riesgo total aporta equity?",
        "steps": [
            "Var_p = (0.6×0.15)² + (0.4×0.05)² = 0.0081 + 0.0004 = 0.0085",
            "σ_p = √0.0085 ≈ 9.22%",
            "RC_equity ≈ 0.6²×0.15² / 0.0085 = 0.0081/0.0085 ≈ 95.3% del riesgo"
        ],
        "answer": "≈95% del riesgo total",
        "bus_hint": "Var equity = (0.6×0.15)²=0.0081 | Var bonds=(0.4×0.05)²=0.0004 | equity/total = 0.0081/0.0085 ≈ 95%"
    },
    "graph_type": "risk_parity_contributions",
},

{
    "id": "aa_003",
    "domain": "Asset Allocation",
    "topic": "Rebalancing — Momentum vs. Contrarian",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Perold & Sharpe (1988) FAJ; Asness et al.",
    "front": "¿Cuándo el rebalanceo sistemático destruye valor y cuándo lo crea, en función del régimen de mercado?",
    "back": "Rebalanceo contrario (vender ganadores, comprar perdedores) destruye valor en mercados con momentum fuerte (tendencias persistentes). Crea valor en mercados con reversión a la media (range-bound). Regla práctica: en activos con alto autocovarianza positiva (momentum) → rebalanceo menos frecuente o por umbral ancho. En activos con baja autocovarianza → rebalanceo frecuente captura 'rebalancing bonus'. No existe una frecuencia óptima universal.",
    "mcq": {
        "question": "En un mercado con fuerte momentum en acciones, ¿qué estrategia de rebalanceo es más adecuada?",
        "options": [
            "A) Rebalanceo mensual a pesos fijos para aprovechar la reversión",
            "B) Rebalanceo por umbral amplio o no rebalancear para dejar correr el momentum",
            "C) Rebalanceo diario para capturar máximo rebalancing bonus",
            "D) Eliminar el proceso de rebalanceo completamente"
        ],
        "answer": "B",
        "explanation": "Con momentum, vender activos que suben (rebalanceo contrario) va contra la tendencia y destruye alfa. Un umbral amplio (e.g. ±10% del peso objetivo) permite 'dejar correr' la tendencia mientras mantiene un nivel de diversificación mínimo."
    },
},


# ════════════════════════════════════════════════════════════════
# TRADING STRATEGY
# ════════════════════════════════════════════════════════════════

{
    "id": "ts_001",
    "domain": "Trading Strategy",
    "topic": "Market Microstructure — Bid-Ask Spread",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Glosten & Milgrom (1985) JFE; Amihud & Mendelson (1986)",
    "front": "¿Cuáles son los 3 componentes del bid-ask spread según la teoría de microestructura?",
    "back": "1) Costo de inventario: el market maker asume riesgo de precio al mantener posiciones; requiere compensación. 2) Costo de orden: costos operativos de procesar y ejecutar órdenes. 3) Selección adversa: el market maker teme negociar contra inversores informados (informed traders); el spread compensa el riesgo de perder ante traders con información privada. El componente de selección adversa es el más relevante para la eficiencia de mercado.",
    "mcq": {
        "question": "En la víspera de un earnings release, el spread bid-ask de una acción típicamente:",
        "options": [
            "A) Se reduce porque hay mayor liquidez por volumen de trading",
            "B) Se amplía porque market makers temen mayor selección adversa",
            "C) No cambia si el mercado es eficiente",
            "D) Se reduce porque los algoritmos compiten por liquidez"
        ],
        "answer": "B",
        "explanation": "Antes de anuncios de earnings, aumenta la probabilidad de que algunos traders tengan información privada (selección adversa). Los market makers amplían el spread para protegerse de potenciales pérdidas ante informed traders. El volumen puede subir pero el spread también."
    },
    "fill_blank": {
        "template": "El componente de _______ adversa del spread bid-ask compensa al market maker por el riesgo de negociar contra inversores con información privada.",
        "answers": ["selección", "selection", "información"]
    },
    "true_false": {
        "statement": "Un spread bid-ask más amplio siempre indica menor eficiencia de mercado.",
        "answer": False,
        "explanation": "Un spread amplio puede reflejar mayor incertidumbre de información (normal y eficiente en ese contexto), menor liquidez por tamaño del mercado, o mayor riesgo de inventario. No es sinónimo de ineficiencia — puede ser el precio correcto de la liquidez bajo mayor incertidumbre."
    },
},

{
    "id": "ts_002",
    "domain": "Trading Strategy",
    "topic": "Execution — VWAP y Algoritmos",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Almgren & Chriss (2001) — 'Optimal Execution of Portfolio Transactions'",
    "front": "¿Qué mide el VWAP y cuándo es una benchmark apropiada vs. inapropiada para evaluar calidad de ejecución?",
    "back": "VWAP (Volume-Weighted Average Price) = Σ(precio × volumen) / volumen total del día. Mide si ejecutaste mejor o peor que el precio promedio ponderado por volumen del mercado. Apropiado: para órdenes de tamaño moderado, trading intradía sin urgencia, benchmarking de brokers. Inapropiado: para órdenes muy grandes (tu propia ejecución mueve el VWAP), para órdenes urgentes con información (VWAP te expone al mercado), cuando el timing es crítico.",
    "mcq": {
        "question": "Un gestor debe vender una posición grande urgentemente porque recibió un mandate de redemption. ¿Cuál benchmark de ejecución es más adecuada?",
        "options": [
            "A) VWAP del día completo",
            "B) Arrival Price (precio al momento de la decisión de vender)",
            "C) TWAP del período de ejecución",
            "D) Precio de cierre del día"
        ],
        "answer": "B",
        "explanation": "El Arrival Price mide el costo de implementación desde la decisión. En situaciones urgentes con información, VWAP no es relevante. Lo que importa es cuánto se deteriora el precio desde que se decide vender hasta que se completa la ejecución (Implementation Shortfall)."
    },
    "fill_blank": {
        "template": "El Implementation Shortfall mide la diferencia entre el retorno del portafolio _______ (paper portfolio) y el retorno real ejecutado, capturando todos los costos de transacción.",
        "answers": ["teórico", "hipotético", "paper", "ideal"]
    },
    "graph_type": "vwap_execution_profile",
},

{
    "id": "ts_003",
    "domain": "Trading Strategy",
    "topic": "Statistical Arbitrage — Pairs Trading",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "Gatev, Goetzmann & Rouwenhorst (2006) RFS",
    "front": "¿Cómo se construye y ejecuta un pairs trade? ¿Cuáles son las condiciones estadísticas necesarias?",
    "back": "1) Encontrar par cointegrado: test ADF/Johansen en el spread. 2) Estimar relación de cobertura (hedge ratio) vía regresión OLS o Kalman filter. 3) Normalizar spread en z-score: z = (spread − μ) / σ. 4) Señales: long spread cuando z < −2, short cuando z > +2, cerrar en z = 0. Condiciones: cointegración estable (no correlación de corto plazo), mean-reversion verificada, liquidez suficiente en ambas legs. Riesgo principal: breakdown de cointegración (fundamental divergence).",
    "latex": r"z_t = \frac{S_t - \mu_S}{\sigma_S}; \quad S_t = P_{A,t} - \beta P_{B,t}",
    "fill_blank": {
        "template": "En pairs trading, el z-score del spread se usa como señal: se compra cuando cae por debajo de _______ y se cierra cuando vuelve a cero.",
        "answers": ["-2", "−2", "menos dos", "-1.5", "-2.0"]
    },
},


# ════════════════════════════════════════════════════════════════
# EQUITY INVESTING — van Binsbergen & Koijen (2009)
# Predictive Regressions: A Present-Value Approach
# ════════════════════════════════════════════════════════════════

{
    "id": "eq_pv_001",
    "domain": "Equity Investing",
    "topic": "Predictabilidad — Modelo de Valor Presente",
    "difficulty": "Advanced",
    "mode_tags": ["bus", "home"],
    "source": "van Binsbergen & Koijen (2009) — Stanford GSB / U. Chicago Booth; JFE",
    "front": "¿Por qué el ratio precio-dividendo (P/D) es un predictor ruidoso de retornos si se usa solo, según van Binsbergen & Koijen (2009)?",
    "back": "Porque el P/D se mueve por DOS fuentes: variación en retornos esperados (μ_t) Y variación en crecimiento esperado de dividendos (g_t). Si asumes que solo refleja retornos esperados, atribuyes todo el movimiento del P/D a μ_t cuando parte se debe a g_t — sesgando la estimación. El modelo de VB&K usa un filtro de Kalman para separar ambas fuentes latentes del P/D, generando predictores más eficientes (R² retornos: 8.2–8.9%; R² dividendos: 13.9–31.6%).",
    "latex": r"pd_t = A - B_1(\mu_t - \delta_0) + B_2(g_t - \gamma_0)",
    "intuition": "El P/D es como un termómetro que mide tanto temperatura (retornos esperados) como humedad (crecimiento esperado de dividendos) al mismo tiempo. Usarlo solo para predecir temperatura da señales ruidosas. VB&K instala dos sensores separados (filtro de Kalman) para descomponer las dos señales.",
    "mcq": {
        "question": "En el modelo de VB&K (2009), el loading del P/D sobre retornos esperados (B₁) es MAYOR cuando:",
        "options": [
            "A) La persistencia de retornos esperados (δ₁) es baja",
            "B) La persistencia de retornos esperados (δ₁) es alta, acercándose a ρ⁻¹",
            "C) La volatilidad de dividendos (σ_D) es alta",
            "D) El crecimiento esperado de dividendos (g_t) es constante"
        ],
        "answer": "B",
        "explanation": "B₁ = 1/(1−ρδ₁). Cuando δ₁ → 1/ρ (alta persistencia), el denominador → 0 y B₁ → ∞: el P/D es extremadamente sensible a retornos esperados. Intuitivamente, retornos esperados muy persistentes tienen impacto de largo plazo sobre el P/D vía valor presente."
    },
    "true_false": {
        "statement": "VB&K (2009) encuentra que el crecimiento de dividendos es más persistente que los retornos esperados en el mercado accionario agregado.",
        "answer": False,
        "explanation": "El hallazgo opuesto: los retornos esperados (μ_t) son MÁS persistentes que el crecimiento esperado de dividendos (g_t). Lo demuestran con un likelihood-ratio test. Esto es importante porque afecta el diseño de estrategias de timing: las señales de retorno son más lentas y duraderas que las señales de crecimiento de dividendos."
    },
    "fill_blank": {
        "template": "VB&K usan un _______ de Kalman para estimar las dos variables latentes (retornos esperados y crecimiento esperado de dividendos) a partir de la historia del ratio P/D y de las tasas de crecimiento de dividendos.",
        "answers": ["filtro", "filter", "Kalman filter", "filtro de Kalman"]
    },
    "numerical_problem": {
        "question": "El modelo VB&K implica pd_t = A − B₁·μ̂_t + B₂·ĝ_t, con B₁=1/(1−ρδ₁). Si ρ=0.96 y δ₁=0.90, ¿cuánto vale B₁?",
        "steps": [
            "B₁ = 1 / (1 − ρ × δ₁)",
            "= 1 / (1 − 0.96 × 0.90)",
            "= 1 / (1 − 0.864)",
            "= 1 / 0.136 ≈ 7.35"
        ],
        "answer": "B₁ ≈ 7.35",
        "bus_hint": "1−(0.96×0.90) = 1−0.864 = 0.136 → 1/0.136 ≈ 7.4"
    },
    "graph_type": "gordon_sensitivity",
    "connections": ["Campbell-Shiller (1988) Log-linearización", "Fama & French (1988) — P/D predictor", "Cochrane (2007) — Camp & Shiller VAR", "Kalman Filter — State Space Models"],
    "derivation": "Iterando la ecuación de retorno log-linealizada r_{t+1} ≈ κ + ρ·pd_{t+1} + Δd_{t+1} − pd_t hacia adelante: pd_t = A − B₁(μ_t−δ₀) + B₂(g_t−γ₀), donde B₁ = 1/(1−ρδ₁) y B₂ = 1/(1−ργ₁). Estos loadings dependen de la persistencia relativa de cada proceso AR(1).",
},

{
    "id": "eq_pv_002",
    "domain": "Equity Investing",
    "topic": "Predictabilidad — Reinversión de Dividendos",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "van Binsbergen & Koijen (2009) — Stanford GSB / U. Chicago Booth",
    "front": "¿Por qué la estrategia de reinversión de dividendos (en T-bills vs. en mercado) afecta el modelo de valor presente y qué implica esto metodológicamente?",
    "back": "Dividendos reinvertidos en mercado (D^M): la volatilidad del crecimiento es el doble (12.3% vs 6.2%) porque D^M_{t+1} = D_{t+1}·exp(r_{t+1}), incorporando la volatilidad del retorno. VB&K demuestran que si el crecimiento de dividendos en cash (D^C) sigue un AR(1), entonces el crecimiento de dividendos en mercado sigue un ARMA(1,1). Usar el modelo equivocado para la estrategia equivocada genera estimadores inconsistentes. La implicancia: hay que especificar el modelo de reinversión antes de estimar.",
    "latex": r"\Delta d^M_{t+1} = \Delta d^C_{t+1} + r_{t+1} - r_t \Rightarrow \text{ARMA}(1,1) \text{ si } g^C_t \sim AR(1)",
    "fill_blank": {
        "template": "Si el crecimiento de dividendos en cash sigue un AR(1), el crecimiento de dividendos reinvertidos en mercado sigue un proceso _______, con un componente de media móvil adicional.",
        "answers": ["ARMA(1,1)", "ARMA", "ARMA 1 1"]
    },
    "true_false": {
        "statement": "La correlación entre retornos con dividendos reinvertidos en mercado y en T-bills es prácticamente 1.0 (0.9999) — por lo que la estrategia de reinversión no afecta la serie de retornos.",
        "answer": True,
        "explanation": "Correcto y es un hallazgo clave del paper: aunque las series de RETORNOS son prácticamente idénticas (corr=0.9999), las series de CRECIMIENTO DE DIVIDENDOS son muy distintas (vol 12.3% vs 6.2%). Esto implica que la elección de reinversión afecta la especificación del modelo de dividendos pero no el modelo de retornos."
    },
    "connections": ["ARMA processes", "Campbell-Shiller log-linearization", "Dividend smoothing"],
},

{
    "id": "eq_pv_003",
    "domain": "Equity Investing",
    "topic": "Predictabilidad — Descomposición de Varianza",
    "difficulty": "Expert",
    "mode_tags": ["home"],
    "source": "van Binsbergen & Koijen (2009); Campbell (1991) — Decomposición de varianza de retornos",
    "front": "¿Qué parte de la varianza condicional de retornos del mercado accionario atribuyen VB&K a cash-flow news vs. discount-rate news, y cómo se compara con el consenso previo?",
    "back": "VB&K encuentran que cash-flow news explica 34.6–49.4% de la varianza condicional de retornos, discount-rate news explica 118.4–215.3% (más del 100% porque la covarianza es negativa y grande), y el resto (negativo) es la covarianza entre ambos. La mayor parte de la varianza del P/D viene de discount rates (consistente con Campbell 1991), pero el papel del cash-flow news es mayor de lo que estudios anteriores —que forzaban g_t constante— sugerían. Implicancia: subestimar la predictabilidad de dividendos lleva a sobreestimar el componente de discount-rate.",
    "fill_blank": {
        "template": "Cuando se fuerza al modelo a asumir que el crecimiento esperado de dividendos es _______, se sobreestima la contribución de discount-rate news a la varianza del P/D.",
        "answers": ["constante", "constant", "cero", "zero"]
    },
    "true_false": {
        "statement": "VB&K (2009) rechazan la hipótesis nula de que ni los retornos ni el crecimiento de dividendos son predecibles a niveles convencionales de significancia.",
        "answer": True,
        "explanation": "Usando un likelihood-ratio test, rechazan tanto que los retornos esperados sean constantes (δ₁=0) como que el crecimiento esperado de dividendos sea constante (γ₁=0). Ambos procesos son time-varying y persistentes, aunque con diferente grado de persistencia."
    },
    "connections": ["Campbell (1991) — VAR return decomposition", "Cochrane (2007) — Discount rates vs cash flows", "Lettau & Van Nieuwerburgh (2006)"],
},

{
    "id": "eq_pv_004",
    "domain": "Equity Investing",
    "topic": "Predictabilidad — Aplicación a Timing Táctico",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "van Binsbergen & Koijen (2009) — Implicancias para gestión activa",
    "front": "¿Cómo aplicarías el framework de VB&K (2009) para mejorar el timing táctico de equity en un portafolio multi-activo de AFP?",
    "back": "Señal de timing: monitorear la serie filtrada de μ_t (retornos esperados implícitos del P/D ajustado por g_t esperado). Cuando μ_t está por encima de su media histórica → sobreponderar equity; cuando está deprimido → subponderar. La ventaja sobre usar el P/D crudo: menor ruido (g_t explicita variación independiente del P/D). Implementación práctica: (1) estimar modelo en datos históricos, (2) actualizar el filtro mensualmente con nuevos datos de precios y dividendos, (3) traducir μ_t filtrado en un tilt sobre el benchmark de renta variable local. Limitación para AFP: horizonte de largo plazo puede dominar el timing de corto plazo.",
    "mcq": {
        "question": "Un P/D de mercado históricamente bajo puede ser señal de compra (alto μ_t) pero también puede reflejar expectativas de menor crecimiento futuro de dividendos (bajo g_t). El modelo VB&K resuelve esta ambigüedad:",
        "options": [
            "A) Asumiendo que g_t es siempre constante y atribuyendo todo al μ_t",
            "B) Usando solo el P/D actual como predictor sin historia",
            "C) Separando μ_t y g_t vía filtro de Kalman con toda la historia de P/D y Δd",
            "D) Eliminando g_t del modelo porque no es predecible"
        ],
        "answer": "C",
        "explanation": "El valor del modelo está en descomponer el P/D en sus dos fuentes: μ_t (discount rate) y g_t (cash flow). Un P/D bajo podría ser bullish (alto μ_t) o bearish (bajo g_t esperado). El filtro de Kalman asigna probabilidades a cada causa usando TODA la historia de datos — no solo el nivel actual del P/D."
    },
    "true_false": {
        "statement": "Un inversor que usa solo el P/D actual como predictor de retornos sobreestima el R² de predicción respecto al modelo de VB&K.",
        "answer": False,
        "explanation": "El modelo de VB&K MEJORA el R² de predicción (8.2–8.9% para retornos, hasta 31.6% para dividendos) al agregar toda la historia del P/D y Δd vía el filtro. El P/D actual como predictor único tiene R² mucho menor — la historia importa porque los procesos son AR(1) persistentes."
    },
    "graph_type": "gordon_sensitivity",
    "connections": ["P/D ratio como predictor", "Kalman filter — aplicaciones a señales de inversión", "Tactical Asset Allocation — señales de valoración"],
},


# ════════════════════════════════════════════════════════════════
# THEMATIC INVESTING — Somefun, Perchet, Yin & de Carvalho (2022)
# Allocating to Thematic Investments — BNP Paribas AM / FAJ
# ════════════════════════════════════════════════════════════════

{
    "id": "th_bnp_001",
    "domain": "Thematic Investing",
    "topic": "Temas como Dimensión Adicional de Riesgo",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Somefun, Perchet, Yin & de Carvalho (2022) — Financial Analysts Journal; BNP Paribas AM",
    "front": "¿En qué se diferencia una inversión temática de una apuesta sectorial o de un portafolio de acciones de crecimiento, según Somefun et al. (2022)?",
    "back": "Diferencias clave: (1) vs. sectorial: un tema puede atravesar múltiples sectores (e.g., transición energética incluye utilities, industriales, materiales). No es un bet puro en un sector. (2) vs. growth stocks: los temas aplican a empresas en cualquier etapa (incumbentes que reinventan su modelo y startups disruptores), no necesariamente high-P/E growth. (3) vs. ESG: no toda inversión ESG es temática; excluir emisores ≠ apostar activamente en beneficiarios de una transición. Lo que define un tema: exposición a un megatrend estructural que impacta economías y modelos de negocio.",
    "mcq": {
        "question": "Según Somefun et al. (2022), un índice temático de 'energía limpia' con altísima exposición al sector de utilities europeas sería problemático para un portafolio temático porque:",
        "options": [
            "A) Utilities tienen beta muy baja y reducen el retorno esperado del portafolio",
            "B) Si la mayor parte del riesgo viene del sector y no del tema, la inversión es solo un sector bet disfrazado",
            "C) Los índices de utilities tienen tracking error demasiado bajo para ser considerados temáticos",
            "D) ESG y temas no pueden coexistir en el mismo portafolio según el framework"
        ],
        "answer": "B",
        "explanation": "El paper enfatiza que un índice temático debe generar 'thematic volatility' significativa — riesgo no explicado por factores tradicionales (mercado, sector, estilo, región). Si el R² de la regresión Lasso contra sectores es muy alto, la inversión no aporta una nueva dimensión real al portafolio: es solo un sector bet con marketing temático."
    },
    "fill_blank": {
        "template": "Somefun et al. descomponen el riesgo de un índice temático en: volatilidad _______ (por factores macro), volatilidad específica (no explicada por el modelo de factores), y volatilidad temática (propia del tema).",
        "answers": ["sistemática", "sistemica", "systematic", "sistémica"]
    },
    "true_false": {
        "statement": "Según Somefun et al. (2022), el tema de 'Disruptive Tech' es el que tiene mayor proporción de riesgo específicamente temático (no explicado por factores tradicionales) entre los temas analizados.",
        "answer": False,
        "explanation": "¡Sorpresa contraintuitiva! Disruptive Tech tiene MENOR proporción de riesgo temático que Energy Transition o Environmental Sustainability. Solo el 31.7% de su riesgo residual es específicamente temático vs. 94.5% para Energy Transition. Disruptive Tech está muy explicado por factores sectoriales (IT, Small Cap Growth USA)."
    },
    "graph_type": "ai_value_chain",
    "connections": ["Factor model — Lasso regression", "Blitz (2021) — Crítica a índices temáticos S&P/MSCI", "Core-satellite framework", "Robust portfolio optimization"],
},

{
    "id": "th_bnp_002",
    "domain": "Thematic Investing",
    "topic": "Metodología — Lasso y Descomposición de Riesgo Temático",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "Somefun, Perchet, Yin & de Carvalho (2022) — Financial Analysts Journal",
    "front": "¿Por qué Somefun et al. usan regresiones Lasso en lugar de OLS estándar para identificar exposiciones de índices temáticos a factores regionales, sectoriales y de estilo?",
    "back": "Con 128 índices de equity y 46 de renta fija como regresores potenciales, OLS colapsa (problema de dimensión p>>n, multicolinealidad extrema). Lasso (L1 regularization) hace selección automática de variables al forzar muchos coeficientes a cero, produciendo un modelo parsimónico con los factores más relevantes. Esto evita overfitting y genera exposiciones interpretables. La regularización también estabiliza los coeficientes ante multicolinealidad de índices similares — crítico cuando sectores correlacionados compiten por explicar un mismo tema.",
    "latex": r"\min_\beta \sum(r_i - X\beta)^2 + \lambda \|\beta\|_1",
    "fill_blank": {
        "template": "El Lasso usa regularización L_______ (norma L1) que tiene la propiedad de forzar coeficientes exactamente a cero, haciendo selección de variables automáticamente.",
        "answers": ["1", "uno", "one", "L1"]
    },
    "true_false": {
        "statement": "El paper usa OLS en dos pasos: primero regresa contra el mercado (CAPM), y luego regresa los residuos contra índices de regiones/sectores/estilos vía Lasso.",
        "answer": True,
        "explanation": "Correcto: primero remueven el beta de mercado (CAPM) tanto del índice temático como de los regresores, luego aplican Lasso sobre los residuos. Este enfoque ortogonaliza la exposición de mercado antes de estimar exposiciones más granulares — evita que el beta de mercado 'domine' la regresión y oscurezca las exposiciones sectoriales menores."
    },
    "code_python": '''
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler

# Simular: residuos de un tema contra CAPM, y residuos de 128 factores
np.random.seed(42)
n, p = 260, 128  # 5 años de semanas, 128 factores potenciales
X = np.random.randn(n, p)  # residuos de factores vs. mercado
true_factors = [5, 12, 45]  # solo 3 factores realmente relevantes
beta_true = np.zeros(p)
beta_true[true_factors] = [0.4, 0.3, 0.25]
y = X @ beta_true + np.random.randn(n) * 0.02  # residuos del tema

# Lasso con cross-validation para seleccionar lambda
scaler = StandardScaler()
X_sc = scaler.fit_transform(X)
lasso = Lasso(alpha=0.01, max_iter=5000)
lasso.fit(X_sc, y)

# Factores seleccionados (coef != 0)
selected = np.where(lasso.coef_ != 0)[0]
print(f"Factores seleccionados: {selected}")
print(f"Coeficientes: {lasso.coef_[selected].round(4)}")
''',
    "connections": ["Ridge regression vs Lasso", "Regularización en factor models", "Sparse portfolios", "PCA — factor model de BNP"],
},

{
    "id": "th_bnp_003",
    "domain": "Thematic Investing",
    "topic": "Construcción de Portafolio — Robust Optimization con Temáticos",
    "difficulty": "Advanced",
    "mode_tags": ["bus", "home"],
    "source": "Somefun, Perchet, Yin & de Carvalho (2022) — FAJ; Perchet et al. (2016)",
    "front": "¿Por qué Somefun et al. usan robust optimization en lugar de MVO clásico para integrar inversiones temáticas en el SAA, y cuáles son los parámetros clave de input?",
    "back": "Robust optimization toma en cuenta la incertidumbre en las estimaciones de retorno esperado — crucial para temáticos donde el historial es corto (5–10 años) y los retornos esperados son inciertos. MVO clásico amplifica errores de estimación produciendo concentraciones extremas. Los inputs del paper: (1) Retornos esperados de activos core: SR histórico 0.3–0.4 desde 1954. (2) Retornos temáticos: exposiciones a factores macro + alpha temático asumiendo IR=0.3. (3) Modelo de riesgo PCA de 6 factores (explica 87% de varianza). Restricción: long-only, fully invested.",
    "mcq": {
        "question": "En el paper de Somefun et al., cuando se asume un Information Ratio de 0.3 para el alpha temático, ¿qué sucede si en realidad el alpha temático es cero (IR=0)?",
        "options": [
            "A) Los temáticos desaparecen completamente del portafolio",
            "B) Los temáticos aún pueden aparecer en el portafolio por su aporte de diversificación",
            "C) El Sharpe ratio del portafolio colapsa por debajo del portafolio sin temáticos",
            "D) El optimizer rechaza el tema por violar el constraint de tracking error"
        ],
        "answer": "B",
        "explanation": "Cita directa del paper: 'even a zero information ratio could have been used. In that case, thematic investments would only add diversification, much like diversification assets.' Si la volatilidad temática es suficientemente independiente de los factores macro, el optimizador la incluirá por su aporte de diversificación — incluso sin alpha. Esto es una implicancia importante: los temáticos tienen valor incluso si el alpha es cero."
    },
    "numerical_problem": {
        "question": "Un tema tiene volatilidad temática de 9.7% (Energy Transition per paper) y systematic vol de 12.1%. ¿Qué % del riesgo total de 15.8% es temático?",
        "steps": [
            "Volatilidad total = 15.8% (dato del paper, Tabla 3)",
            "Thematic vol = 9.7%",
            "% temático = (9.7 / 15.8) × 100",
            "= 61.4% del riesgo total es temático"
        ],
        "answer": "≈61% del riesgo total",
        "bus_hint": "9.7/15.8 ≈ 9.7/16 ≈ 0.61 → 61%. Energy Transition: mayoría de riesgo es genuinamente temático."
    },
    "graph_type": "theme_adoption_s_curve",
    "connections": ["Black-Litterman — robust priors", "Core-satellite SAA", "Tracking error constraints", "Information Ratio en gestión activa"],
},

{
    "id": "th_bnp_004",
    "domain": "Thematic Investing",
    "topic": "Resultados — Impacto de Temáticos en SAA por Perfil de Riesgo",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Somefun, Perchet, Yin & de Carvalho (2022) — FAJ; Tablas 4 y 5",
    "front": "¿Qué efecto produce añadir inversiones temáticas (Portfolio C) al SAA respecto a solo diversificación tradicional (Portfolio B), según los resultados de Somefun et al.?",
    "back": "Portafolio C (core + diversificación + temáticos) vs. B (core + diversificación): Sharpe ratio mejora para todos los perfiles (e.g., perfil moderado: de 0.44 a 0.49). El satélite crece al 40% del portafolio (vs. 15% en B). Los temáticos REEMPLAZAN parcialmente a diversificación tradicional (e.g., Emerging Markets Equity desaparece). La mayor diferencia de tracking error viene de volatilidad temática (0.6–0.7%), no de factores macro (solo 0.1–0.2%). El resultado clave: la adición de temáticos mejora el Sharpe sin aumentar significativamente el tracking error macro.",
    "mcq": {
        "question": "En los resultados del paper, ¿cuál tema temático tiene el mayor peso promedio en los portafolios C a través de todos los perfiles de riesgo?",
        "options": [
            "A) Disruptive Technology Equities",
            "B) Energy Transition Equities",
            "C) Environmental Sustainability Bonds",
            "D) Sustainable Water Equities"
        ],
        "answer": "C",
        "explanation": "Environmental Sustainability Bonds tiene pesos de 15.1% (conservative) a 17.7–18.7% (moderate) en el portafolio C. Su menor volatilidad (4% total) versus temáticos de equity permite al optimizer asignarle mayor peso sin violar el tracking error constraint — particularmente en perfiles conservadores donde hay demanda de renta fija."
    },
    "true_false": {
        "statement": "Según los resultados del paper, añadir inversiones temáticas (C vs. B) aumenta principalmente el riesgo macro del portafolio, incrementando las exposiciones a los factores de mercado y duration.",
        "answer": False,
        "explanation": "Incorrecto — este es el hallazgo más elegante del paper. El tracking error de C vs. B se explica casi totalmente por 'thematic tracking error' (0.4–0.7%) y muy poco por factores macro (0.1–0.2%). El optimizer aísla el risk budget temático del risk budget macro — los temáticos se integran sin 'contaminar' las exposiciones a factores sistemáticos."
    },
    "fill_blank": {
        "template": "Los portafolios C del paper muestran que la mayor parte del tracking error generado por añadir inversiones temáticas proviene de la volatilidad _______, no de cambios en exposiciones a factores macroeconómicos.",
        "answers": ["temática", "thematic", "específica del tema"]
    },
    "graph_type": "risk_parity_contributions",
    "connections": ["Factor risk attribution", "Satellite allocation", "Blitz (2021) — crítica a índices temáticos", "Robust optimization — Perchet et al."],
},

{
    "id": "th_bnp_005",
    "domain": "Thematic Investing",
    "topic": "Selección de Temas — Criterios de Calidad",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Somefun, Perchet, Yin & de Carvalho (2022) — FAJ; Blitz (2021)",
    "front": "¿Cuáles son los 4 criterios que Somefun et al. usan para SELECCIONAR qué temas y qué índices incluir en el portafolio (respondiendo a la crítica de Blitz 2021)?",
    "back": "Respondiendo a Blitz (2021) que encontró que índices temáticos de S&P y MSCI invierten en acciones de alta volatilidad, baja calidad y alta valuación: (1) Usar índices de múltiples proveedores por tema (no solo S&P/MSCI). (2) Diversificar entre temas con diferentes niveles de beta. (3) Seleccionar temas con bajo exposure a factores negativos de Blitz (high vol, low quality, expensive). (4) Exigir que el riesgo no explicado por factores tradicionales sea significativo — si el riesgo 'temático' es pequeño, el alpha también lo será.",
    "mcq": {
        "question": "Para un tema donde el R² de la regresión Lasso contra factores sectoriales y de estilo es del 95% (como ocurre con algunos ETFs de 'clean energy'), Somefun et al. concluirían que:",
        "options": [
            "A) El tema es ideal porque está muy bien explicado y predecible",
            "B) La volatilidad temática es mínima y el alpha esperado del tema probablemente sea pequeño",
            "C) El tema tiene demasiado riesgo sistemático para incluirse en un SAA conservador",
            "D) Hay que usar ese tema únicamente en portafolios agresivos con alta capacidad de riesgo"
        ],
        "answer": "B",
        "explanation": "Si el 95% del riesgo se explica por factores tradicionales, la volatilidad TEMÁTICA (el residuo) es muy pequeña. El framework dice que el alpha temático se remunera proporcionalmente a la volatilidad temática. Con poca volatilidad temática, incluso un IR de 0.3 genera poco alpha absoluto — la inversión no aporta suficiente valor añadido sobre simplemente comprar los sectores subyacentes."
    },
    "fill_blank": {
        "template": "Blitz (2021) critica que los índices temáticos de S&P y MSCI invierten en acciones de alta _______, baja calidad y alta valuación — sesgos que crean un drag en retornos que debe compensarse con suficiente alpha temático.",
        "answers": ["volatilidad", "volatility", "vol"]
    },
    "connections": ["Blitz (2021) — 'The smart beta industrial complex'", "Factor tilts en índices", "Quality factor", "Style biases en productos de inversión"],
},


# ════════════════════════════════════════════════════════════════
# ASSET ALLOCATION — Davidsson (2011)
# Portfolio Optimization and Linear Programming
# ════════════════════════════════════════════════════════════════

{
    "id": "aa_lp_001",
    "domain": "Asset Allocation",
    "topic": "Optimización — QP vs. LP: Escalabilidad y Trade-offs",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Davidsson (2011) — Journal of Money, Investment and Banking, Issue 20",
    "front": "¿Cuáles son los 4 métodos de optimización de portafolio por universo de activos según Davidsson (2011), y cuál es la ventaja principal de LP sobre QP?",
    "back": "Métodos por escala: (1) CO (Constrained Optimization con Lagrange): <10 activos. (2) QP (Quadratic Programming): <200 activos — estándar tradicional. (3) LP (Linear Programming): miles de activos. (4) SOCP (Second-Order Cone Programming): decenas de miles de activos — familia convexa más moderna. Ventaja LP sobre QP: velocidad computacional para universos grandes. La función objetivo LP de Davidsson usa enteros {−1, 0, 1} — portafolios igual-ponderados con posiciones long/short/nula. QP trabaja con retornos y pesos continuos; LP trabaja con precios y pesos discretos.",
    "mcq": {
        "question": "La formulación LP de Davidsson maximiza S^T·PP − S^T·Draw. ¿Qué están capturando estos dos términos?",
        "options": [
            "A) Maximiza retorno esperado y minimiza varianza (equivalente a Sharpe ratio)",
            "B) Maximiza momentum de precio (P[n]−P[0]) y minimiza drawdown máximo (Max−Min del precio)",
            "C) Maximiza el beta del portafolio y minimiza el tracking error",
            "D) Maximiza el Treynor ratio y minimiza el VaR"
        ],
        "answer": "B",
        "explanation": "PP = vector de diferencia P[n]−P[0] (momentum de precio total en el periodo). Draw = vector de Max(P)−Min(P) (máximo drawdown del precio en el periodo). El LP busca activos que subieron mucho (PP alto) con poca volatilidad en el camino (Draw bajo) — una proxy de Sharpe usando precios en lugar de retornos. No requiere estimar varianzas ni covarianzas."
    },
    "true_false": {
        "statement": "La formulación LP de Davidsson con enteros {-1, 0, 1} permite portafolios con pesos continuos variables entre -1 y +1 para cada activo.",
        "answer": False,
        "explanation": "Los pesos son enteros DISCRETOS: exactamente -1 (short), 0 (sin posición) o +1 (long). Esto impone igualdad de pesos entre todas las posiciones (equal weighting). Es una limitación importante: no puede sobre/subponderar activos individualmente. La ventaja es la velocidad computacional y la eliminación del problema de estimación de pesos óptimos."
    },
    "fill_blank": {
        "template": "La restricción S^T·W = 0 en la formulación LP de Davidsson garantiza la _______ del portafolio: el número de posiciones long cancela exactamente el número de posiciones short.",
        "answers": ["neutralidad de mercado", "market neutrality", "neutralidad", "market neutral"]
    },
    "numerical_problem": {
        "question": "En la formulación LP de Davidsson con PS=4 (portfolio size=4), ¿cuántas posiciones tiene el portafolio long-short y cuál es la restricción de suma de pesos?",
        "steps": [
            "PS = 4 → portafolio con 2×PS = 8 posiciones",
            "4 posiciones long (w=+1) y 4 posiciones short (w=−1)",
            "Suma de pesos: S^T·W = (+1)×4 + (−1)×4 = 0 ✓",
            "Restricción de cardinalidad: S^T·v = 2×PS = 8 (v_i=1 cuando hay posición)"
        ],
        "answer": "8 posiciones: 4 long + 4 short, suma = 0",
        "bus_hint": "PS=4 → 4 long + 4 short = 8 posiciones totales, suma de pesos = 4−4 = 0"
    },
    "graph_type": "efficient_frontier_bl",
    "connections": ["Markowitz MVO — QP estándar", "Cardinality constraints", "Equal weighting", "SOCP — optimización convexa"],
},

{
    "id": "aa_lp_002",
    "domain": "Asset Allocation",
    "topic": "Optimización — Cardinality Constraints",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Davidsson (2011) — Journal of Money, Investment and Banking",
    "front": "¿Qué son los cardinality constraints en optimización de portafolio y por qué son especialmente importantes para inversores pequeños o con costos de transacción altos?",
    "back": "Cardinality constraint: restricción que limita el NÚMERO de posiciones del portafolio (e.g., 'máximo 10 posiciones de un universo de 500'). Importante para: (1) Inversores con costos de transacción altos — un portafolio de 200 posiciones requiere 200 trades para rebalancear. (2) Administración operativa — monitorear cientos de posiciones es costoso. (3) Inversores pequeños con acceso limitado a plataformas algorítmicas. QP no maneja cardinality constraints naturalmente (requiere solvers MIP separados). LP con enteros {0,1} los maneja directamente — es una de las ventajas clave de la formulación de Davidsson.",
    "mcq": {
        "question": "¿Por qué QP estándar NO puede manejar cardinality constraints directamente?",
        "options": [
            "A) QP asume pesos continuos sin restricción de número de posiciones activas",
            "B) QP requiere una función objetivo cuadrática que no puede expresar número de activos",
            "C) La solución QP siempre produce portafolios con todos los activos con peso > 0",
            "D) Cardinality constraints violan la condición KKT de QP"
        ],
        "answer": "A",
        "explanation": "QP trabaja con pesos continuos w_i ∈ [−1, 1]. Para imponer que exactamente K activos tengan peso ≠ 0, necesitas variables binarias z_i ∈ {0,1} y restricciones del tipo w_i ≤ M·z_i — esto convierte el problema en un Mixed Integer QP (MIQP), mucho más complejo computacionalmente. LP con enteros {−1, 0, 1} incorpora la cardinalidad directamente en la estructura del problema."
    },
    "fill_blank": {
        "template": "El paper de Davidsson resuelve el problema de cardinality constraints usando optimización lineal con variables enteras _______, donde cada activo solo puede estar long, short o sin posición.",
        "answers": ["{-1, 0, 1}", "enteras {-1,0,1}", "binarias enteras", "integer"]
    },
    "true_false": {
        "statement": "Davidsson (2011) concluye que la formulación LP con enteros {-1,0,1} supera claramente a QP en retornos ajustados por riesgo en el backtesting sobre datos empíricos de SP-500.",
        "answer": False,
        "explanation": "Esta es una conclusión que el paper explícitamente NO puede hacer. La comparación directa LP vs QP en datos empíricos no se realizó — es una limitación explícita del paper. El autor reconoce que 'further testing is necessary'. El LP muestra buen performance en datos simulados pero la comparación rigurosa vs. QP sigue siendo una pregunta abierta."
    },
    "connections": ["Mixed Integer Programming (MIP)", "Transaction costs", "Concentrated portfolios", "Equal weighting strategies"],
},

{
    "id": "aa_lp_003",
    "domain": "Asset Allocation",
    "topic": "Optimización — Overfitting y la Brecha In-Sample vs. Out-of-Sample",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Davidsson (2011) — Journal of Money, Investment and Banking; Taleb (2007)",
    "front": "¿Qué hallazgo empírico de Davidsson (2011) sobre el SP-500 ilustra el problema de overfitting en backtesting de portafolios, y cuáles son las 4 explicaciones que el autor propone?",
    "back": "El equity curve in-sample (datos simulados) es muy suave y creciente. El equity curve out-of-sample (SP-500 2005–2010) es errático y sufre durante la crisis 2008 a pesar de ser long-short. Las 4 explicaciones: (1) Muestra pequeña / universo pequeño — la señal no es extrapolable. (2) Datos simulados más 'bien comportados' — correlación constante 0.4 asumida no se cumple in reality. (3) LP puede haber bajo-rendido vs. QP. (4) Variables explicativas faltantes — la función objetivo no captura exposición al riesgo de mercado (beta) suficientemente. Lección: ningún algoritmo escapa al problema fundamental de estabilidad de parámetros.",
    "mcq": {
        "question": "Davidsson sugiere que optimizar el Treynor ratio en lugar del Sharpe ratio habría reducido el problema durante el crash de 2008. ¿Por qué?",
        "options": [
            "A) El Treynor ratio maximiza el retorno por unidad de beta — forzando al portafolio a ser beta-neutral",
            "B) El Treynor ratio no requiere estimar la varianza, reduciendo el error de estimación",
            "C) El Treynor ratio incluye el risk-free rate que sirvió de refugio en 2008",
            "D) El Treynor ratio premia portafolios concentrados que se benefician de disrupciones"
        ],
        "answer": "A",
        "explanation": "Treynor = (R_p − R_f) / β_p. Maximizar Treynor implica también minimizar β_p — el algoritmo tendería hacia posiciones beta-neutrales. Un portafolio beta-neutral sufrió menos en el crash de 2008 que uno que simplemente era 'equal long-short' sin control explícito de beta. La formulación Sharpe de Davidsson maximiza retorno/riesgo total pero no controla el beta del portafolio."
    },
    "true_false": {
        "statement": "Según Davidsson, la diferencia entre la curva in-sample (simulada) y out-of-sample (empírica) se debe principalmente a que los datos simulados tienen correlación cruzada NEGATIVA constante.",
        "answer": False,
        "explanation": "Al revés: los datos simulados tienen correlación cruzada POSITIVA constante (0.4). Una correlación positiva alta y constante en un portafolio long-short genera una curva suave porque las posiciones se diversifican bien. En los datos reales del SP-500, la correlación NO fue constante — colapsa durante crisis (efecto 'correlation goes to 1 in a crash') arruinando el beneficio de la diversificación."
    },
    "fill_blank": {
        "template": "Taleb llama 'falacia _______ ' (del latín ludus) a la creencia de que los procesos financieros se comportan como juegos de casino con probabilidades estables — una suposición que subyace en muchos modelos de optimización.",
        "answers": ["lúdica", "ludica", "lúdico", "ludic fallacy", "lúdica o ludic"]
    },
    "graph_type": "correlation_matrix_regimes",
    "connections": ["Overfitting en backtesting", "Walk-forward testing", "Sharpe vs Treynor ratio", "Taleb — Black Swan", "Correlaciones en crisis"],
},

{
    "id": "aa_lp_004",
    "domain": "Asset Allocation",
    "topic": "Optimización — Autocorrelación y Momentum como Fundamento",
    "difficulty": "Foundational",
    "mode_tags": ["bus", "home"],
    "source": "Davidsson (2011); Conrad & Kaul (1988); Engle (1982)",
    "front": "¿Cuál es el fundamento empírico que justifica la optimización de portafolio según Davidsson, y por qué la autocorrelación positiva de retornos y varianzas es la premisa clave?",
    "back": "Fundamento: retornos esperados (Conrad & Kaul 1988) y varianzas de retorno (Engle 1982 — ARCH) exhiben autocorrelación positiva: si el Sharpe ratio es alto hoy, probablemente sea alto mañana. Esto hace viable la optimización: los parámetros estimados tienen poder predictivo. Sin autocorrelación (ruido puro), cualquier portafolio óptimo basado en historia pasada sería inútil. La autocorrelación de varianza (clustering de volatilidad) justifica modelos GARCH. La limitación: en el largo plazo, hay structural breaks — los parámetros no son constantes eternamente, requiriendo rebalanceo frecuente.",
    "mcq": {
        "question": "Si los retornos de activos NO tuvieran autocorrelación positiva (fueran ruido puro), ¿qué implicaría para la optimización de portafolio basada en datos históricos?",
        "options": [
            "A) La optimización histórica seguiría siendo válida porque la diversificación no requiere autocorrelación",
            "B) La optimización histórica perdería su poder predictivo — cualquier portafolio sería igual de bueno",
            "C) Solo QP fallaría — LP seguiría funcionando porque no estima correlaciones",
            "D) El rebalanceo más frecuente compensaría la falta de autocorrelación"
        ],
        "answer": "B",
        "explanation": "Si los retornos son i.i.d. (no hay autocorrelación), el mejor predictor del Sharpe ratio futuro no es el Sharpe ratio pasado — la historia no aporta información sobre el futuro. El portafolio óptimo histórico sería tan bueno como uno aleatorio out-of-sample. La autocorrelación positiva es la condición necesaria para que cualquier modelo de portafolio basado en datos pasados tenga valor."
    },
    "true_false": {
        "statement": "Davidsson argumenta que el risk-free rate es la única tasa que NO puede experimentar cambios en retorno esperado, y por eso permanece como constante en la teoría de portafolio.",
        "answer": True,
        "explanation": "Por definición (por el valor tiempo del dinero), el prestamista siempre recibe un retorno positivo y cierto — sin riesgo de cambio en el retorno esperado. Sin embargo, el paper también señala que el risk-free rate ha caído estructuralmente en 30 años, lo que es una complicación práctica: aunque teóricamente constante, el nivel del risk-free sí cambia secularmente, afectando todos los Sharpe ratios calculados históricamente."
    },
    "fill_blank": {
        "template": "Davidsson cita a Fabozzi & Focardi (2010) para argumentar que la diversificación debería ser de _______, no solo de fluctuaciones locales — reconociendo que los retornos esperados cambian estructuralmente con el tiempo.",
        "answers": ["expectativas", "expectations", "expectativas de retorno"]
    },
    "connections": ["GARCH — volatility clustering", "Conrad & Kaul (1988) — autocorrelación de retornos", "Structural breaks", "Regime switching models"],
},

# ════════════════════════════════════════════════════════════════
# EQUITY INVESTING — Yee (2004)
# Forward Versus Trailing Earnings in Equity Valuation
# Review of Accounting Studies, 9, 301–329
# ════════════════════════════════════════════════════════════════

{
    "id": "eq_fwd_001",
    "domain": "Equity Investing",
    "topic": "Valoración — Forward vs. Trailing Earnings",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Yee, K.K. (2004) — Review of Accounting Studies 9:301–329; Columbia Business School. DOI: 10.1023/B:RAST.0000028195.75276.44",
    "front": "¿Por qué las forward earnings son teóricamente más precisas como atributo de valoración que las trailing earnings, según Yee (2004)?",
    "back": "Porque cuando existen variables de información no observables (como el estado del ciclo de demanda de la industria), las accrual rules lineales NO pueden lograr relaciones contemporáneas exactas valor-earnings — requieren actualización bayesiana no lineal por parte del contador. En cambio, SÍ pueden lograr relaciones forward exactas, porque el analista que hace el forecast incorpora su propia estimación bayesiana (mt) al proyectar. Así, forward accounting traslada la carga de la inferencia subjetiva del contador al usuario de los estados financieros. Regla general: cuanto más hacia adelante el earnings, más preciso como atributo de valoración.",
    "latex": r"V_t = \frac{f \cdot E_t[ox_{t+1}]}{R} \quad \text{(forward)} \quad \text{vs.} \quad V_t = f \cdot ox_t^c - c_t \quad \text{(contemporánea, no lineal)}",
    "intuition": "Las trailing earnings son como navegar mirando solo por el espejo retrovisor — el contador trata de incorporar todo lo que el mercado sabe, pero no puede hacerlo sin subjetividad. Las forward earnings le piden al conductor que señale hacia dónde va: el analista que pronostica usa su propia visión del futuro (mt), y eso es exactamente lo que necesita la valoración.",
    "mcq": {
        "question": "En el modelo de Yee (2004), ¿qué es mt y por qué genera heterogeneidad de creencias entre analistas?",
        "options": [
            "A) mt es la tasa de descuento del mercado, que varía según el risk premium de cada inversor",
            "B) mt es la creencia bayesiana sobre la probabilidad de que la industria esté en estado de alta persistencia (H), y varía porque depende del prior m₀ subjetivo de cada analista",
            "C) mt es el múltiplo de capitalización aplicado a los earnings forward, que varía por diferencias en metodología",
            "D) mt es el margen de error de los accruals contables, determinado por la calidad de auditoría",
        ],
        "answer": "B",
        "explanation": "mt = Pr(st=H | m₀, Ω_t) es la probabilidad bayesiana de que el estado de la industria sea 'alta persistencia' dado el prior m₀ y toda la historia de shocks. Dos analistas igualmente racionales con la misma información pueden tener mt distintos si su m₀ inicial difiere — y m₀ es puramente subjetivo. Esta heterogeneidad NO requiere asimetría de información.",
    },
    "true_false": {
        "statement": "Según Yee (2004), si una política contable logra una relación contemporánea exacta (Vt = f·oxt − ct), entonces automáticamente logra también la relación forward (Vt = f·E[oxt+1]/R).",
        "answer": True,
        "explanation": "Ohlson (1991) demostró que cualquier sistema que logre la relación contemporánea la logra también como subproducto, pero NO al revés. La relación forward es menos exigente: se puede lograr con accruals lineales incluso cuando la contemporánea requiere no-linealidad bayesiana.",
    },
    "fill_blank": {
        "template": "En Yee (2004), la accrual policy forward-earnings logra una relación valor-earnings lineal sin requerir que el contador estime mt, porque traslada esa inferencia _______ al usuario del estado financiero que hace el forecast.",
        "answers": ["bayesiana", "subjetiva", "no lineal", "bayesian"],
    },
    "connections": ["Ohlson (1995) — modelo residual income", "Accruals quality — Dechow & Dichev", "Analyst forecasts — valor informativo de EPS estimates", "Shaffer (2024) — multiples en M&A"],
},

{
    "id": "eq_fwd_002",
    "domain": "Equity Investing",
    "topic": "Valoración — Más Forward = Más Preciso",
    "difficulty": "Advanced",
    "mode_tags": ["bus", "home"],
    "source": "Yee, K.K. (2004) — Review of Accounting Studies 9:301–329; Columbia Business School",
    "front": "¿Qué establece la Proposición 2 de Yee (2004) sobre horizonte del forecast y precisión de valoración, y qué implica para el uso de EPS 1Y vs. 2Y forward?",
    "back": "Proposición 2: para cualquier error de valoración ε>0 deseado, existe un horizonte F* tal que el forecast F-períodos adelante logra error < ε para todo F≥F*. Implicancia: si hay variables no observables en S estados, un forecast F=S-1 períodos adelante puede lograr valoración exacta con accruals lineales. El EPS 2Y-forward es generalmente más preciso que el 1Y-forward — aunque la mejora no es siempre estrictamente monotónica. Esto justifica el uso de NTM+1 en modelos de valoración.",
    "latex": r"\|V_t - \hat{V}_t(F')\| \leq \|V_t - \hat{V}_t(F)\| \quad \forall F' > F",
    "mcq": {
        "question": "La Observación 1 de Yee (2004) muestra que el error de valoración decae con el horizonte de forecast cuando los earnings tienen ruido persistente de duración T. ¿Cuál es la fórmula del error para F<T?",
        "options": [
            "A) error(F) = σ²_Z × F, creciente con el horizonte",
            "B) error(F) = (f/R^F)² × σ²_Z × (T−F), decreciente con F; cero para F≥T",
            "C) error(F) = σ²_Z / F, decreciente hiperbólicamente",
            "D) error(F) = σ²_Z × (1−ρ^F), convergiendo asintóticamente",
        ],
        "answer": "B",
        "explanation": "error(F) = (f/R^F)² × σ²_Z × (T−F) para F<T. Cuando F≥T, el error es exactamente cero — los cargos contables persistentes se han revertido completamente. Para F<T, el error decrece linealmente con F porque hay T−F cargos aún pendientes de reversión. Los errores temporales de accruals se 'cancelan' al mirar suficientemente hacia adelante.",
    },
    "true_false": {
        "statement": "Yee (2004) demuestra de forma incondicional (Conjetura A) que más-forward earnings es siempre más preciso que menos-forward earnings para cualquier política contable posible.",
        "answer": False,
        "explanation": "El paper explícitamente reconoce que la Conjetura A (validez universal) NO pudo ser probada — ni siquiera el autor la considera plausible en su forma más fuerte. Lo que sí se prueba es la Proposición 2 (existencia de al menos una política contable para la que más-forward es más preciso) y la Observación 1 (para ruido i.i.d. persistente). La honestidad del paper sobre sus propias limitaciones es clave.",
    },
    "fill_blank": {
        "template": "Si el espacio de la variable no observable abarca S estados, una accrual policy lineal con S parámetros puede lograr valoración exacta para forecasts de horizonte F ≥ _______.",
        "answers": ["S-1", "S menos 1", "S−1"],
    },
    "connections": ["EPS consensus estimates — 1Y vs 2Y forward", "NTM earnings en modelos DCF", "Accrual accounting — persistencia de errores", "Ohlson-Juettner-Nauroth (2000) — AEG model"],
},

{
    "id": "eq_fwd_003",
    "domain": "Equity Investing",
    "topic": "Valoración — Efficient Accounting con Variables No Observables",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "Yee, K.K. (2004) — Review of Accounting Studies 9:301–329; Columbia Business School",
    "front": "¿Por qué el Lema 3 de Yee (2004) implica que el 'efficient accounting' (Feltham-Ohlson) es imposible con accruals lineales cuando hay variables no observables, y qué solución ofrece el paper?",
    "back": "Efficient accounting requiere valor = combinación lineal de book value y earnings. Pero cuando Vt depende de mt (creencia bayesiana sobre estado no observable), los accruals lineales no pueden capturar mt — que es una función no lineal de toda la historia de shocks. Lema 3: ninguna elección de parámetros {d₀, d₁, d₂} logra efficient accounting. Solución de Yee: relajar el objetivo a relaciones forward — con política OXF lineal se logra Vt = f·E[oxt+1]/R sin necesitar mt. Alternativa para mantener efficient accounting: accruals dependientes de beliefs (no lineales), o anclar a cash flow forecasts como proxies de mt (Observación 3).",
    "latex": r"ox_t = (1+d_1)c_t - (1-d_0)oa_{t-1} + d_2 n_t \quad \text{(lineal, belief-free)} \implies \text{no logra efficient accounting}",
    "fill_blank": {
        "template": "El Lema 3 de Yee demuestra que la efficient accounting de Feltham-Ohlson es imposible con accruals _______ cuando el flujo de caja depende de una variable de estado no observable.",
        "answers": ["lineales", "belief-free", "lineales y libres de creencias", "linear"],
    },
    "true_false": {
        "statement": "En el modelo de Yee (2004), las reservas de siniestros de seguros que anclan a forecasts de cash flows son equivalentes a políticas contables que dependen explícitamente de beliefs bayesianos.",
        "answer": True,
        "explanation": "Observación 3: la política que usa ct+1 (forecast de cash flow) como proxy de mt produce exactamente la misma efficient accounting que la política que usa mt directamente. Esto racionaliza por qué SFAS 60 (seguros) exige reservas basadas en forecasts de pagos futuros — es incorporar beliefs sin nombrarlos. La subjetividad existe igualmente; solo está enmascarada.",
    },
    "connections": ["Feltham-Ohlson (1995/1996) — efficient accounting", "SFAS 60 — reservas de seguros", "Accruals no lineales", "Creencias heterogéneas y precios de activos"],
},

{
    "id": "eq_fwd_004",
    "domain": "Equity Investing",
    "topic": "Valoración — Aplicación: NTM vs. TTM P/E",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Yee (2004) — RAS; Shaffer (2024) — RAS; Koller et al. (2020) — Valuation (McKinsey)",
    "front": "¿Cómo el resultado de Yee (2004) justifica el uso de NTM P/E sobre TTM P/E, y en qué contextos el TTM sigue siendo relevante?",
    "back": "Justificación teórica: si las trailing earnings incorporan shocks transitorios no observables (write-offs, provisiones inusuales), el TTM P/E será volátil y ruidoso — no guarda relación lineal estable con el precio. NTM earnings filtran esos ruidos porque los analistas proyectan condiciones normalizadas, incorporando su propia mt. TTM sigue siendo relevante cuando: (1) sin cobertura de analistas (small caps, mercados emergentes como Perú), (2) empresa cíclica con earnings normalizados históricos (ej. Shiller CAPE), (3) M&A donde los abogados prefieren números auditados para limitar litigación.",
    "mcq": {
        "question": "Shaffer (2024) documenta que en M&A advisory se usan trailing multiples el 42% del tiempo y forward solo el 25%, aunque la teoría recomienda forward. ¿Cuál es la explicación más consistente con Yee (2004)?",
        "options": [
            "A) Los trailing earnings son más precisos en M&A por el mayor riesgo de forecast",
            "B) Los asesores prefieren trailing por su menor subjetividad aparente — anclan a números auditados para limitar litigación, aunque teóricamente sean menos precisos",
            "C) La regulación SEC prohíbe el uso de earnings forecasts de terceros en fairness opinions",
            "D) Los trailing multiples producen valuaciones sistemáticamente más altas, beneficiando al target advisor",
        ],
        "answer": "B",
        "explanation": "Yee (2004) advierte que los trailing earnings parecen más 'objetivos' porque no dependen de beliefs del analista — pero es una ilusión cuando hay variables no observables. DeAngelo (1990) lo explica: los multiples contables se prefieren porque son 'transparentes y anclados en señales comúnmente reconocidas', aunque teóricamente inferiores. Paradoja: trailing parece más objetivo pero es potencialmente menos preciso.",
    },
    "true_false": {
        "statement": "El CAPE de Shiller (precio / earnings promedio 10 años ajustado por inflación) contradice directamente el resultado de Yee (2004) al usar trailing earnings.",
        "answer": False,
        "explanation": "No necesariamente. El CAPE promedia 10 años para suavizar shocks transitorios — precisamente los Zt que distorsionan las trailing earnings en Yee. La media de 10 años actúa como filtro que reduce el ruido de corto plazo, aproximando earnings normalizados. Donde sí hay tensión: el CAPE no captura cambios estructurales en márgenes o crecimiento que sí captaría un NTM forecast.",
    },
    "fill_blank": {
        "template": "El P/E usando earnings _______ es teóricamente más preciso porque el analista que hace el forecast incorpora su propia estimación bayesiana del estado no observable de la industria.",
        "answers": ["forward", "proyectados", "futuros", "NTM", "next twelve months"],
    },
    "graph_type": "pe_ratio_vs_growth",
    "connections": ["Shiller CAPE", "NTM vs TTM P/E en Bloomberg", "I/B/E/S analyst earnings forecasts", "Shaffer (2024) — multiples en M&A"],
},


# ════════════════════════════════════════════════════════════════
# EQUITY INVESTING — Shaffer (2024)
# Which Multiples Matter in M&A? An Overview
# Review of Accounting Studies (2024) 29:2724–2752
# ════════════════════════════════════════════════════════════════

{
    "id": "eq_mna_001",
    "domain": "Equity Investing",
    "topic": "Valoración M&A — Las 4 Dimensiones de los Multiples",
    "difficulty": "Foundational",
    "mode_tags": ["bus", "home"],
    "source": "Shaffer, M. (2024) — Review of Accounting Studies 29:2724–2752; USC Marshall. DOI: 10.1007/s11142-023-09768-7",
    "front": "¿Cuáles son las 4 dimensiones en que Shaffer (2024) clasifica todos los multiples en M&A advisory, y cuál es el hallazgo más llamativo sobre la distribución de frecuencias?",
    "back": "Las 4 dimensiones: (1) Numerador: Enterprise Value vs. Equity Value. (2) Value driver denominador: EBITDA, Net Income, Revenue, Book Equity, EBIT, etc. (3) Período de medición: trailing (pasado), current (LTM), o forward (NTM). (4) Tipo de comps: comparable transactions vs. comparable trading firms. Hallazgo llamativo: enorme heterogeneidad — el multiple más común (EV/EBITDA current, trading comps) representa apenas 7.48% de la muestra. Se necesitan los 22 multiples más frecuentes para cubrir el 80% del total. Los 5 value drivers dominantes (EBITDA 32%, Net Income 25%, Revenue 22%, Book Equity 9%, EBIT 6%) cubren el 95%, pero cash flow metrics solo el 1.8%.",
    "mcq": {
        "question": "Shaffer (2024) encuentra que cash flow metrics representan solo 1.8% de los multiples en M&A. ¿Qué implica esto respecto al debate sobre la relevancia del accrual accounting?",
        "options": [
            "A) Confirma que el accrual accounting es irrelevante y debe reemplazarse por métricas de caja",
            "B) Es paradójico: a pesar del debate académico sobre declining value-relevance de accruals, los practicantes de M&A los usan casi universalmente como value drivers",
            "C) Los advisors de M&A no conocen la teoría de DCF y por eso evitan métricas de cash flow",
            "D) El 1.8% es consistente con la teoría porque el FCF libre de deuda es difícil de observar",
        ],
        "answer": "B",
        "explanation": "La paradoja señalada por Shaffer: precisamente cuando Lev & Gu (2016) y otros académicos argumentan que el accounting ha perdido relevancia, los usuarios más sofisticados de financial statements en el mundo (bancos de inversión en M&A de $bn) siguen usando métricas de accrual accounting en el 97%+ de sus valuaciones. La 'revealed preference' de los practitioners contradice la narrativa de declining relevance.",
    },
    "true_false": {
        "statement": "En M&A advisory, según Shaffer (2024), el P/Book es un múltiplo frecuentemente usado en la mayoría de sectores industriales.",
        "answer": False,
        "explanation": "Book equity como value driver aparece en solo 9% total, y está masivamente concentrado en FIRE (Finance, Insurance, Real Estate) donde llega al 32%. Para empresas industriales y de servicios, solo 2.0%. Shaffer concluye que los M&A advisors tratan al P/Book como irrelevante para empresas operativas — lo que contrasta con su amplio uso en investigación académica.",
    },
    "fill_blank": {
        "template": "La revealed preference de los advisors de M&A en Shaffer (2024) muestra que las métricas del estado de _______ dominan (97%) sobre métricas de flujo de caja como value drivers de valoración.",
        "answers": ["resultados", "income statement", "cuenta de resultados", "resultados y balance"],
    },
    "graph_type": "pe_ratio_vs_growth",
    "intuition": "Los asesores de M&A son como arquitectos que saben que el cemento reforzado es superior, pero siguen usando ladrillo porque todos lo entienden, es auditable, y nadie los puede demandar por usarlo. El trailing EBITDA no es la 'verdad' económica, pero es la lengua común de las salas de directorio.",
    "connections": ["EV/EBITDA como múltiplo preferido", "DeAngelo (1990) — por qué multiples en M&A", "Yee (2004) — forward vs. trailing earnings", "Fairness opinions — Smith v. Van Gorkom"],
},

{
    "id": "eq_mna_002",
    "domain": "Equity Investing",
    "topic": "Valoración M&A — El Puzzle de los Trailing Multiples",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Shaffer, M. (2024) — Review of Accounting Studies 29:2724–2752; USC Marshall",
    "front": "¿Por qué Shaffer (2024) describe como 'puzzle' que los asesores de M&A usen trailing multiples (42%) más que forward (25%), cuando teoría, textos y los propios DCFs del mismo deal usan proyecciones?",
    "back": "Es un puzzle porque: (1) McKinsey Valuation y la teoría recomiendan explícitamente forward multiples. (2) No hay restricción legal — Delaware referencia DCFs con múltiples años de proyecciones. (3) Los mismos asesores presentan DCFs en el 84% de los deals — que requieren 5-10 años de proyecciones. (4) Forecasts de analistas están disponibles para la mayoría de empresas públicas. (5) Shaffer verifica que los advisors NO usan más forward multiples incluso cuando ya incluyeron un DCF en el mismo deal — descartando la hipótesis de que 'ya cubrieron esa base'. Ninguna explicación simple es satisfactoria.",
    "mcq": {
        "question": "Cuando los advisors NO incluyen DCF en el deal (16% de los casos), ¿qué cambio en value driver ocurre según Shaffer (2024)?",
        "options": [
            "A) Usan más EBITDA para compensar la ausencia del análisis de flujos",
            "B) Usan menos earnings multiples y más revenue multiples — porque ambos (earnings y DCF) son inviables para empresas no rentables",
            "C) Usan más forward multiples para reemplazar el poder predictivo del DCF",
            "D) Usan más book equity como proxy de valor intrínseco",
        ],
        "answer": "B",
        "explanation": "Sin DCF: revenue sube de 20.7% a 30.4%; earnings baja de 25.2% a 21.8%; EBITDA baja de 33.3% a 25.9%. La explicación: advisors consideran que tanto DCF como earnings multiples son inadecuados para empresas pre-rentables — usan revenue como único denominador viable. Esto sugiere que DCF y earnings multiples son sustitutos en la percepción del practicante, no complementos.",
    },
    "true_false": {
        "statement": "Usar comparable transaction multiples en M&A establece un benchmark de valoración más alto que trading multiples, porque los precios de transacciones pasadas incluyen el premium de control.",
        "answer": True,
        "explanation": "La prima de control en la muestra de Shaffer es 30% (mediana) a 38% (media) sobre el precio de mercado a 30 días. Los transaction comps están calculados sobre deal prices que ya incluyen ese premium. Al usar transaction comps, el advisor benchmarks el target contra empresas ya adquiridas con premium — lo que Shaffer señala como relevante para el debate sobre sesgos de advisors.",
    },
    "fill_blank": {
        "template": "Los multiples de _______ proveen una estimación del valor en el mercado de control corporativo, mientras que los trading comps estiman el valor standalone.",
        "answers": ["transaction comps", "transacciones comparables", "comparable transactions", "precedent transactions"],
    },
    "connections": ["Comparable company analysis (CCA)", "Precedent transaction analysis (PTA)", "Control premium en M&A", "Eaton et al. (2001) — sesgos de peer selection"],
},

{
    "id": "eq_mna_003",
    "domain": "Equity Investing",
    "topic": "Valoración M&A — EV vs. Equity Value: Regla de Consistencia",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Shaffer, M. (2024) — Review of Accounting Studies 29:2724–2752; Damodaran (2012) — Investment Valuation",
    "front": "¿Cuándo usar EV multiples vs. Equity Value multiples, y qué excepción documenta Shaffer (2024) para el sector FIRE?",
    "back": "Regla de consistencia: numerador y denominador deben representar a la misma entidad. EV (equity + deuda neta) → denominadores pre-deuda: EBITDA, EBIT, Revenue. Equity Value → denominadores post-deuda: Net Income, Book Equity. Excepción FIRE documentada por Shaffer: para bancos y aseguradoras, los advisors usan Equity Value en el 84% de casos (vs. 27% en otros sectores). Razón: definir 'net debt' es problemático cuando los depósitos son simultáneamente 'deuda' y 'activo operativo'. El balance ES el activo en firmas financieras, por lo que P/Book y equity multiples son más naturales.",
    "numerical_problem": {
        "question": "Una empresa tiene EBITDA = $100M, Net Debt = $200M, y comparables trading tienen EV/EBITDA = 8x. ¿Cuál es el Equity Value implícito?",
        "steps": [
            "EV implícito = 8x × $100M = $800M",
            "Equity Value = EV − Net Debt = $800M − $200M = $600M",
        ],
        "answer": "Equity Value = $600M",
        "bus_hint": "EV = 8×100 = 800 → Equity = 800 − 200 = 600",
    },
    "mcq": {
        "question": "Un analista usa EV/Net Income para valorar una empresa. ¿Cuál es el problema fundamental?",
        "options": [
            "A) Net Income es volátil y no refleja el poder de generación de caja",
            "B) EV incluye deuda, pero Net Income ya descontó los intereses — inconsistencia entre numerador pre-deuda y denominador post-deuda",
            "C) El múltiplo no es comparable entre firmas con diferentes tasas impositivas",
            "D) Net Income incluye items no recurrentes que distorsionan el múltiplo",
        ],
        "answer": "B",
        "explanation": "EV representa el valor total (accionistas + acreedores), pero Net Income ya restó intereses — es solo el retorno para el accionista. Mezcla a quién beneficia el numerador vs. el denominador. Lo correcto: EV/EBITDA o EV/EBIT para valor total; Equity/Net Income (P/E) para valor del accionista.",
    },
    "fill_blank": {
        "template": "El EV/EBITDA domina en M&A porque es consistente con Enterprise Value y neutral respecto a diferencias en estructura de _______, depreciación y tasas impositivas entre compañías comparables.",
        "answers": ["capital", "capital y deuda", "deuda", "financiamiento"],
    },
    "connections": ["EBITDA como proxy de FCF operativo", "Net debt adjustment en M&A", "P/E vs EV/EBITDA — cuándo usar cada uno", "Sector FIRE — valoración por P/Book"],
},

{
    "id": "eq_mna_004",
    "domain": "Equity Investing",
    "topic": "Valoración M&A — Tendencias 2000-2020: EBITDA, Non-GAAP y Decline del P/Book",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Shaffer, M. (2024) — Review of Accounting Studies 29:2724–2752; Lev & Gu (2016) — The End of Accounting",
    "front": "¿Qué tres tendencias documenta Shaffer (2024) en la evolución de multiples de M&A entre 2000-2020, y qué paradoja normativa señala?",
    "back": "Tres tendencias: (1) EV multiples crecen de ~55% a ~65%+ del total. (2) EBITDA reemplaza a Net Income y EBIT como value driver dominante — acelerado post-2005, vinculado al auge Non-GAAP y preferencia por métricas más arriba en el income statement. (3) Book equity cae sostenidamente de ~12% a <6%, atribuido al crecimiento de intangibles no reconocidos (IP, brand, data) que hacen el book value menos representativo. Paradoja normativa: si los usuarios más sofisticados de financial statements usan casi exclusivamente flow measures para valorar, ¿justifica esto seguir invirtiendo esfuerzos en mejorar el balance sheet para empresas operativas?",
    "mcq": {
        "question": "Shaffer (2024) señala que el aumento de EBITDA en M&A NO se explica solo por la migración hacia EV multiples. ¿Cuál es su explicación adicional?",
        "options": [
            "A) Los DCFs usan EBITDA como punto de partida, y su auge arrastró a los multiples",
            "B) Dentro de los EV multiples, EBITDA también desplazó al EBIT — vinculado al fenómeno Non-GAAP y preferencia por métricas que excluyen D&A y restructuring",
            "C) Los reguladores contables redefinieron EBIT para incluir items que antes excluía, haciendo EBITDA más limpio",
            "D) Las empresas con mayor deuda prefieren EBITDA porque sube su valoración al ignorar intereses",
        ],
        "answer": "B",
        "explanation": "EBITDA y EBIT compiten en el mismo espacio (ambos pre-intereses, ambos matched con EV). Si el cambio fuera solo por el auge de EV multiples, EBIT y EBITDA crecerían igualmente. Pero EBITDA desplazó también al EBIT — Shaffer lo vincula al auge del Non-GAAP reporting y la preferencia por excluir D&A y costos de restructuring para mostrar una métrica de 'cash earnings' más alta.",
    },
    "true_false": {
        "statement": "La caída del P/Book en M&A advisory entre 2000-2020 implica que el mercado de control corporativo ha abandonado el valor en libros como referencia de valoración para empresas del sector financiero.",
        "answer": False,
        "explanation": "La caída es para empresas operativas (industriales, servicios, retail). El sector FIRE (Finance, Insurance, Real Estate) es la excepción: en esas industrias el Book Equity sigue siendo el value driver en el 32% de los casos. Shaffer distingue explícitamente: para firmas financieras donde los activos en balance son el negocio (préstamos, depósitos, securities), el book value es relevante. Para empresas con intangibles no capitalizados, no.",
    },
    "fill_blank": {
        "template": "La declining relevance del Book Equity como value driver en M&A refleja el crecimiento de _______ no reconocidos en balance, que hacen que el book value subestime progresivamente los activos económicos reales.",
        "answers": ["intangibles", "activos intangibles", "intangible assets"],
    },
    "connections": ["Lev & Gu (2016) — The End of Accounting", "Non-GAAP earnings — auge post-2000", "Intangibles y relevancia del accounting", "Income statement vs. balance sheet (FASB debate)"],
},

# 06/06/2026
# ════════════════════════════════════════════════════════════════
# EQUITY INVESTING — Oh & Penman (2024)
# A Proposal for Goodwill Accounting
# KAIST / Columbia Business School — January 2024
# ════════════════════════════════════════════════════════════════

{
    "id": "eq_gw_001",
    "domain": "Equity Investing",
    "topic": "Valoración M&A — Descomposición del Precio de Adquisición",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Oh, H.I. & Penman, S. (2024) — 'A Proposal for Goodwill Accounting', KAIST / Columbia Business School, January 2024",
    "front": "¿Cuáles son los 4 componentes en que Oh & Penman (2024) descomponen el precio de adquisición en M&A, y cuál es la fórmula central?",
    "back": "Precio de adquisición = (1) Book value del target (Bt) + (2) Fair value de earnings adquiridos [(OIt − r·NOAt)/r] + (3) Value of Growth acquired (valor del crecimiento esperado del target standalone) + (4) Value of Combination (sinergias). El goodwill es la suma de (3) y (4): todo lo que excede el book value y los earnings actuales del target. Esta descomposición es objetiva — usa datos auditados disponibles al anuncio — versus el 'plug' subjetivo del GAAP.",
    "latex": r"P_{acq} = B_t + \frac{OI_t - r \cdot NOA_t}{r} + V_{growth} + V_{combo}",
    "intuition": "Comprar una empresa es como comprar una casa: el book value es el terreno (activos físicos), los earnings capitalizados son la renta que ya genera, el value of growth es el potencial de revalorización del barrio, y las sinergias son lo que tú específicamente puedes hacer con ella que otros no. El GAAP actual mezcla todo en un solo número — 'goodwill' — sin decirte qué parte es qué.",
    "mcq": {
        "question": "Procter & Gamble pagó $57B por Gillette. Book value = $3.6B, fair value de earnings = $19.3B, value of growth = $25.4B. ¿Cuánto implican las sinergias pagadas?",
        "options": [
            "A) $0B — el precio se explica completamente con book value, earnings y crecimiento",
            "B) $8.7B — la diferencia entre el precio y el valor standalone de Gillette",
            "C) $14.1B — la diferencia entre precio y book value",
            "D) $25.4B — todo el crecimiento es en realidad sinergia",
        ],
        "answer": "B",
        "explanation": "Standalone value de Gillette = 3.6 + 19.3 + 25.4 = $48.3B (que era el precio de mercado previo). PG pagó $57B → sinergias implícitas = 57 − 48.3 = $8.7B. Esta es la única parte verdaderamente 'incremental' que PG puede capturar que otros compradores no podrían — y debería justificarse explícitamente en el due diligence.",
    },
    "numerical_problem": {
        "question": "Una empresa target tiene NOA = $500M, OI = $60M, y el required return es r = 10%. ¿Cuánto vale el componente 'fair value of earnings' según Oh & Penman (2024)?",
        "steps": [
            "Fair value of earnings = (OI − r·NOA) / r",
            "= (60 − 0.10×500) / 0.10",
            "= (60 − 50) / 0.10",
            "= 10 / 0.10 = $100M",
        ],
        "answer": "$100M de valor adicionado por los earnings sobre el book value",
        "bus_hint": "RI = OI − r·NOA = 60 − 50 = 10 → capitalizado a 10% = 10/0.10 = 100",
    },
    "true_false": {
        "statement": "En el framework de Oh & Penman (2024), el goodwill GAAP actual y el goodwill propuesto son prácticamente iguales en todos los casos, con diferencias menores al 5%.",
        "answer": False,
        "explanation": "La tabla empírica del paper muestra diferencias enormes. Por ejemplo, Anadarko/Western Gas: GAAP goodwill = $104M vs. propuesto = $3,051M. Danaher/Beckman: GAAP = $3,746M vs. propuesto = $1,307M. Las diferencias surgen porque el GAAP asigna valor a activos individuales identificados (fair value adjustments) mientras que el modelo propuesto lo captura por la capacidad de generación de earnings conjunta. Para 8 de 12 ejemplos, el propuesto es mayor — sugiriendo que el GAAP subestima el valor de los earnings conjuntos.",
    },
    "fill_blank": {
        "template": "Oh & Penman critican el goodwill GAAP como un '_______ ' al precio de compra, sin identificar qué está siendo comprado — haciendo que la impairment posterior sea ambigua porque no se sabe qué ha sido deteriorado.",
        "answers": ["plug", "residuo", "saldo de cierre", "número residual"],
    },
    "connections": ["Residual Income Model — Ohlson (1995)", "Shaffer (2024) — multiples en M&A", "Goodwill impairment — ASC 350", "Penman & Zhang (2020) — contabilidad conservadora y riesgo"],
},

{
    "id": "eq_gw_002",
    "domain": "Equity Investing",
    "topic": "Valoración M&A — Goodwill e Incertidumbre Contable",
    "difficulty": "Advanced",
    "mode_tags": ["bus", "home"],
    "source": "Oh, H.I. & Penman, S. (2024) — 'A Proposal for Goodwill Accounting', KAIST / Columbia Business School",
    "front": "¿Por qué Oh & Penman (2024) argumentan que el 'value of combination' (sinergias) de una adquisición tipo Merck/Prometheus Biosciences debería posiblemente NO capitalizarse en balance, y qué principio contable subyace?",
    "back": "Principio de contabilización bajo incertidumbre: un activo solo debe capitalizarse si existe 'probable future economic benefit'. En Prometheus Biosciences: revenue = $6.8M vs. R&D expense = $112.8M — la empresa reporta pérdidas operativas de $145.8M. El R&D interno no fue capitalizado por el target (por FASB/IASB bajo R&D expensing rule) porque la probabilidad de éxito no está demostrada. ¿Por qué debería el adquirente capitalizar ese mismo R&D implícito en el goodwill? El paper aplica el mismo principio de consistencia: si el activo no era capitalizable en el target, tampoco debería serlo en el adquirente como parte del goodwill — a menos que haya evidencia concreta (Phase 3 success, patente otorgada) que cambie la probabilidad.",
    "mcq": {
        "question": "Un CEO adquiere una biotech pre-revenue por $10B. Según el framework de Oh & Penman (2024) aplicando el principio de contabilización bajo incertidumbre, ¿cuál sería la acción más apropiada?",
        "options": [
            "A) Capitalizar los $10B como goodwill porque el precio de mercado refleja el valor",
            "B) Solo capitalizar el book value del target (~$0.7B) y expensear el resto porque el value of growth y sinergias son inciertos sin evidencia auditada de viabilidad",
            "C) Usar el fair value de todos los activos identificados (patentes, IP) según GAAP/IFRS como base",
            "D) Amortizar los $10B en 40 años como era práctica pre-SFAS 142",
        ],
        "answer": "B",
        "explanation": "Si el R&D del target no fue capitalizable bajo incertidumbre (FASB ASC 730), aplicar el mismo principio al adquirente implica no capitalizar el valor especulativo. El due diligence documenta cuánto del precio está en activos probados (book value + earnings realizados) vs. cuánto en apuestas futuras (growth + synergies). Ese segundo bloque puede no pasar el threshold de capitalización — igual que no pasa en el target. El paper señala: 'Why should in-process R&D be recorded on the acquirer's books when it is not booked in the target's accounts?'",
    },
    "true_false": {
        "statement": "Oh & Penman (2024) encuentran empíricamente que el goodwill propuesto predice mejor los futuros goodwill impairments bajo GAAP que el propio goodwill GAAP, controlando por múltiples factores.",
        "answer": True,
        "explanation": "En la muestra de 290 transacciones (2001-2015) con 69 impairments en los 3 años post-adquisición, el goodwill propuesto es estadísticamente significativo para predecir impairments. Crucialmente, dado el goodwill propuesto, el goodwill GAAP pierde poder predictivo — sugiriendo que el número propuesto captura mejor la sobrevaluación real de la adquisición que el 'plug' GAAP.",
    },
    "fill_blank": {
        "template": "Oh & Penman argumentan que el componente de 'value of combination' (sinergias) tiene una correlación _______ con el value of growth y el valor del book value + earnings, sugiriendo escepticismo sobre si las sinergias proclamadas en acquisitions realmente existen.",
        "answers": ["negativa", "negative", "inversa"],
    },
    "connections": ["R&D expensing — FASB ASC 730", "Goodwill impairment predictability", "Penman (2021) — contabilidad bajo incertidumbre", "Warren Buffett — crítica a sinergias optimistas"],
},

{
    "id": "eq_gw_003",
    "domain": "Equity Investing",
    "topic": "Valoración M&A — Goodwill como Herramienta de Due Diligence",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Oh, H.I. & Penman, S. (2024) — 'A Proposal for Goodwill Accounting', KAIST / Columbia Business School",
    "front": "¿Cómo la descomposición del precio de adquisición de Oh & Penman (2024) puede usarse ANTES del closing para evaluar si un deal tiene sentido económico?",
    "back": "La descomposición es calculable en tiempo real con datos auditados del target (balance + P&L) al momento del anuncio — antes de que el GAAP publique números post-adquisición. Preguntas que habilita: (1) ¿Estamos pagando demasiado por el crecimiento del target? (crítico en mercados 'hot' como 2021 donde $5.1T en deals con alto múltiplo). (2) ¿El value of combination (sinergias) está justificado dado el negocio combinado? (3) ¿El ratio revenue/R&D del target indica valor realizable o especulativo? El paper calcula los componentes para Microsoft/Activision ($68.7B): Book value $17.6B + earnings $24.4B + growth $4.0B + synergies $22.7B — exponiendo que MSFT pagó $22.7B en sinergias, la mayor parte del goodwill, para una empresa con growth modesto.",
    "mcq": {
        "question": "En el deal MSFT/Activision ($68.7B), el value of growth adquirido fue solo $4.0B mientras que las sinergias fueron $22.7B. ¿Qué implicación tiene esto para evaluar el deal?",
        "options": [
            "A) El deal es malo porque hay poco crecimiento orgánico en Activision",
            "B) MSFT está pagando principalmente por sinergias — que son el componente más incierto y más difícil de justificar — requiriendo un riguroso business case de integración",
            "C) Un alto componente de sinergias es señal positiva de que el deal creará valor para MSFT",
            "D) El GAAP reconocerá las sinergias como activos identificables, reduciendo el goodwill final",
        ],
        "answer": "B",
        "explanation": "Las sinergias son el componente MÁS incierto y el MÁS frecuentemente ilusorio (Buffett 1997). Si la mayoría del precio está en sinergias ($22.7B de $26.7B de goodwill total), el deal depende de que MSFT pueda materializar integraciones con Xbox, Game Pass, etc. que no están probadas. El framework de Oh & Penman permite cuantificar exactamente cuánto del precio depende de promesas vs. valor demostrado.",
    },
    "fill_blank": {
        "template": "La descomposición de Oh & Penman permite calcular el precio de adquisición con datos _______ al momento del anuncio, sin requerir las estimaciones de fair value de activos individuales que solo aparecen meses después en los estados financieros post-adquisición.",
        "answers": ["auditados", "públicos", "observables", "públicos y auditados"],
    },
    "graph_type": "pe_ratio_vs_growth",
    "connections": ["Purchase price allocation (PPA)", "Earnout structures en M&A", "Due diligence cuantitativo", "Microsoft/Activision deal analysis"],
},


# ════════════════════════════════════════════════════════════════
# EQUITY INVESTING — Aggelopoulos (2017)
# Understanding Bank Valuation: ECF and Residual Income
# Open Journal of Accounting, 6, 1-10
# ════════════════════════════════════════════════════════════════

{
    "id": "eq_bkv_001",
    "domain": "Equity Investing",
    "topic": "Valoración de Bancos — ECF vs. Residual Income: Equivalencia",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Aggelopoulos, E. (2017) — 'Understanding Bank Valuation: ECF and RI', Open Journal of Accounting 6:1-10. DOI: 10.4236/ojacct.2017.61001",
    "front": "¿Por qué en bancos se usa Equity Cash Flow (ECF) en lugar del Enterprise DCF estándar, y por qué ambos (ECF y Residual Income) producen el mismo valor según Aggelopoulos (2017)?",
    "back": "En bancos, la deuda (depósitos, fondos interbancarios) es un insumo operativo — no solo financiamiento. Separar 'operating cash flows' de 'financing cash flows' es imposible: el margen de intermediación ES el negocio. Por eso no se usa WACC ni EBITDA. Se usa ECF (dividendos + cambios en capital regulatorio = cash flow al accionista) descontado a ke (costo de equity vía CAPM). La equivalencia ECF = RI: ambos descontan el mismo flujo económico al accionista — ECF lo hace directamente en caja, RI lo hace como Equity(t-1) + PV(Net Income − ke·Equity(t-1)) = mismo resultado. En el ejemplo del paper: ambos producen Equity Value = 1,267 unidades monetarias.",
    "latex": r"V_{equity} = BV_0 + \sum_{t=1}^{T} \frac{NI_t - k_e \cdot BV_{t-1}}{(1+k_e)^t} + \frac{TV_{RI}}{(1+k_e)^T}",
    "intuition": "Valorar un banco con Enterprise DCF es como calcular el valor de un restaurante sin contar los ingresos por comida — solo la cocina. Los depósitos y el margen de interés son el negocio del banco, no su 'deuda'. El ECF mira directamente cuánto cash llega al accionista (dividendos reales o potenciales), y el Residual Income dice lo mismo en lenguaje contable: cuánto genera el banco por encima de lo que el accionista mínimamente exige.",
    "mcq": {
        "question": "En el ejemplo de Aggelopoulos (2017), el banco tiene equity inicial de 329 unidades. Con ECF descontado al 10% (ke CAPM), el equity value calculado es 1,267. ¿Qué implica un equity value ~4x el book value?",
        "options": [
            "A) El banco está sobrevalorado y debería cotizar near book value (P/B ≈ 1x)",
            "B) El banco genera residual income positivo sostenido — ROE > ke en cada período — creando valor sobre el capital invertido",
            "C) Los supuestos de la tasa de descuento son incorrectos porque el ke debería ser mayor para bancos",
            "D) El modelo comete un error al no incluir el valor de los depósitos como pasivos de mercado",
        ],
        "answer": "B",
        "explanation": "Un P/B > 1x implica ROE > ke: el banco gana más sobre su capital que lo que el accionista exige. En el ejemplo: Net Income ≈ 112 sobre equity inicial 329 → ROE ≈ 34% vs ke = 10%. El residual income es 112 − 0.10×329 = 79 por período — positivo y creciente. La diferencia entre equity value (1,267) y book value (329) = 938 = valor presente de todos los residual incomes futuros. Este es el 'franchise value' del banco.",
    },
    "true_false": {
        "statement": "Según Aggelopoulos (2017), para valorar bancos se puede usar el método Enterprise DCF con WACC porque los depósitos son financiamiento regular, similar a la deuda corporativa.",
        "answer": False,
        "explanation": "Incorrecto — es uno de los errores más comunes en bank valuation. Los depósitos son simultáneamente 'deuda' y 'activo operativo' del banco: generan margen de interés (NIM) y son la materia prima del negocio bancario. Separar el valor operativo del financiero es imposible. Por eso el método correcto es ECF (o RI) aplicado directamente al equity, no Enterprise DCF con WACC. Damodaran (2009) también lo señala explícitamente.",
    },
    "numerical_problem": {
        "question": "Un banco tiene Equity (inicio de año) = 329, Net Income = 112, ke = 10%. ¿Cuál es el Residual Income del año?",
        "steps": [
            "RI = Net Income − ke × Equity(inicio de año)",
            "= 112 − 0.10 × 329",
            "= 112 − 32.9 ≈ 79",
        ],
        "answer": "Residual Income ≈ 79 unidades monetarias",
        "bus_hint": "RI = 112 − 10%×329 = 112 − 33 ≈ 79",
    },
    "fill_blank": {
        "template": "En la valoración de bancos, el Equity Cash Flow se calcula como dividendos pagados (o potenciales) más/menos cambios en el _______ requerido, que en bancos está determinado por las reglas de capital de Basilea (Tier 1 sobre RWA).",
        "answers": ["capital regulatorio", "capital mínimo", "Tier 1 capital", "capital Basilea"],
    },
    "connections": ["Damodaran — Financial firm valuation", "P/Book ratio en banca", "CAPM para bancos — beta sectorial", "NIM (Net Interest Margin) como driver de valor"],
},

{
    "id": "eq_bkv_002",
    "domain": "Equity Investing",
    "topic": "Valoración de Bancos — Capital Regulatorio y Terminal Value",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Aggelopoulos, E. (2017) — 'Understanding Bank Valuation: ECF and RI', Open Journal of Accounting 6:1-10",
    "front": "¿Por qué el capital regulatorio de Basilea (Tier 1 / RWA) es el determinante central del equity proyectado en un modelo de valoración bancaria, y cómo afecta esto al ECF?",
    "back": "En un banco, el equity no crece libremente — está atado a los Risk-Weighted Assets (RWA) × mínimo de capital (8% Basilea + buffer). El modelo de Aggelopoulos usa 10% de RWA como equity requerido en cada año. Esto crea un 'equity constraint': si el banco necesita más capital para crecer (RWA sube), el ECF se reduce porque el exceso de utilidades debe retenerse en lugar de distribuirse. El ECF = Net Income − cambio en equity requerido = dividendos potenciales. Esta restricción es específica de bancos y no existe en corporaciones industriales, donde la política de dividendos es discrecional.",
    "mcq": {
        "question": "En el modelo del paper, si los préstamos del banco crecen al 3% anual y el ratio préstamos/RWA es 75%, ¿cuál es el efecto principal sobre el ECF en años de alto crecimiento de loans?",
        "options": [
            "A) El ECF sube porque los préstamos generan más Net Interest Income",
            "B) El ECF puede caer porque el mayor RWA requiere más capital retenido, reduciendo los dividendos potenciales a pesar de mayor utilidad",
            "C) El ECF no se ve afectado porque el capital regulatorio es fijo en el tiempo",
            "D) El ECF sube siempre que el NIM (Net Interest Margin) sea positivo",
        ],
        "answer": "B",
        "explanation": "Este es el trade-off central en bank valuation: crecer requiere más capital regulatorio (10% de RWA en el modelo). Si el banco gana 112 de Net Income pero necesita retener 9 adicionales para capitalizar el crecimiento de préstamos, el ECF disponible es 103 — no 112. El growth 'consume' equity. Es por esto que bancos con alto crecimiento de crédito no necesariamente generan más ECF, y por qué el modelo de Aggelopoulos produce ECF que crece más lento que el Net Income en los primeros años.",
    },
    "true_false": {
        "statement": "En la valoración de bancos con el modelo ECF, el terminal value se calcula dividiendo el Net Income del año terminal entre el costo de equity — análogo al Gordon Growth Model con g=0.",
        "answer": True,
        "explanation": "Correcto: TV = NI_terminal / ke (con g=0 implícito). En el ejemplo: TV = 142 / 0.10 = 1,420 unidades. Esto equivale a asumir que el banco genera el mismo nivel de utilidad neta a perpetuidad sin crecimiento adicional — un supuesto conservador pero comúnmente usado para el período post-analítico. Para el modelo de RI, el TV se calcula análogamente: TV_RI = RI_terminal / ke = 101 / 0.10 = 1,010, y el valor total incluye el book value inicial + PV(RI) + PV(TV_RI).",
    },
    "fill_blank": {
        "template": "El Equity Cash Flow de un banco se puede calcular también como dividendos pagados más/menos _______ de capital (recompras de acciones son outflows, emisiones son inflows), siendo este el método de verificación alternativo de Koller, Goedhart & Wessels (2005).",
        "answers": ["cambios en el", "variaciones en", "movimientos de"],
    },
    "connections": ["Basilea III — capital requirements", "Gordon Growth Model — terminal value", "ROE vs. ke como driver de P/Book", "Stress testing bancario — ECF bajo escenarios"],
},


# ════════════════════════════════════════════════════════════════
# EQUITY INVESTING — Penman (1997)
# A Synthesis of Equity Valuation Techniques and the
# Terminal Value Calculation for the Dividend Discount Model
# UC Berkeley — Review of Accounting Studies 2:303-323
# ════════════════════════════════════════════════════════════════

{
    "id": "eq_tv_001",
    "domain": "Equity Investing",
    "topic": "Valoración — DDM, DCF y Residual Income: Equivalencia y Terminal Value",
    "difficulty": "Advanced",
    "mode_tags": ["bus", "home"],
    "source": "Penman, S.H. (1997) — 'A Synthesis of Equity Valuation Techniques and the Terminal Value Calculation for the DDM', UC Berkeley. Review of Accounting Studies 2:303-323",
    "front": "¿Cuál es el hallazgo central de Penman (1997) sobre la relación entre DDM, DCF y Residual Income (RI), y qué implica para el analista que elige entre estos modelos?",
    "back": "Con horizonte infinito, todos los modelos (DDM, DCF, RI) convergen al mismo valor — son matemáticamente equivalentes bajo clean-surplus accounting. La diferencia real está en el horizonte finito: cuando se trunca la proyección a T años, se introduce un error que depende del modelo usado y del accounting del terminal year. El insight clave: los modelos alternativos al DDM (DCF, RI) no son superiores per se — son formas de CALCULAR EL TERMINAL VALUE implícito del DDM. El RI model produce menor error de terminal value que el DCF cuando los activos operativos tendrán valor más allá del horizonte — porque el RI descontará ese valor vía el book value residual, mientras que el DCF asume liquidación.",
    "latex": r"P_t = B_t + \sum_{\tau=1}^{T} \frac{X^a_{t+\tau}}{(1+r)^\tau} + \underbrace{\frac{P_{t+T} - B_{t+T}}{(1+r)^T}}_{\text{error terminal}}",
    "intuition": "Es como navegar a una isla: el DDM dice 'sigue el barco hasta la isla' pero el barco (los dividendos) zigzaguea. El DCF dice 'sigue el viento' (free cash flow) — más directo pero depende de que no haya viento cruzado después del horizonte. El RI dice 'sigue el mapa' (el book value acumulado) — más robusto porque el mapa persiste más allá del horizonte visible. Todos llegan a la misma isla si navegas suficientemente lejos, pero con horizontes finitos el mapa (RI) comete menos error.",
    "mcq": {
        "question": "Penman (1997) muestra que el error de terminal value en el modelo DCF es igual a la ____ proyectada de los activos operativos al horizonte T. ¿Cuál es la implicación práctica?",
        "options": [
            "A) Valor de mercado de los activos operativos — el DCF es perfecto si el mercado es eficiente",
            "B) Valor presente de los activos operativos (OA_T) al horizonte — el DCF comete gran error cuando hay activos operativos sustanciales en T (no liquidados)",
            "C) Valor de la deuda neta al horizonte — por eso el DCF funciona mejor para empresas sin deuda",
            "D) Suma de los dividendos esperados post-horizonte — equivalente al error del DDM",
        ],
        "answer": "B",
        "explanation": "El error del DCF = PV(OA_{t+T}): el DCF implícitamente asume que todos los activos operativos se habrán liquidado en activos financieros (net debt = 0) al horizonte T. Para una empresa manufacturera con plantas y equipos vigentes en año T, este error es enorme. El RI model tiene error = PV(P_{t+T} − B_{t+T}) — el premium de mercado sobre book value al horizonte, que es pequeño si B_{t+T} es una buena aproximación del valor. Por eso el RI es más robusto para empresas con activos de larga vida.",
    },
    "true_false": {
        "statement": "Según Penman (1997), el modelo DCF es preferible al Residual Income para valorar empresas de capital intensivo (manufactura, infraestructura) con activos de larga vida, porque el DCF no depende de los principios de accrual accounting.",
        "answer": False,
        "explanation": "Al contrario: el DCF tiene mayor error de terminal value para empresas con activos operativos sustanciales al horizonte, precisamente porque asume implícitamente que esos activos se han liquidado. El RI model comete menor error porque usa el book value contable como 'ancla' — y si la accounting es conservadora, el premium P_{t+T}−B_{t+T} es capturado por los residual incomes futuros. Penman (1997) es explícito: para empresas de capital intensivo, el RI es más robusto que el DCF.",
    },
    "fill_blank": {
        "template": "Penman (1997) demuestra que el Residual Income model y el DDM son equivalentes, y que la diferencia entre usar RI vs. DDM es simplemente una diferente especificación del _______ del modelo de descuento de dividendos.",
        "answers": ["terminal value", "valor terminal", "continuing value", "valor residual"],
    },
    "connections": ["Ohlson (1995) — RI model", "Feltham & Ohlson (1995) — accrual accounting en valuación", "DCF vs. RI para terminal value", "Penman & Sougiannis (1998) — comparación empírica de modelos"],
},

{
    "id": "eq_tv_002",
    "domain": "Equity Investing",
    "topic": "Valoración — Terminal Value: Errores Comunes y el Rol del Accounting",
    "difficulty": "Intermediate",
    "mode_tags": ["bus", "home"],
    "source": "Penman, S.H. (1997) — 'A Synthesis of Equity Valuation Techniques', UC Berkeley / Review of Accounting Studies",
    "front": "¿Por qué Penman (1997) afirma que el problema del terminal value es fundamentalmente un problema de ACCOUNTING, no de finanzas, y qué implica esto para el analista?",
    "back": "El error de terminal value surge de truncar el horizonte de proyección. Ese error depende de qué tan bien el accounting 'captura' el valor acumulado hasta T: si el balance sheet (Bt+T) refleja fielmente el valor económico de los activos al horizonte, el error P_{t+T} − B_{t+T} es pequeño y no se necesita una TV sofisticada. El problema es que diferentes principios contables (conservatismo, capitalización vs. expensing de intangibles) crean gaps diferentes entre P y B. Por tanto, la elección de accounting para el pro-forma (ej. capitalizar R&D o no, usar IFRS vs. GAAP) determina directamente la precisión del terminal value. No es un problema de modelos financieros sino de cómo se miden los activos.",
    "mcq": {
        "question": "Si un analista proyecta el pro-forma con accounting conservador (expensea R&D, no capitaliza brand investments), ¿cuál es el efecto sobre el error del terminal value según Penman (1997)?",
        "options": [
            "A) El error aumenta porque el book value es menor que el valor económico, creando un gap mayor P_{T}−B_{T}",
            "B) El error disminuye porque el conservatismo captura el riesgo correctamente",
            "C) No hay efecto — el terminal value error depende solo de la tasa de descuento",
            "D) El error disminuye porque el DCF compensa automáticamente los bajos book values",
        ],
        "answer": "A",
        "explanation": "Con accounting conservador, B_{t+T} subestima el valor económico → P_{t+T} > B_{t+T} es más grande → el error de terminal value es mayor. Esto parece paradójico pero es la esencia del paper: el conservatismo accounting 'desplaza' valor hacia los residual incomes futuros (que el analista sí proyecta), pero si el horizonte T es corto, ese valor no alcanza a ser capturado. Solución: alargar el horizonte de proyección explícita para reducir el error, o usar una TV que reconozca el premium P−B residual.",
    },
    "true_false": {
        "statement": "Penman (1997) demuestra que el Residual Income model produce valuaciones idénticas al DCF cuando se aplican durante horizontes infinitos con clean-surplus accounting.",
        "answer": True,
        "explanation": "Sí — es el resultado fundamental del paper. Con T → ∞ y clean-surplus (Xt = Bt − Bt-1 + dt, sin violaciones), ambos modelos convergen al mismo Pt. La divergencia ocurre SOLO para horizontes finitos, donde el error de terminal value difiere según qué activos quedan sin liquidar al horizonte T. Este resultado es la base para entender por qué practitioners usan indistintamente DCF y RI — son el mismo modelo con diferente 'packaging' del terminal value.",
    },
    "numerical_problem": {
        "question": "Una empresa tiene Book Value = $100, residual income perpetuo esperado = $10/año, ke = 10%. ¿Cuál es el Equity Value bajo el RI model sin crecimiento?",
        "steps": [
            "Equity Value = BV + PV(RI a perpetuidad)",
            "PV(RI) = RI / ke = 10 / 0.10 = $100",
            "Equity Value = 100 + 100 = $200",
            "P/B = 200/100 = 2x (ROE = 20% > ke = 10%)",
        ],
        "answer": "$200 (P/B = 2x)",
        "bus_hint": "BV = 100 | RI/ke = 10/0.10 = 100 | Total = 200 | P/B = 2x porque ROE (20%) > ke (10%)",
    },
    "fill_blank": {
        "template": "Penman (1997) demuestra que el terminal value en el DDM puede calcularse como el _______ esperado al horizonte T dividido entre la tasa de descuento — que es equivalente a capitalizar el residual income como perpetuidad cuando no hay crecimiento adicional.",
        "answers": ["residual income", "abnormal earnings", "earnings residuales", "RI"],
    },
    "connections": ["Gordon Growth Model — TV simplificado", "Ohlson (1995) — pricing model", "Penman & Sougiannis (1998) — comparación empírica RI vs DCF", "Clean Surplus Relation (CSR)"],
},

{
    "id": "eq_tv_003",
    "domain": "Equity Investing",
    "topic": "Valoración — Cuando No Se Necesita Terminal Value",
    "difficulty": "Advanced",
    "mode_tags": ["home"],
    "source": "Penman, S.H. (1997) — 'A Synthesis of Equity Valuation Techniques', UC Berkeley / Review of Accounting Studies",
    "front": "¿Bajo qué condición de accounting el RI model NO requiere terminal value (TV = 0), y por qué esto es prácticamente imposible pero teóricamente importante?",
    "back": "El RI model requiere TV = 0 si y solo si el residual income esperado post-horizonte es CERO, es decir, P_{t+T} = B_{t+T}: el book value equivale exactamente al precio de mercado al horizonte. Esto ocurre solo si el accounting es 'ideal' — todos los activos están al fair value continuamente (mark-to-market completo). Teóricamente importante porque: (1) identifica que el TV es una corrección de los errores de accounting del pro-forma, no una pieza separada del modelo. (2) muestra que el TV necesario es más pequeño cuando el accounting es más informativo (mejor aproximación del valor económico). (3) implica que mejorar el pro-forma accounting reduce más el error que sofisticar la fórmula del TV.",
    "fill_blank": {
        "template": "El error de terminal value en el RI model es _______ cuando el book value proyectado al horizonte T equivale exactamente al precio de mercado esperado en ese período.",
        "answers": ["cero", "zero", "nulo", "inexistente"],
    },
    "true_false": {
        "statement": "Penman (1997) muestra que el modelo de 'capitalized earnings' (Vt = Bt + capitalized residual income) converge al mismo valor que el DDM solo si se usa un capitalization factor específico que depende del horizonte T.",
        "answer": True,
        "explanation": "El modelo de capitalized earnings usa el factor (ρ^T − 1)^−1 × suma_ponderada(RI) — no el simple 1/ke. Este factor difiere de 1/ke para horizontes finitos, y converge a 1/ke solo cuando T → ∞. Para T finito, usar 1/ke como si fuera una perpetuidad introduce un error sistemático. Penman (1997) formaliza exactamente cómo esta diferencia mapea al terminal value del DDM — demostrando que el modelo de capitalized earnings es una forma particular de especificar ese terminal value.",
    },
    "connections": ["Mark-to-market accounting — IFRS 9/13", "Ideal vs. historical cost accounting", "Penman — Financial Statement Analysis and Security Valuation", "Fair value hierarchy — Level 1/2/3"],
},

]


def get_all_cards() -> list[dict]:
    """Returns all curated + user-added cards."""
    from core.store import CardStore
    store      = CardStore()
    user_cards = store.all_user_cards()
    return INVEST_CARDS + user_cards


def get_bus_cards() -> list[dict]:
    return [c for c in get_all_cards() if "bus" in c.get("mode_tags", [])]


def get_cards_by_domain(domain: str) -> list[dict]:
    return [c for c in get_all_cards() if c.get("domain") == domain]


DOMAINS = [
    "Equity Investing",
    "Fixed Income",
    "Alternatives",
    "Thematic Investing",
    "ESG",
    "Asset Allocation",
    "Trading Strategy",
    "Derivatives",
    "Real Assets",
    "Risk Management",
    "Macroeconomics",
]
