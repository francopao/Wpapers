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
]
