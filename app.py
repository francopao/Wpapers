"""
INVEST MEMORIA — v1.0
=====================
Plataforma de aprendizaje activo para analistas de inversiones.
7 dominios: Equity | Fixed Income | Alternatives | Thematic | ESG | Asset Allocation | Trading
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
import random
import json
import math
import numpy as np
from datetime import datetime
from pathlib import Path

from core.srs_engine import SRSEngine, Rating, CardState
from core.store import CardStore
from content.invest_cards import get_all_cards, get_bus_cards, get_cards_by_domain, DOMAINS
from utils.analytics import AnalyticsEngine

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Invest Memoria",
    page_icon="∂",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS — Mobile-first dark theme ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600&family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    background-color: #070b14 !important;
    color: #dde3ee !important;
    font-family: 'Inter', sans-serif !important;
}
.stApp { background-color: #070b14 !important; }
section[data-testid="stSidebar"] {
    background: #0a0f1e !important;
    border-right: 1px solid #1a2540;
}
div[data-testid="metric-container"] {
    background: #0e1526;
    border: 1px solid #1a2540;
    border-radius: 10px;
    padding: 14px;
}
.stButton > button {
    background: #0e1526 !important;
    color: #60a5fa !important;
    border: 1px solid #1e3a6e !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    transition: all 0.15s ease !important;
}
.stButton > button:hover {
    background: #1a2e50 !important;
    border-color: #3b82f6 !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #1d4ed8, #2563eb) !important;
    color: #fff !important;
    border: none !important;
    font-weight: 600 !important;
}
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: #0e1526 !important;
    color: #dde3ee !important;
    border: 1px solid #1a2540 !important;
    border-radius: 8px !important;
}
.stTabs [data-baseweb="tab"] {
    background: #0e1526 !important;
    color: #64748b !important;
    border-radius: 8px 8px 0 0 !important;
    font-size: 13px !important;
}
.stTabs [aria-selected="true"] {
    color: #60a5fa !important;
    border-bottom: 2px solid #3b82f6 !important;
}
code, pre { background: #0a0f1e !important; color: #34d399 !important; border-radius: 6px; }
hr { border-color: #1a2540 !important; }

/* ── Card components ── */
.card-q {
    background: #0e1526;
    border: 1px solid #1a2540;
    border-left: 4px solid #3b82f6;
    border-radius: 12px;
    padding: 20px 24px;
    margin: 10px 0;
    font-size: 15px;
    line-height: 1.8;
}
.card-a {
    background: #0c1a0e;
    border: 1px solid #1a3d22;
    border-left: 4px solid #34d399;
    border-radius: 12px;
    padding: 20px 24px;
    margin: 10px 0;
    font-size: 14px;
    line-height: 1.8;
}
.card-numeric {
    background: #12100a;
    border: 1px solid #3d2e0a;
    border-left: 4px solid #f59e0b;
    border-radius: 12px;
    padding: 18px 22px;
    margin: 10px 0;
    font-size: 13px;
    line-height: 1.8;
    font-family: 'JetBrains Mono', monospace;
}
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
    margin: 2px 3px;
    border: 1px solid rgba(255,255,255,0.1);
}
.title-main {
    font-family: 'JetBrains Mono', monospace;
    font-size: 22px;
    font-weight: 700;
    color: #60a5fa;
    letter-spacing: -0.5px;
}
.title-sub {
    font-size: 12px;
    color: #475569;
    margin-bottom: 20px;
}
.mcq-opt {
    background: #0e1526;
    border: 1px solid #1a2540;
    border-radius: 8px;
    padding: 11px 16px;
    margin: 5px 0;
    font-size: 14px;
}
.mcq-ok  { border-color: #34d399 !important; background: #071a0e !important; color: #34d399; }
.mcq-err { border-color: #f87171 !important; background: #1a0707 !important; color: #f87171; }
.prog-bg { background: #1a2540; border-radius: 6px; height: 5px; margin-bottom: 18px; }
.hint-box {
    background: #12100a;
    border: 1px solid #3d2e0a;
    border-radius: 8px;
    padding: 12px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #fbbf24;
    margin: 8px 0;
}
.domain-pill {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin: 2px;
}
</style>
""", unsafe_allow_html=True)


# ── Session state ──────────────────────────────────────────────────────────────
def init():
    defs = {
        "page": "Dashboard",
        "queue": [], "q_idx": 0,
        "revealed": False,
        "q_domain": "All",
        "q_type": "Flashcard",
        "mcq_answered": None,
        "tf_answered": None,
        "fill_submitted": False,
        "fill_input": "",
        "session_total": 0,
        "session_correct": 0,
        "idea_search": "",
    }
    for k, v in defs.items():
        if k not in st.session_state:
            st.session_state[k] = v

init()

store     = CardStore()
engine    = SRSEngine()
analytics = AnalyticsEngine()
ALL_CARDS = get_all_cards()
ALL_DOMAINS = ["All"] + DOMAINS


# ── Domain color map ───────────────────────────────────────────────────────────
DOMAIN_COLORS = {
    "Equity Investing":   "#818cf8",
    "Fixed Income":       "#38bdf8",
    "Alternatives":       "#a78bfa",
    "Thematic Investing": "#f59e0b",
    "ESG":                "#34d399",
    "Asset Allocation":   "#fb923c",
    "Trading Strategy":   "#f87171",
    "Derivatives":        "#e879f9",
    "Real Assets":        "#4ade80",
    "Risk Management":    "#fb7185",
    "Macroeconomics":     "#fde68a",
}
DIFF_COLORS = {
    "Foundational":  "#34d399",
    "Intermediate":  "#60a5fa",
    "Advanced":      "#f59e0b",
    "Expert":        "#f87171",
}


# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="padding:10px 0 18px 0;">
      <div style="font-family:'JetBrains Mono',monospace;font-size:18px;
                  font-weight:700;color:#60a5fa;">∂ INVEST MEMORIA</div>
      <div style="font-size:11px;color:#475569;margin-top:3px;">AFP · Investment Research</div>
    </div>
    """, unsafe_allow_html=True)

    pages = {
        "📊 Dashboard":    "Dashboard",
        "🚌 Modo Bus":     "Bus",
        "🏠 Modo Profundo":"Deep",
        "💡 Modo Idea":    "Idea",
        "📚 Biblioteca":   "Library",
        "📈 Analytics":    "Analytics",
        "➕ Nueva Carta":  "AddCard",
    }
    for label, key in pages.items():
        is_active = st.session_state.page == key
        if st.button(label, use_container_width=True,
                     type="primary" if is_active else "secondary"):
            st.session_state.page = key
            st.session_state.queue = []
            st.session_state.q_idx = 0
            st.session_state.revealed = False
            st.rerun()

    st.divider()

    states = store.all_states()
    due_count = sum(
        1 for c in ALL_CARDS
        if engine.is_due(states.get(c["id"], CardState(card_id=c["id"])))
    )
    streak = store.streak_days()

    st.markdown(f"""
    <div style="text-align:center;padding:4px 0;">
      <div style="font-size:26px;color:#60a5fa;font-family:'JetBrains Mono',monospace;
                  font-weight:700;">{due_count}</div>
      <div style="font-size:11px;color:#475569;">para revisar hoy</div>
    </div>
    <div style="text-align:center;padding:4px 0;">
      <div style="font-size:20px;color:#f59e0b;font-family:'JetBrains Mono',monospace;">
        🔥 {streak}d</div>
      <div style="font-size:11px;color:#475569;">racha activa</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    # Domain mini-legend
    for dom, col in DOMAIN_COLORS.items():
        abbrev = dom[:3].upper()
        count  = sum(1 for c in ALL_CARDS if c.get("domain") == dom)
        st.markdown(
            f'<div style="display:flex;justify-content:space-between;font-size:11px;'
            f'padding:2px 0;"><span style="color:{col};">{dom[:16]}</span>'
            f'<span style="color:#475569;">{count}</span></div>',
            unsafe_allow_html=True
        )


# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def mastery_color(pct):
    if pct < 33: return "#f87171"
    if pct < 66: return "#f59e0b"
    return "#34d399"

def render_tags(card):
    dom   = card.get("domain", "")
    diff  = card.get("difficulty", "")
    topic = card.get("topic", "")
    dc    = DOMAIN_COLORS.get(dom, "#64748b")
    dfc   = DIFF_COLORS.get(diff, "#64748b")
    modes = card.get("mode_tags", [])
    mode_badge = "🚌🏠" if "bus" in modes and "home" in modes else ("🚌" if "bus" in modes else "🏠")
    st.markdown(
        f'<span class="badge" style="color:{dc};border-color:{dc}30;">{dom}</span>'
        f'<span class="badge" style="color:#94a3b8;">{topic[:30]}</span>'
        f'<span class="badge" style="color:{dfc};">{diff}</span>'
        f'<span class="badge" style="color:#06b6d4;">{mode_badge}</span>',
        unsafe_allow_html=True
    )

def render_graph(card):
    gtype = card.get("graph_type", "")
    if not gtype:
        return
    try:
        import plotly.graph_objects as go

        LAYOUT = dict(
            paper_bgcolor="#070b14", plot_bgcolor="#070b14",
            font=dict(color="#94a3b8", size=11, family="Inter"),
            margin=dict(l=10, r=10, t=35, b=10),
            height=300,
            xaxis=dict(gridcolor="#1a2540", zeroline=False, showline=False),
            yaxis=dict(gridcolor="#1a2540", zeroline=False, showline=False),
        )
        COLORS = ["#60a5fa", "#34d399", "#f59e0b", "#f87171", "#a78bfa", "#38bdf8", "#fb923c"]

        # ── Price-Yield with Convexity ─────────────────────────────────────
        if gtype == "price_yield_convexity":
            yields = np.linspace(0.01, 0.15, 100)
            coupon, par, n = 0.06, 100, 20
            prices_bullet = [
                sum(coupon * par / (1+y)**t for t in range(1, n+1)) + par / (1+y)**n
                for y in yields
            ]
            # Callable: capped at ~110 when yields low (call price)
            prices_callable = [min(p, 108 - 30 * max(0, 0.07 - y)) for p, y in zip(prices_bullet, yields)]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=yields*100, y=prices_bullet, name="Bono Bullet",
                line=dict(color=COLORS[0], width=2.5)))
            fig.add_trace(go.Scatter(x=yields*100, y=prices_callable, name="Bono Callable",
                line=dict(color=COLORS[2], width=2.5, dash="dash")))
            # Tangent at 6%
            y0_idx = np.argmin(np.abs(yields - 0.06))
            p0 = prices_bullet[y0_idx]
            slope = (prices_bullet[y0_idx+2] - prices_bullet[y0_idx-2]) / (yields[y0_idx+2] - yields[y0_idx-2])
            tangent_y = [p0 + slope * (y - 0.06) * 100 for y in yields]
            fig.add_trace(go.Scatter(x=yields*100, y=tangent_y, name="Aprox. Duración (lineal)",
                line=dict(color="#f87171", width=1.5, dash="dot")))
            fig.update_layout(**LAYOUT, title="Precio vs. Yield — Convexidad y Callable")
            fig.update_xaxes(title="Yield (%)")
            fig.update_yaxes(title="Precio")
            st.plotly_chart(fig, use_container_width=True)

        # ── Yield Curve Shapes ─────────────────────────────────────────────
        elif gtype == "yield_curve_shapes":
            mats = [0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30]
            curves = {
                "Normal (upward)":   [3.0, 3.2, 3.5, 3.9, 4.1, 4.4, 4.6, 4.8, 5.0, 5.1],
                "Invertida":         [5.3, 5.2, 5.0, 4.6, 4.3, 4.0, 3.8, 3.6, 3.5, 3.4],
                "Flat":              [4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2],
                "Humped (2y peak)":  [3.5, 3.8, 4.2, 4.8, 4.6, 4.3, 4.1, 3.9, 3.7, 3.6],
            }
            fig = go.Figure()
            for (name, vals), col in zip(curves.items(), COLORS):
                fig.add_trace(go.Scatter(x=mats, y=vals, name=name,
                    line=dict(color=col, width=2.2)))
            fig.update_layout(**LAYOUT, title="Formas de la Curva de Rendimientos")
            fig.update_xaxes(title="Vencimiento (años)")
            fig.update_yaxes(title="Yield (%)")
            st.plotly_chart(fig, use_container_width=True)

        # ── PE J-Curve ─────────────────────────────────────────────────────
        elif gtype == "pe_cashflow_j_curve":
            years = list(range(0, 12))
            # Capital calls (negative), distributions (positive)
            calls  = [-20, -25, -20, -15, -10, 0, 0, 0, 0, 0, 0, 0]
            distrib = [0, 0, 0, 5, 15, 30, 45, 50, 35, 20, 10, 5]
            cumul  = []
            s = 0
            for c, d in zip(calls, distrib):
                s += c + d
                cumul.append(s)
            fig = go.Figure()
            fig.add_trace(go.Bar(x=years, y=calls, name="Capital Calls", marker_color="#f87171"))
            fig.add_trace(go.Bar(x=years, y=distrib, name="Distribuciones", marker_color="#34d399"))
            fig.add_trace(go.Scatter(x=years, y=cumul, name="NAV Neto Acumulado",
                line=dict(color=COLORS[0], width=2.5), mode="lines+markers"))
            fig.add_hline(y=0, line_color="#475569", line_dash="dot")
            fig.update_layout(**LAYOUT, title="J-Curve — Fondo Private Equity Típico",
                barmode="relative")
            fig.update_xaxes(title="Año del Fondo")
            fig.update_yaxes(title="USD millones")
            st.plotly_chart(fig, use_container_width=True)

        # ── Risk Parity Contributions ──────────────────────────────────────
        elif gtype == "risk_parity_contributions":
            categories = ["Equity", "Bonds", "Cmdties", "Real Est"]
            contrib_6040 = [89, 8, 2, 1]
            contrib_rp   = [25, 25, 25, 25]
            fig = go.Figure()
            fig.add_trace(go.Bar(name="60/40 Tradicional", x=categories, y=contrib_6040,
                marker_color="#f87171"))
            fig.add_trace(go.Bar(name="Risk Parity", x=categories, y=contrib_rp,
                marker_color="#34d399"))
            fig.update_layout(**LAYOUT, title="Contribución al Riesgo (%)", barmode="group")
            fig.update_yaxes(title="% del riesgo total")
            st.plotly_chart(fig, use_container_width=True)

        # ── Efficient Frontier ─────────────────────────────────────────────
        elif gtype == "efficient_frontier_bl":
            np.random.seed(42)
            rets, vols, sharpes = [], [], []
            for _ in range(3000):
                w = np.random.dirichlet(np.ones(5))
                mu_v = np.array([0.08, 0.05, 0.12, 0.07, 0.10])
                cov_m = np.array([
                    [0.04, 0.01, 0.02, 0.005, 0.01],
                    [0.01, 0.01, 0.005, 0.002, 0.004],
                    [0.02, 0.005, 0.09, 0.01, 0.015],
                    [0.005, 0.002, 0.01, 0.025, 0.006],
                    [0.01, 0.004, 0.015, 0.006, 0.04],
                ])
                r = float(w @ mu_v)
                v = float(math.sqrt(w @ cov_m @ w))
                rets.append(r * 100); vols.append(v * 100)
                sharpes.append(r / v)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=vols, y=rets, mode="markers",
                marker=dict(color=sharpes, colorscale="Plasma", size=3, opacity=0.5,
                    colorbar=dict(title="Sharpe", thickness=12)),
                name="Portafolios simulados"))
            fig.update_layout(**LAYOUT, title="Frontera Eficiente — 5 Clases de Activo")
            fig.update_xaxes(title="Volatilidad (%)")
            fig.update_yaxes(title="Retorno esperado (%)")
            st.plotly_chart(fig, use_container_width=True)

        # ── Momentum Decile Returns ────────────────────────────────────────
        elif gtype == "momentum_decile_returns":
            deciles = [f"D{i}" for i in range(1, 11)]
            returns = [-4.2, -2.1, -0.8, 0.2, 0.9, 1.4, 2.0, 2.8, 3.9, 6.1]
            colors_bar = [COLORS[3] if r < 0 else COLORS[0] for r in returns]
            fig = go.Figure(go.Bar(x=deciles, y=returns, marker_color=colors_bar))
            fig.add_annotation(x="D1", y=-4.2, text="Perdedores", showarrow=False,
                font=dict(color="#f87171", size=10), yshift=-18)
            fig.add_annotation(x="D10", y=6.1, text="Ganadores", showarrow=False,
                font=dict(color="#60a5fa", size=10), yshift=12)
            fig.update_layout(**LAYOUT, title="Retornos por Decil — Momentum (12-1 meses)")
            fig.update_yaxes(title="Retorno mensual promedio (%)")
            st.plotly_chart(fig, use_container_width=True)

        # ── Gordon Growth Sensitivity ──────────────────────────────────────
        elif gtype == "gordon_sensitivity":
            g_range = np.linspace(0.01, 0.09, 50)
            r_vals  = [0.09, 0.10, 0.12]
            D1 = 2.10
            fig = go.Figure()
            for r, col in zip(r_vals, COLORS):
                prices = [D1 / (r - g) if r > g else None for g in g_range]
                valid = [(g, p) for g, p in zip(g_range, prices) if p is not None and p < 200]
                if valid:
                    gs, ps = zip(*valid)
                    fig.add_trace(go.Scatter(x=[g*100 for g in gs], y=list(ps),
                        name=f"r={r*100:.0f}%", line=dict(color=col, width=2.2)))
            fig.update_layout(**LAYOUT, title="Gordon Growth — Sensibilidad Precio vs. g (D₁=$2.10)")
            fig.update_xaxes(title="Tasa de crecimiento g (%)")
            fig.update_yaxes(title="Precio ($)", range=[0, 200])
            st.plotly_chart(fig, use_container_width=True)

        # ── AI Value Chain ─────────────────────────────────────────────────
        elif gtype == "ai_value_chain":
            layers = ["Infraestructura\n(Chips, Cloud, Energía)",
                      "Modelos\n(LLMs, Foundation)",
                      "Aplicaciones\n(SaaS vertical, Herramientas)"]
            capture_now = [70, 20, 10]
            capture_lt  = [30, 25, 45]
            fig = go.Figure()
            fig.add_trace(go.Bar(name="Captura de valor HOY", x=layers, y=capture_now,
                marker_color="#f59e0b"))
            fig.add_trace(go.Bar(name="Captura de valor LT (estimado)", x=layers, y=capture_lt,
                marker_color="#60a5fa"))
            fig.update_layout(**LAYOUT, title="Cadena de Valor IA — Distribución de Valor (%)",
                barmode="group")
            fig.update_yaxes(title="% captura de valor estimado")
            st.plotly_chart(fig, use_container_width=True)

        # ── VWAP Execution Profile ─────────────────────────────────────────
        elif gtype == "vwap_execution_profile":
            hours = [f"{h}:00" for h in range(9, 17)]
            vol_profile = [18, 12, 8, 7, 7, 8, 10, 30]  # typical U-shape
            exec_profile = [25, 20, 12, 8, 8, 10, 12, 5]  # algo execution
            fig = go.Figure()
            fig.add_trace(go.Bar(x=hours, y=vol_profile, name="Volumen mercado (%)",
                marker_color="#1a2540"))
            fig.add_trace(go.Scatter(x=hours, y=exec_profile, name="Ejecución algo (%)",
                line=dict(color=COLORS[0], width=2.5), mode="lines+markers"))
            fig.update_layout(**LAYOUT, title="Perfil VWAP — Volumen intradía vs. Ejecución")
            fig.update_yaxes(title="% del volumen total")
            st.plotly_chart(fig, use_container_width=True)

        # ── Credit Spread History ──────────────────────────────────────────
        elif gtype == "credit_spread_history":
            np.random.seed(7)
            n = 120
            t = list(range(n))
            hy_base = 4.5 + np.cumsum(np.random.normal(0, 0.15, n))
            hy_base = np.clip(hy_base, 2, 20)
            ig_base = hy_base * 0.28 + np.random.normal(0, 0.1, n)
            # Spike at 2008-like event
            hy_base[36:42] += np.array([3, 8, 14, 10, 7, 4])
            ig_base[36:42] += np.array([1, 3, 5, 4, 2.5, 1.5])
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=t, y=hy_base, name="HY Spread (bps×10)",
                line=dict(color=COLORS[3], width=2), fill="tozeroy",
                fillcolor="rgba(248,113,113,0.08)"))
            fig.add_trace(go.Scatter(x=t, y=ig_base, name="IG Spread (bps×10)",
                line=dict(color=COLORS[0], width=2)))
            fig.add_vrect(x0=36, x1=42, fillcolor="rgba(248,113,113,0.15)",
                line_width=0, annotation_text="Crisis")
            fig.update_layout(**LAYOUT, title="Credit Spreads — IG vs HY a lo largo del tiempo")
            fig.update_yaxes(title="Spread (bps / 10)")
            st.plotly_chart(fig, use_container_width=True)

        # ── HML Cumulative ─────────────────────────────────────────────────
        elif gtype == "hml_cumulative":
            np.random.seed(3)
            n = 300
            monthly = np.random.normal(0.003, 0.03, n)
            # Value premium with some crashes
            monthly[150:160] -= 0.04  # dotcom reversal
            monthly[200:210] -= 0.05  # GFC
            cumul = 100 * np.cumprod(1 + monthly)
            sp500 = 100 * np.cumprod(1 + np.random.normal(0.007, 0.045, n))
            fig = go.Figure()
            fig.add_trace(go.Scatter(y=cumul, name="HML (Value)",
                line=dict(color=COLORS[1], width=2)))
            fig.add_trace(go.Scatter(y=sp500, name="Market (referencia)",
                line=dict(color="#475569", width=1.5, dash="dot")))
            fig.update_layout(**LAYOUT, title="HML Factor — Retorno Acumulado (simulado)")
            fig.update_yaxes(title="Valor base 100")
            st.plotly_chart(fig, use_container_width=True)

        else:
            # Generic placeholder
            st.caption(f"📊 Gráfico `{gtype}` — visualización interactiva disponible en Modo Profundo.")

    except ImportError:
        st.info("Instala plotly para ver gráficos interactivos.")
    except Exception as e:
        st.caption(f"Gráfico: {e}")


def render_detail_tabs(card):
    keys = {
        "💡 Intuición":     "intuition",
        "🔢 Derivación":    "derivation",
        "🐍 Python":        "code_python",
        "🔗 Conexiones":    "connections",
        "📌 Fuente":        "source",
    }
    has = {label: bool(card.get(k)) for label, k in keys.items()}
    labels = [l for l, h in has.items() if h]
    if not labels:
        return
    tabs = st.tabs(labels)
    for tab, label in zip(tabs, labels):
        key = keys[label]
        with tab:
            if key == "code_python":
                st.code(card[key], language="python")
            elif key == "connections":
                for c in card[key]:
                    st.markdown(f"→ **{c}**")
            elif key == "source":
                st.markdown(f"📄 {card[key]}")
            else:
                st.markdown(card[key])


def _advance():
    st.session_state.q_idx       += 1
    st.session_state.revealed     = False
    st.session_state.mcq_answered = None
    st.session_state.tf_answered  = None
    st.session_state.fill_submitted = False
    st.session_state.fill_input   = ""


def _rating_buttons(card, state):
    st.divider()
    st.markdown("**¿Qué tan bien lo recordaste?**")
    cols = st.columns(6)
    ratings = [
        (0, "⬛ Nada"), (1, "🔴 Mal"),
        (2, "🟡 Difícil"), (3, "🟢 Bien"),
        (4, "💙 Fácil"), (5, "⚡ Perfecto"),
    ]
    for col, (score, label) in zip(cols, ratings):
        with col:
            if st.button(label, use_container_width=True, key=f"rate_{score}_{card['id']}"):
                new_s = engine.update(state, Rating(score))
                store.save_state(new_s)
                store.log_review(card["id"], score, card.get("domain", ""), card.get("topic", ""))
                st.session_state.session_total += 1
                if score >= 3:
                    st.session_state.session_correct += 1
                _advance()
                st.rerun()


def _next_button(card, state, correct: bool):
    st.divider()
    if st.button("→ Siguiente", type="primary", use_container_width=True):
        rating = Rating.EASY if correct else Rating.WRONG
        new_s  = engine.update(state, rating)
        store.save_state(new_s)
        store.log_review(card["id"], int(rating), card.get("domain", ""), card.get("topic", ""))
        st.session_state.session_total += 1
        _advance()
        st.rerun()


def render_numerical_bus(card, state):
    """Bus-friendly numerical problem: show hint, rate."""
    prob = card.get("numerical_problem", {})
    if not prob:
        return False
    st.markdown(f'<div class="card-q">🔢 {prob["question"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hint-box">💡 Bus hint: {prob["bus_hint"]}</div>', unsafe_allow_html=True)
    if not st.session_state.revealed:
        if st.button("👁 Ver solución completa", type="primary", use_container_width=True):
            st.session_state.revealed = True
            st.rerun()
    else:
        with st.expander("📐 Solución paso a paso", expanded=True):
            for i, step in enumerate(prob.get("steps", []), 1):
                st.markdown(f"`Paso {i}:` {step}")
            st.success(f"**Respuesta: {prob['answer']}**")
        render_graph(card)
        _rating_buttons(card, state)
    return True


def render_question_modes(card, state, is_bus: bool):
    qtype = st.session_state.q_type

    # ── FLASHCARD ────────────────────────────────────────────────────────────
    if qtype == "Flashcard":
        st.markdown(f'<div class="card-q">{card["front"]}</div>', unsafe_allow_html=True)
        if card.get("latex"):
            st.latex(card["latex"])
        if not st.session_state.revealed:
            if st.button("👁 Ver Respuesta", type="primary", use_container_width=True):
                st.session_state.revealed = True
                st.rerun()
        else:
            st.markdown(f'<div class="card-a">{card["back"]}</div>', unsafe_allow_html=True)
            render_graph(card)
            if not is_bus:
                render_detail_tabs(card)
            _rating_buttons(card, state)

    # ── MCQ ──────────────────────────────────────────────────────────────────
    elif qtype == "MCQ":
        mcq = card.get("mcq")
        if not mcq:
            st.session_state.q_type = "Flashcard"; st.rerun()
        st.markdown(f'<div class="card-q">{mcq["question"]}</div>', unsafe_allow_html=True)
        if card.get("latex"): st.latex(card["latex"])
        if is_bus: render_graph(card)

        if st.session_state.mcq_answered is None:
            for opt in mcq["options"]:
                if st.button(opt, use_container_width=True, key=f"mcq_{opt[0]}_{card['id']}"):
                    st.session_state.mcq_answered = opt[0]
                    if opt[0] == mcq["answer"]:
                        st.session_state.session_correct += 1
                    st.rerun()
        else:
            chosen, correct = st.session_state.mcq_answered, mcq["answer"]
            for opt in mcq["options"]:
                letter = opt[0]
                css = "mcq-ok" if letter == correct else ("mcq-err" if letter == chosen else "mcq-opt")
                st.markdown(f'<div class="mcq-opt {css}">{opt}</div>', unsafe_allow_html=True)
            ok = (chosen == correct)
            if ok: st.success(f"✅ Correcto — {mcq['explanation']}")
            else:   st.error(f"❌ Respuesta: **{correct}** — {mcq['explanation']}")
            _next_button(card, state, correct=ok)

    # ── TRUE/FALSE ───────────────────────────────────────────────────────────
    elif qtype == "True/False":
        tf = card.get("true_false")
        if not tf:
            st.session_state.q_type = "Flashcard"; st.rerun()
        st.markdown(f'<div class="card-q">{tf["statement"]}</div>', unsafe_allow_html=True)
        if is_bus: render_graph(card)

        if st.session_state.tf_answered is None:
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ VERDADERO", use_container_width=True, type="primary"):
                    st.session_state.tf_answered = True
                    if True == tf["answer"]: st.session_state.session_correct += 1
                    st.rerun()
            with c2:
                if st.button("❌ FALSO", use_container_width=True):
                    st.session_state.tf_answered = False
                    if False == tf["answer"]: st.session_state.session_correct += 1
                    st.rerun()
        else:
            ok = (st.session_state.tf_answered == tf["answer"])
            label = "VERDADERO" if tf["answer"] else "FALSO"
            if ok: st.success(f"✅ Correcto — La afirmación es **{label}**")
            else:   st.error(f"❌ Es **{label}**")
            st.info(f"💡 {tf['explanation']}")
            _next_button(card, state, correct=ok)

    # ── FILL IN THE BLANK ────────────────────────────────────────────────────
    elif qtype == "Fill-in-blank":
        fb = card.get("fill_blank")
        if not fb:
            st.session_state.q_type = "Flashcard"; st.rerun()
        st.markdown(f'<div class="card-q">{card["front"]}</div>', unsafe_allow_html=True)
        st.markdown(f"**Completa:** `{fb['template']}`")

        if not st.session_state.fill_submitted:
            user_input = st.text_input("Tu respuesta:", key="fill_input_field",
                                       placeholder="Escribe sin ver la carta...")
            if st.button("✔ Verificar", type="primary", use_container_width=True):
                st.session_state.fill_submitted = True
                st.session_state.fill_input = user_input
                answers = [a.lower().strip() for a in fb["answers"]]
                if any(a in user_input.lower() for a in answers):
                    st.session_state.session_correct += 1
                st.rerun()
        else:
            answers = fb["answers"]
            user    = st.session_state.fill_input
            ok = any(a.lower() in user.lower() for a in answers)
            if ok: st.success(f"✅ Correcto — {' / '.join(answers)}")
            else:   st.error(f"❌ Esperado: **{' / '.join(answers)}** | Tu respuesta: {user}")
            _next_button(card, state, correct=ok)

    # ── NUMERICAL PROBLEM ────────────────────────────────────────────────────
    elif qtype == "Numérico":
        prob = card.get("numerical_problem")
        if not prob:
            st.info("Esta carta no tiene problema numérico. Cargando flashcard...")
            st.session_state.q_type = "Flashcard"; st.rerun()
        render_numerical_bus(card, state)

    # ── GRÁFICO ──────────────────────────────────────────────────────────────
    elif qtype == "Gráfico":
        if not card.get("graph_type"):
            st.session_state.q_type = "Flashcard"; st.rerun()
        st.markdown("**Observa el gráfico y responde la pregunta:**")
        render_graph(card)
        st.markdown(f'<div class="card-q">{card["front"]}</div>', unsafe_allow_html=True)
        if not st.session_state.revealed:
            if st.button("👁 Ver Interpretación", type="primary", use_container_width=True):
                st.session_state.revealed = True
                st.rerun()
        else:
            st.markdown(f'<div class="card-a">{card["back"]}</div>', unsafe_allow_html=True)
            _rating_buttons(card, state)


def build_queue(domain_filter, bus_only: bool, question_type: str) -> list[dict]:
    cards = ALL_CARDS
    if domain_filter != "All":
        cards = [c for c in cards if c["domain"] == domain_filter]
    if bus_only:
        cards = [c for c in cards if "bus" in c.get("mode_tags", [])]

    type_key_map = {
        "MCQ": "mcq", "True/False": "true_false",
        "Fill-in-blank": "fill_blank", "Numérico": "numerical_problem",
        "Gráfico": "graph_type",
    }
    if question_type in type_key_map:
        k = type_key_map[question_type]
        cards = [c for c in cards if c.get(k)]

    states = store.all_states()
    due   = [c for c in cards if engine.is_due(states.get(c["id"], CardState(card_id=c["id"])))]
    other = [c for c in cards if c not in due]
    random.shuffle(due); random.shuffle(other)
    return due + other


def render_study_session(mode_label: str):
    is_bus = (mode_label == "Bus")
    icon   = "🚌" if is_bus else "🏠"
    title  = f"{icon} MODO {'BUS' if is_bus else 'PROFUNDO'}"
    sub    = "Sin papel — MCQ, T/F, Numérico mental" if is_bus else "Derivaciones, código, análisis completo"

    st.markdown(f'<div class="title-main">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="title-sub">{sub}</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.5, 1.5, 1])
    with col1:
        domain = st.selectbox("Dominio", ALL_DOMAINS, key=f"dom_{mode_label}")
    with col2:
        if is_bus:
            q_types = ["Flashcard", "MCQ", "True/False", "Numérico", "Gráfico", "Fill-in-blank"]
        else:
            q_types = ["Flashcard", "MCQ", "True/False", "Fill-in-blank", "Numérico", "Gráfico"]
        q_type = st.selectbox("Tipo de pregunta", q_types, key=f"qt_{mode_label}")
        st.session_state.q_type = q_type
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("▶ Iniciar sesión", type="primary", use_container_width=True,
                     key=f"load_{mode_label}"):
            queue = build_queue(domain, is_bus, q_type)
            st.session_state.queue = queue
            st.session_state.q_idx = 0
            st.session_state.revealed = False
            st.session_state.mcq_answered = None
            st.session_state.tf_answered  = None
            st.session_state.fill_submitted = False
            st.session_state.session_total  = 0
            st.session_state.session_correct = 0
            if not queue:
                st.warning("Sin cartas con ese filtro. Prueba 'All'.")
            st.rerun()

    queue = st.session_state.queue
    idx   = st.session_state.q_idx

    if not queue:
        st.markdown("""
        <div style="background:#0e1526;border:1px solid #1a2540;border-radius:16px;
                    padding:44px;text-align:center;margin-top:24px;">
          <div style="font-size:36px;margin-bottom:10px;">📚</div>
          <div style="color:#60a5fa;font-size:17px;font-weight:600;">Configura y carga una sesión</div>
          <div style="color:#475569;font-size:13px;margin-top:6px;">
            Elige dominio y tipo de pregunta, luego presiona ▶ Iniciar sesión
          </div>
        </div>
        """, unsafe_allow_html=True)
        return

    if idx >= len(queue):
        total   = st.session_state.session_total
        correct = st.session_state.session_correct
        pct     = int(correct / max(total, 1) * 100)
        st.markdown(f"""
        <div style="background:#0e1526;border:1px solid #1a2540;border-radius:16px;
                    padding:44px;text-align:center;">
          <div style="font-size:36px;margin-bottom:10px;">🎓</div>
          <div style="color:#60a5fa;font-size:19px;font-weight:700;">¡Sesión completa!</div>
          <div style="display:flex;justify-content:center;gap:40px;margin-top:16px;">
            <div>
              <div style="font-size:32px;color:#60a5fa;font-family:'JetBrains Mono',monospace;">{total}</div>
              <div style="font-size:11px;color:#475569;">revisadas</div>
            </div>
            <div>
              <div style="font-size:32px;color:#34d399;font-family:'JetBrains Mono',monospace;">{pct}%</div>
              <div style="font-size:11px;color:#475569;">precisión</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔁 Nueva sesión", type="primary", use_container_width=True):
            st.session_state.queue = []
            st.session_state.q_idx = 0
            st.rerun()
        return

    card  = queue[idx]
    state = store.get_state(card["id"])

    pct_prog = idx / len(queue)
    m_score  = engine.mastery_score(state)
    m_pct    = int(m_score * 100)
    m_col    = mastery_color(m_pct)

    st.markdown(f"""
    <div style="display:flex;justify-content:space-between;font-size:11px;color:#475569;margin-bottom:3px;">
      <span>{idx+1} / {len(queue)}</span>
      <span>Dominio carta: <span style="color:{m_col};">{m_pct}%</span></span>
    </div>
    <div class="prog-bg">
      <div style="background:#3b82f6;width:{pct_prog*100:.1f}%;height:100%;border-radius:6px;"></div>
    </div>
    """, unsafe_allow_html=True)

    render_tags(card)
    st.markdown("")
    render_question_modes(card, state, is_bus=is_bus)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGES
# ═══════════════════════════════════════════════════════════════════════════════

# ── DASHBOARD ─────────────────────────────────────────────────────────────────
if st.session_state.page == "Dashboard":
    st.markdown('<div class="title-main">∂ INVEST MEMORIA</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-sub">Investment Research Learning Platform · AFP</div>',
               unsafe_allow_html=True)

    summ = analytics.summary(ALL_CARDS)
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Cartas totales", len(ALL_CARDS))
    c2.metric("Para hoy",       summ["due_today"])
    c3.metric("Dominio medio",  f"{summ['mean_mastery']*100:.0f}%")
    c4.metric("Precisión",      f"{summ['accuracy']*100:.0f}%")
    c5.metric("Streak 🔥",      f"{summ['streak_days']}d")

    st.divider()
    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown("#### 🎯 Temas más débiles")
        for t in analytics.weak_topics(ALL_CARDS, 6):
            pct = int(t["mastery"] * 100)
            col = mastery_color(pct)
            st.markdown(f"""
            <div style="margin-bottom:10px;">
              <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:3px;">
                <span>{t['topic']}</span>
                <span style="color:{col};font-family:'JetBrains Mono',monospace;">{pct}%</span>
              </div>
              <div style="background:#1a2540;border-radius:5px;height:4px;">
                <div style="background:{col};width:{pct}%;height:100%;border-radius:5px;"></div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    with col_r:
        st.markdown("#### 📋 Cartas por dominio")
        for dom in DOMAINS:
            cnt = sum(1 for c in ALL_CARDS if c.get("domain") == dom)
            bus = sum(1 for c in ALL_CARDS if c.get("domain") == dom and "bus" in c.get("mode_tags", []))
            col = DOMAIN_COLORS.get(dom, "#64748b")
            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;font-size:13px;
                        padding:6px 0;border-bottom:1px solid #1a2540;">
              <span style="color:{col};">{dom}</span>
              <span style="font-family:'JetBrains Mono',monospace;color:#475569;">
                {cnt} total · {bus} bus</span>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    c_bus, c_deep, c_idea = st.columns(3)
    bus_n = len(get_bus_cards())
    with c_bus:
        if st.button(f"🚌 Modo Bus ({bus_n} cartas)", use_container_width=True, type="primary"):
            st.session_state.page = "Bus"; st.session_state.queue = []; st.rerun()
    with c_deep:
        if st.button(f"🏠 Modo Profundo ({len(ALL_CARDS)} cartas)", use_container_width=True):
            st.session_state.page = "Deep"; st.session_state.queue = []; st.rerun()
    with c_idea:
        if st.button("💡 Modo Idea (browser libre)", use_container_width=True):
            st.session_state.page = "Idea"; st.rerun()


# ── BUS MODE ──────────────────────────────────────────────────────────────────
elif st.session_state.page == "Bus":
    render_study_session("Bus")


# ── DEEP MODE ─────────────────────────────────────────────────────────────────
elif st.session_state.page == "Deep":
    render_study_session("Deep")


# ── IDEA MODE ─────────────────────────────────────────────────────────────────
elif st.session_state.page == "Idea":
    st.markdown('<div class="title-main">💡 MODO IDEA</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-sub">Browser libre — busca conceptos, encuentra conexiones, captura ideas</div>',
               unsafe_allow_html=True)

    search = st.text_input("🔍 Busca un concepto, tema o keyword de un paper",
                           placeholder="momentum, convexidad, risk parity, ESG materiality...",
                           key="idea_search_input")

    col_d, col_type = st.columns(2)
    with col_d:
        f_domain = st.selectbox("Filtrar dominio", ALL_DOMAINS, key="idea_dom")
    with col_type:
        has_numeric = st.checkbox("Solo con problema numérico", value=False)

    filtered = ALL_CARDS
    if f_domain != "All":
        filtered = [c for c in filtered if c["domain"] == f_domain]
    if has_numeric:
        filtered = [c for c in filtered if c.get("numerical_problem")]
    if search:
        q = search.lower()
        filtered = [c for c in filtered if
                    q in c.get("front", "").lower() or
                    q in c.get("back", "").lower() or
                    q in c.get("topic", "").lower() or
                    q in c.get("intuition", "").lower() or
                    q in str(c.get("connections", [])).lower() or
                    q in c.get("source", "").lower()]

    st.markdown(f"**{len(filtered)} cartas encontradas**")

    states = store.all_states()
    for card in filtered:
        state = states.get(card["id"], CardState(card_id=card["id"]))
        m_pct = int(engine.mastery_score(state) * 100)
        m_col = mastery_color(m_pct)
        dom_col = DOMAIN_COLORS.get(card.get("domain", ""), "#64748b")

        with st.expander(f"[{card.get('domain','')[:3].upper()}] {card.get('topic','')} — {card['front'][:60]}..."):
            render_tags(card)
            st.markdown(f"**Q:** {card['front']}")
            st.markdown(f"**A:** {card['back']}")
            if card.get("latex"): st.latex(card["latex"])
            if card.get("intuition"):
                st.markdown(f"💡 *{card['intuition']}*")
            if card.get("numerical_problem"):
                prob = card["numerical_problem"]
                st.markdown(f"**🔢 Problema:** {prob['question']}")
                st.caption(f"Bus hint: {prob['bus_hint']}")
            if card.get("connections"):
                st.markdown("**Conexiones:** " + " · ".join(card["connections"]))
            if card.get("source"):
                st.caption(f"📄 {card['source']}")
            render_graph(card)

            col_study, col_note = st.columns(2)
            with col_study:
                if st.button("📖 Estudiar esta carta", key=f"idea_{card['id']}",
                             use_container_width=True):
                    st.session_state.queue   = [card]
                    st.session_state.q_idx   = 0
                    st.session_state.q_type  = "Flashcard"
                    st.session_state.revealed = False
                    st.session_state.page    = "Deep"
                    st.rerun()
            with col_note:
                st.markdown(f"<div style='text-align:center;font-size:12px;color:{m_col};'>"
                           f"Dominio: {m_pct}%</div>", unsafe_allow_html=True)


# ── LIBRARY ───────────────────────────────────────────────────────────────────
elif st.session_state.page == "Library":
    st.markdown('<div class="title-main">📚 BIBLIOTECA</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-sub">Todas las cartas del sistema</div>', unsafe_allow_html=True)

    col_s, col_d, col_m = st.columns([2, 1.5, 1])
    with col_s:
        search = st.text_input("🔍 Buscar", placeholder="duracion, momentum, ESG...")
    with col_d:
        f_domain = st.selectbox("Dominio", ALL_DOMAINS)
    with col_m:
        f_diff = st.selectbox("Dificultad", ["Todos", "Foundational", "Intermediate", "Advanced", "Expert"])

    filtered = ALL_CARDS
    if f_domain != "All":
        filtered = [c for c in filtered if c["domain"] == f_domain]
    if f_diff != "Todos":
        filtered = [c for c in filtered if c.get("difficulty") == f_diff]
    if search:
        q = search.lower()
        filtered = [c for c in filtered if
                    q in c.get("front", "").lower() or
                    q in c.get("topic", "").lower() or
                    q in c.get("back", "").lower()]

    st.markdown(f"**{len(filtered)} cartas**")
    states = store.all_states()

    for card in filtered:
        state = states.get(card["id"], CardState(card_id=card["id"]))
        m_pct = int(engine.mastery_score(state) * 100)
        m_col = mastery_color(m_pct)
        with st.expander(f"[{card.get('topic','')}] {card['front'][:70]}"):
            cc1, cc2 = st.columns([3, 1])
            with cc1:
                render_tags(card)
                st.markdown(f"**A:** {card['back'][:400]}")
                if card.get("latex"): st.latex(card["latex"])
                render_graph(card)
                render_detail_tabs(card)
            with cc2:
                st.markdown(f"""
                <div style="text-align:center;background:#0a0f1e;border:1px solid #1a2540;
                            border-radius:8px;padding:14px;">
                  <div style="font-size:26px;color:{m_col};font-family:'JetBrains Mono',monospace;
                              font-weight:700;">{m_pct}%</div>
                  <div style="font-size:11px;color:#475569;">dominio</div>
                  <div style="margin-top:8px;font-size:11px;color:#475569;line-height:1.8;">
                    {state.repetitions} repasos<br>
                    {state.error_count} errores<br>
                    vence en {engine.days_until_due(state):.0f}d
                  </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("Estudiar", key=f"lib_{card['id']}", use_container_width=True):
                    st.session_state.queue   = [card]
                    st.session_state.q_idx   = 0
                    st.session_state.q_type  = "Flashcard"
                    st.session_state.revealed = False
                    st.session_state.page    = "Deep"
                    st.rerun()


# ── ANALYTICS ─────────────────────────────────────────────────────────────────
elif st.session_state.page == "Analytics":
    st.markdown('<div class="title-main">📈 ANALYTICS</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-sub">Retención · Heatmaps · Progreso por dominio</div>',
               unsafe_allow_html=True)

    summ = analytics.summary(ALL_CARDS)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Streak", f"{summ['streak_days']}d 🔥")
    c2.metric("Precisión", f"{summ['accuracy']*100:.1f}%")
    c3.metric("Dominio medio", f"{summ['mean_mastery']*100:.1f}%")
    c4.metric("Repasos totales", summ["total_reviews"])

    try:
        import plotly.graph_objects as go

        LAYOUT2 = dict(
            paper_bgcolor="#070b14", plot_bgcolor="#070b14",
            font=dict(color="#94a3b8", size=11, family="Inter"),
            margin=dict(l=0, r=0, t=30, b=0), height=280,
            xaxis=dict(gridcolor="#1a2540"), yaxis=dict(gridcolor="#1a2540"),
        )

        st.divider()
        st.markdown("### 📅 Actividad diaria (últimos 14 días)")
        rpd    = analytics.reviews_per_day(14)
        dates  = [d["date"][-5:] for d in rpd]
        counts = [d["count"] for d in rpd]
        fig    = go.Figure(go.Bar(x=dates, y=counts, marker_color="#3b82f6"))
        fig.update_layout(**LAYOUT2, title="Repasos por día")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 🗺️ Heatmap de dominio por tópico")
        hdata = analytics.topic_mastery_heatmap(ALL_CARDS)
        if hdata:
            domains_h = sorted({d["domain"] for d in hdata})
            topics_h  = sorted({d["topic"] for d in hdata})
            zm = []
            for dom in domains_h:
                row = []
                for top in topics_h:
                    match = next((d for d in hdata if d["domain"] == dom and d["topic"] == top), None)
                    row.append(match["mastery"] * 100 if match else None)
                zm.append(row)
            fig3 = go.Figure(go.Heatmap(
                z=zm, x=topics_h, y=domains_h,
                colorscale=[[0,"#070b14"],[0.33,"#f87171"],[0.66,"#f59e0b"],[1,"#34d399"]],
                zmin=0, zmax=100,
                text=[[f"{v:.0f}%" if v is not None else "" for v in row] for row in zm],
                texttemplate="%{text}",
            ))
            fig3.update_layout(paper_bgcolor="#070b14", plot_bgcolor="#070b14",
                font=dict(color="#94a3b8", size=10),
                height=max(200, len(domains_h) * 55),
                margin=dict(l=0, r=0, t=10, b=0),
                xaxis=dict(tickangle=-40))
            st.plotly_chart(fig3, use_container_width=True)

    except ImportError:
        st.info("Instala plotly para ver gráficos.")

    col_w, col_s = st.columns(2)
    with col_w:
        st.markdown("### ⚠️ Temas más débiles")
        for t in analytics.weak_topics(ALL_CARDS, 5):
            st.markdown(f"- **{t['topic']}** ({t['mastery']*100:.0f}%)")
    with col_s:
        st.markdown("### ✅ Temas más fuertes")
        for t in analytics.strong_topics(ALL_CARDS, 5):
            st.markdown(f"- **{t['topic']}** ({t['mastery']*100:.0f}%)")


# ── ADD CARD ──────────────────────────────────────────────────────────────────
elif st.session_state.page == "AddCard":
    st.markdown('<div class="title-main">➕ NUEVA CARTA</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-sub">Agrega insights de papers directamente desde el formulario</div>',
               unsafe_allow_html=True)

    st.info(
        "💡 **Workflow recomendado:** Usa el prompt en `PAPER_EXTRACTION_PROMPT.py` con Claude/GPT-4o "
        "para generar cartas automáticamente desde un paper, luego pégalas en `content/invest_cards.py` "
        "para que sean permanentes. Este formulario es para cartas rápidas o ideas ad-hoc."
    )

    with st.form("add_card"):
        c1, c2 = st.columns(2)
        with c1:
            domain = st.selectbox("Dominio", DOMAINS)
        with c2:
            topic = st.text_input("Tópico", placeholder="Factor Investing — Low Vol")

        c3, c4, c5 = st.columns(3)
        with c3:
            diff = st.selectbox("Dificultad", ["Foundational", "Intermediate", "Advanced", "Expert"])
        with c4:
            mode_raw = st.selectbox("Modo", ["bus+home", "bus only", "home only"])
        with c5:
            source = st.text_input("Fuente", placeholder="Autor (año) — Journal")

        front     = st.text_area("Pregunta *", height=80)
        back      = st.text_area("Respuesta *", height=120)
        latex     = st.text_input("Fórmula LaTeX (sin $)")
        intuition = st.text_area("Intuición / Analogía memorable", height=70)
        bus_hint  = st.text_input("Bus Hint numérico (si aplica)", placeholder="MD×Δy = 7.5×0.005 = 0.0375")
        connections_raw = st.text_input("Conexiones (separadas por coma)", placeholder="Duration, Convexidad, OAS")

        submitted = st.form_submit_button("💾 Guardar carta", type="primary", use_container_width=True)

    if submitted:
        if not front or not back:
            st.error("Pregunta y respuesta son obligatorias.")
        else:
            import uuid
            mode_map = {"bus+home": ["bus", "home"], "bus only": ["bus"], "home only": ["home"]}
            connections = [c.strip() for c in connections_raw.split(",") if c.strip()] if connections_raw else []
            new_card = {
                "id": f"user_{str(uuid.uuid4())[:8]}",
                "domain": domain,
                "topic": topic,
                "difficulty": diff,
                "mode_tags": mode_map[mode_raw],
                "source": source,
                "front": front,
                "back": back,
                "latex": latex,
                "intuition": intuition,
                "connections": connections,
            }
            if bus_hint:
                new_card["numerical_problem"] = {
                    "question": front,
                    "steps": [],
                    "answer": "Ver respuesta completa",
                    "bus_hint": bus_hint
                }
            store.save_user_card(new_card)
            ALL_CARDS.append(new_card)
            st.success(f"✅ Carta guardada. Para que sea permanente entre sesiones, agrégala a `content/invest_cards.py`.")
