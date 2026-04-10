import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

# ─── Page Config ────────────────────────────────────────────────
st.set_page_config(
    page_title="Sales Forecasting · Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Premium CSS Theme ──────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Root Variables ── */
:root {
    --bg-primary: #0a0e17;
    --bg-card: rgba(17, 25, 40, 0.75);
    --bg-card-hover: rgba(25, 35, 55, 0.85);
    --border-color: rgba(99, 130, 255, 0.12);
    --accent-blue: #6C8FFF;
    --accent-purple: #A78BFA;
    --accent-cyan: #22D3EE;
    --accent-emerald: #34D399;
    --accent-rose: #FB7185;
    --accent-amber: #FBBF24;
    --text-primary: #E2E8F0;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;
    --gradient-1: linear-gradient(135deg, #6C8FFF 0%, #A78BFA 100%);
    --gradient-2: linear-gradient(135deg, #22D3EE 0%, #6C8FFF 100%);
    --gradient-3: linear-gradient(135deg, #34D399 0%, #22D3EE 100%);
    --shadow-glow: 0 0 40px rgba(108, 143, 255, 0.08);
}

/* ── Global ── */
html, body, .stApp, [data-testid="stAppViewContainer"] {
    background-color: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1321 0%, #111b2e 100%) !important;
    border-right: 1px solid var(--border-color) !important;
}

section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: var(--accent-blue) !important;
    font-weight: 600 !important;
    letter-spacing: -0.02em;
}

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] label {
    color: var(--text-secondary) !important;
    font-size: 0.85rem !important;
}

section[data-testid="stSidebar"] .stSlider > div > div {
    color: var(--text-primary) !important;
}

/* ── Slider Thumb & Track ── */
.stSlider [data-baseweb="slider"] [role="slider"] {
    background: var(--gradient-1) !important;
    border: 2px solid rgba(255,255,255,0.2) !important;
    box-shadow: 0 0 12px rgba(108,143,255,0.4) !important;
}
.stSlider [data-baseweb="slider"] > div > div:first-child {
    background: rgba(108,143,255,0.25) !important;
}
.stSlider [data-baseweb="slider"] > div > div:first-child > div {
    background: var(--accent-blue) !important;
}

/* ── Metric Cards Container (injected via markdown) ── */
.metric-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 1rem 0 1.5rem 0;
}

.metric-card {
    background: var(--bg-card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 1.4rem 1.5rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 16px 16px 0 0;
}
.metric-card:nth-child(1)::before { background: var(--gradient-1); }
.metric-card:nth-child(2)::before { background: var(--gradient-2); }
.metric-card:nth-child(3)::before { background: var(--gradient-3); }
.metric-card:nth-child(4)::before { background: linear-gradient(135deg, var(--accent-rose) 0%, var(--accent-amber) 100%); }

.metric-card:hover {
    background: var(--bg-card-hover);
    transform: translateY(-2px);
    box-shadow: var(--shadow-glow);
    border-color: rgba(99, 130, 255, 0.25);
}

.metric-label {
    font-size: 0.75rem;
    font-weight: 500;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.5rem;
}

.metric-value {
    font-size: 1.75rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 0.25rem;
}
.metric-card:nth-child(1) .metric-value { color: var(--accent-blue); }
.metric-card:nth-child(2) .metric-value { color: var(--accent-cyan); }
.metric-card:nth-child(3) .metric-value { color: var(--accent-emerald); }
.metric-card:nth-child(4) .metric-value { color: var(--accent-rose); }

.metric-sub {
    font-size: 0.78rem;
    color: var(--text-secondary);
}

/* ── Section Titles ── */
.section-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 2rem 0 0.75rem 0;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-title .icon {
    font-size: 1.15rem;
}

/* ── Hero Header ── */
.hero-header {
    padding: 1.5rem 0 0.5rem 0;
}
.hero-header h1 {
    font-size: 2.1rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    background: linear-gradient(135deg, #ffffff 0%, #6C8FFF 50%, #A78BFA 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.25rem 0;
    line-height: 1.2;
}
.hero-subtitle {
    font-size: 0.92rem;
    color: var(--text-secondary);
    font-weight: 400;
    margin: 0;
}

/* ── Dataframe styling ── */
[data-testid="stDataFrame"] {
    border: 1px solid var(--border-color) !important;
    border-radius: 12px !important;
    overflow: hidden;
}

/* ── Toggle buttons (radio/tabs) ── */
.stRadio > div {
    gap: 0.5rem;
}
.stRadio > div > label {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 8px !important;
    padding: 0.4rem 1rem !important;
    color: var(--text-secondary) !important;
    transition: all 0.2s ease;
}
.stRadio > div > label:hover {
    border-color: var(--accent-blue) !important;
    color: var(--text-primary) !important;
}
.stRadio > div > label[data-checked="true"] {
    background: rgba(108,143,255,0.15) !important;
    border-color: var(--accent-blue) !important;
    color: var(--accent-blue) !important;
}

/* ── Divider ── */
.premium-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, var(--border-color) 50%, transparent 100%);
    margin: 1.5rem 0;
    border: none;
}

/* ── Checkbox & selectbox ── */
.stCheckbox label span {
    color: var(--text-secondary) !important;
}
.stSelectbox label {
    color: var(--text-secondary) !important;
}

/* ── Hide default streamlit branding ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

/* ── Smooth scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: rgba(108,143,255,0.25);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(108,143,255,0.4);
}
</style>
""", unsafe_allow_html=True)

# ─── Hero Header ─────────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <h1>📈 Sales Forecasting Dashboard</h1>
    <p class="hero-subtitle">
        Analyze historical writing‑paper sales with Moving Averages &amp; Exponential Smoothing
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)

# ─── Load Data ───────────────────────────────────────────────────
DATA_DIR = Path(__file__).parent
df = pd.read_csv(DATA_DIR / "monthly-writing-paper-sales.csv")
df.columns = ["Month", "Sales"]
df['Month'] = pd.date_range(start='2001-01', periods=len(df), freq='M')

# ─── Sidebar ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Model Parameters")
    st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)

    st.markdown("##### 📐 Window Size (n)")
    n = st.slider(
        "Window size for SMA & WMA",
        min_value=2, max_value=12, value=3,
        label_visibility="collapsed",
    )

    st.markdown("")
    st.markdown("##### 🔮 Smoothing Factor (α)")
    alpha = st.slider(
        "Alpha for Exponential Smoothing",
        min_value=0.05, max_value=1.0, value=0.5, step=0.05,
        label_visibility="collapsed",
    )

    st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
    st.markdown("##### 📊 Chart Options")
    show_sma = st.checkbox("Show SMA", value=True)
    show_wma = st.checkbox("Show WMA", value=True)
    show_exp = st.checkbox("Show Exponential", value=True)

    st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="font-size:0.72rem;color:#475569;text-align:center;">'
        'Built with Streamlit · Data: Monthly Writing‑Paper Sales</p>',
        unsafe_allow_html=True,
    )

# ─── Compute Forecasts ──────────────────────────────────────────
df['SMA'] = df['Sales'].rolling(window=n).mean()

weights = np.arange(1, n + 1)
df['WMA'] = df['Sales'].rolling(n).apply(
    lambda x: np.dot(x, weights) / weights.sum(), raw=True
)

df['Exp_Smoothing'] = df['Sales'].ewm(alpha=alpha, adjust=False).mean()

# ─── KPI Metrics ────────────────────────────────────────────────
latest = df['Sales'].iloc[-1]
avg_sales = df['Sales'].mean()
peak = df['Sales'].max()
low = df['Sales'].min()

# MAE for each method (drop NaN rows)
valid = df.dropna()
mae_sma = np.mean(np.abs(valid['Sales'] - valid['SMA']))
mae_wma = np.mean(np.abs(valid['Sales'] - valid['WMA']))
mae_exp = np.mean(np.abs(valid['Sales'] - valid['Exp_Smoothing']))
best_method = min(
    [("SMA", mae_sma), ("WMA", mae_wma), ("Exponential", mae_exp)],
    key=lambda x: x[1],
)

st.markdown(f"""
<div class="metric-grid">
    <div class="metric-card">
        <div class="metric-label">Latest Sales</div>
        <div class="metric-value">{latest:,.0f}</div>
        <div class="metric-sub">{df['Month'].iloc[-1].strftime('%b %Y')}</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Average Sales</div>
        <div class="metric-value">{avg_sales:,.0f}</div>
        <div class="metric-sub">Across {len(df)} months</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Peak Sales</div>
        <div class="metric-value">{peak:,.0f}</div>
        <div class="metric-sub">{df.loc[df['Sales'].idxmax(), 'Month'].strftime('%b %Y')}</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Best Model (MAE)</div>
        <div class="metric-value">{best_method[0]}</div>
        <div class="metric-sub">MAE: {best_method[1]:,.1f}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Main Chart ──────────────────────────────────────────────────
st.markdown(
    '<div class="section-title"><span class="icon">📉</span> Forecast Comparison</div>',
    unsafe_allow_html=True,
)

fig = go.Figure()

# Actual Sales
fig.add_trace(go.Scatter(
    x=df['Month'], y=df['Sales'],
    name='Actual Sales',
    mode='lines',
    line=dict(color='#E2E8F0', width=2),
    fill='tozeroy',
    fillcolor='rgba(226,232,240,0.04)',
    hovertemplate='<b>Actual</b><br>%{x|%b %Y}<br>Sales: %{y:,.0f}<extra></extra>',
))

if show_sma:
    fig.add_trace(go.Scatter(
        x=df['Month'], y=df['SMA'],
        name=f'SMA (n={n})',
        mode='lines',
        line=dict(color='#6C8FFF', width=2.5, dash='solid'),
        hovertemplate=f'<b>SMA (n={n})</b><br>%{{x|%b %Y}}<br>Value: %{{y:,.0f}}<extra></extra>',
    ))

if show_wma:
    fig.add_trace(go.Scatter(
        x=df['Month'], y=df['WMA'],
        name=f'WMA (n={n})',
        mode='lines',
        line=dict(color='#22D3EE', width=2.5, dash='dot'),
        hovertemplate=f'<b>WMA (n={n})</b><br>%{{x|%b %Y}}<br>Value: %{{y:,.0f}}<extra></extra>',
    ))

if show_exp:
    fig.add_trace(go.Scatter(
        x=df['Month'], y=df['Exp_Smoothing'],
        name=f'Exp (α={alpha})',
        mode='lines',
        line=dict(color='#34D399', width=2.5, dash='dashdot'),
        hovertemplate=f'<b>Exp (α={alpha})</b><br>%{{x|%b %Y}}<br>Value: %{{y:,.0f}}<extra></extra>',
    ))

fig.update_layout(
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Inter, sans-serif', color='#94A3B8'),
    height=480,
    margin=dict(l=0, r=0, t=30, b=0),
    legend=dict(
        orientation='h',
        yanchor='bottom', y=1.02,
        xanchor='left', x=0,
        font=dict(size=12, color='#CBD5E1'),
        bgcolor='rgba(0,0,0,0)',
    ),
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        tickformat='%b\n%Y',
        dtick='M6',
        tickfont=dict(size=10),
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='rgba(99,130,255,0.06)',
        zeroline=False,
        tickfont=dict(size=10),
        tickprefix='',
    ),
    hovermode='x unified',
    hoverlabel=dict(
        bgcolor='#1E293B',
        bordercolor='rgba(99,130,255,0.3)',
        font=dict(color='#E2E8F0', family='Inter'),
    ),
)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# ─── Error Comparison Chart ──────────────────────────────────────
st.markdown(
    '<div class="section-title"><span class="icon">📊</span> Model Accuracy (MAE)</div>',
    unsafe_allow_html=True,
)

col_chart, col_table = st.columns([1, 1], gap="large")

with col_chart:
    bar_fig = go.Figure()
    methods = ['SMA', 'WMA', 'Exponential']
    mae_vals = [mae_sma, mae_wma, mae_exp]
    colors = ['#6C8FFF', '#22D3EE', '#34D399']

    bar_fig.add_trace(go.Bar(
        x=methods,
        y=mae_vals,
        marker=dict(
            color=colors,
            line=dict(width=0),
            cornerradius=6,
        ),
        text=[f'{v:,.0f}' for v in mae_vals],
        textposition='outside',
        textfont=dict(color='#CBD5E1', size=13, family='Inter'),
        hovertemplate='<b>%{x}</b><br>MAE: %{y:,.1f}<extra></extra>',
        width=0.45,
    ))

    bar_fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter, sans-serif', color='#94A3B8'),
        height=300,
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=12, color='#CBD5E1'),
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(99,130,255,0.06)',
            zeroline=False,
            tickfont=dict(size=10),
        ),
        showlegend=False,
    )
    st.plotly_chart(bar_fig, use_container_width=True, config={'displayModeBar': False})

with col_table:
    st.markdown(
        '<div class="section-title" style="margin-top:0;"><span class="icon">🗂️</span> Recent Data</div>',
        unsafe_allow_html=True,
    )
    display_df = df.copy()
    display_df['Month'] = display_df['Month'].dt.strftime('%b %Y')
    display_df = display_df.round(1)
    st.dataframe(
        display_df.tail(12),
        hide_index=True,
        use_container_width=True,
    )
