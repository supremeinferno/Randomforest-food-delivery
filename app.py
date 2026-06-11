import streamlit as st
import pickle
import pandas as pd

# ── Page config ─────────────────────────────────────────────────────────────── 
st.set_page_config(
    page_title="DeliverIQ — Know Before You Wait",
    page_icon="🛵",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #08090d;
    color: #dde1ed;
}

.stApp { background-color: #08090d; }

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 4rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 780px !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0 !important;
}

[data-testid="stToolbar"] { display: none !important; }

/* ── ENTRANCE ANIMATIONS ── */
@keyframes slideDown {
    from { opacity: 0; transform: translateY(-18px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(22px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes popIn {
    from { opacity: 0; transform: scale(0.88); }
    to   { opacity: 1; transform: scale(1); }
}
@keyframes pulse-dot {
    0%, 100% { box-shadow: 0 0 0 0 rgba(74,222,128,0.5); }
    50%       { box-shadow: 0 0 0 5px rgba(74,222,128,0); }
}
@keyframes shimmer {
    0%   { background-position: -400px 0; }
    100% { background-position: 400px 0; }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-4px); }
}

/* ── NAVBAR ── */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 0 1.3rem;
    border-bottom: 1px solid #1c2030;
    margin-bottom: 2.2rem;
    width: 100%;
    animation: slideDown 0.5s cubic-bezier(0.22,1,0.36,1) both;
}
.nav-logo {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.35rem;
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.02em;
    line-height: 1;
}
.nav-logo span { color: #ff5c1a; }
.nav-badge {
    background: #1a1f2e;
    border: 1px solid #2a3048;
    border-radius: 999px;
    padding: 0.3rem 0.9rem;
    font-size: 0.72rem;
    font-weight: 600;
    color: #7b8aab;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}
.dot-green {
    width: 7px; height: 7px;
    background: #4ade80;
    border-radius: 50%;
    display: inline-block;
    flex-shrink: 0;
    animation: pulse-dot 1.8s infinite;
}

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 0.5rem 0 2.2rem;
}
.hero-eyebrow {
    display: inline-block;
    background: rgba(255,92,26,0.12);
    border: 1px solid rgba(255,92,26,0.3);
    color: #ff7a45;
    font-size: 0.73rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.3rem 1rem;
    border-radius: 999px;
    margin-bottom: 1.1rem;
    animation: popIn 0.5s 0.1s cubic-bezier(0.22,1,0.36,1) both;
}
.hero-h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.9rem, 5vw, 2.9rem);
    font-weight: 800;
    color: #fff;
    line-height: 1.1;
    letter-spacing: -0.03em;
    margin-bottom: 0.75rem;
    text-align: center;
    animation: slideUp 0.55s 0.18s cubic-bezier(0.22,1,0.36,1) both;
}
.hero-h1 span { color: #ff5c1a; }
.hero-p {
    font-size: 0.97rem;
    color: #7b8aab;
    max-width: 480px;
    margin: 0 auto 0;   /* ← back to auto = centered */
    line-height: 1.65;
    text-align: center; /* ← center the text too */
    animation: slideUp 0.55s 0.28s cubic-bezier(0.22,1,0.36,1) both;
}

/* ── TRUST STRIP ── */
.trust-strip {
    display: flex;
    justify-content: center;
    gap: 0;
    margin: 2rem 0 2.5rem;
    background: #0f1118;
    border: 1px solid #1c2030;
    border-radius: 14px;
    overflow: hidden;
    animation: slideUp 0.55s 0.38s cubic-bezier(0.22,1,0.36,1) both;
}
.trust-item {
    text-align: center;
    flex: 1;
    padding: 1rem 0.5rem;
    border-right: 1px solid #1c2030;
    transition: background 0.22s ease, transform 0.22s ease;
    cursor: default;
}
.trust-item:last-child { border-right: none; }
.trust-item:hover {
    background: #161b28;
    transform: translateY(-3px);
}
.trust-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: #fff;
    line-height: 1;
}
.trust-num span { color: #ff5c1a; }
.trust-label {
    font-size: 0.68rem;
    color: #5a6480;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-top: 0.25rem;
}

/* ── SECTION HEADER ── */
.sec-head {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.6rem;
    margin-top: 1.8rem;
    animation: slideUp 0.4s cubic-bezier(0.22,1,0.36,1) both;
}
.sec-icon {
    width: 28px; height: 28px;
    background: rgba(255,92,26,0.12);
    border-radius: 7px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.85rem;
    flex-shrink: 0;
    transition: background 0.2s ease, transform 0.2s ease;
}
.sec-head:hover .sec-icon {
    background: rgba(255,92,26,0.22);
    transform: rotate(-8deg) scale(1.1);
}
.sec-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #ff5c1a;
    line-height: 1;
}

/* ── WIDGET OVERRIDES ── */
div[data-testid="stNumberInput"] input {
    background-color: #161b28 !important;
    border: 1px solid #242c3f !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
    font-size: 0.95rem !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: #ff5c1a !important;
    box-shadow: 0 0 0 3px rgba(255,92,26,0.15) !important;
    outline: none !important;
}
div[data-testid="stSelectbox"] > div > div {
    background-color: #161b28 !important;
    border: 1px solid #242c3f !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
    transition: border-color 0.2s ease !important;
}
div[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: #ff5c1a !important;
    box-shadow: 0 0 0 3px rgba(255,92,26,0.15) !important;
}
label[data-testid="stWidgetLabel"] p {
    color: #7b8aab !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
}
div[data-testid="stAlert"] { border-radius: 12px !important; }

/* ── CTA BUTTON ── */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #ff5c1a 0%, #ff8c42 100%) !important;
    color: #fff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.8rem 2rem !important;
    width: 100% !important;
    letter-spacing: 0.01em !important;
    box-shadow: 0 4px 24px rgba(255,92,26,0.35) !important;
    transition: box-shadow 0.2s ease, transform 0.15s ease !important;
    margin-top: 0.5rem !important;
    animation: float 3s ease-in-out infinite !important;
}
div[data-testid="stButton"] > button:hover {
    box-shadow: 0 8px 36px rgba(255,92,26,0.6) !important;
    transform: translateY(-3px) scale(1.01) !important;
    animation: none !important;
}
div[data-testid="stButton"] > button:active {
    transform: translateY(0px) scale(0.99) !important;
}

/* ── RESULT ── */
.result-wrap {
    margin-top: 1.5rem;
    animation: fadeUp 0.4s cubic-bezier(0.22,1,0.36,1) both;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
.result-card {
    background: linear-gradient(135deg, #ff5c1a 0%, #ff9556 100%);
    border-radius: 20px;
    padding: 2.2rem 2rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 16px 56px rgba(255,92,26,0.38);
    animation: popIn 0.5s cubic-bezier(0.22,1,0.36,1) both;
}
.result-card::before {
    content: '';
    position: absolute;
    top: -50px; right: -50px;
    width: 180px; height: 180px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
    pointer-events: none;
    animation: float 4s ease-in-out infinite;
}
.result-card::after {
    content: '';
    position: absolute;
    bottom: -70px; left: -40px;
    width: 220px; height: 220px;
    background: rgba(0,0,0,0.07);
    border-radius: 50%;
    pointer-events: none;
    animation: float 5s ease-in-out infinite reverse;
}
.result-eyebrow {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.65);
    margin-bottom: 0.45rem;
    position: relative; z-index: 1;
}
.result-time {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 5.5rem;
    font-weight: 800;
    color: #fff;
    line-height: 1;
    letter-spacing: -0.05em;
    position: relative; z-index: 1;
}
.result-unit {
    font-size: 1.05rem;
    font-weight: 600;
    color: rgba(255,255,255,0.7);
    margin-top: 0.25rem;
    margin-bottom: 1.5rem;
    position: relative; z-index: 1;
}
.pill-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    justify-content: center;
    position: relative; z-index: 1;
}
.pill {
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.28);
    border-radius: 999px;
    padding: 0.28rem 0.8rem;
    font-size: 0.78rem;
    color: #fff;
    font-weight: 600;
    transition: background 0.2s ease, transform 0.2s ease;
}
.pill:hover {
    background: rgba(255,255,255,0.28);
    transform: translateY(-2px);
}

/* ── BREAKDOWN CARDS ── */
.breakdown-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0.7rem;
    margin-top: 0.9rem;
}
.bk-card {
    background: #0f1118;
    border: 1px solid #1c2030;
    border-radius: 14px;
    padding: 1rem 0.75rem;
    text-align: center;
    transition: border-color 0.22s ease, transform 0.22s ease, box-shadow 0.22s ease;
}
.bk-card:hover {
    border-color: #ff5c1a;
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(255,92,26,0.15);
}
.bk-icon { font-size: 1.35rem; margin-bottom: 0.3rem; line-height: 1; }
.bk-val {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    color: #fff;
    line-height: 1.2;
}
.bk-lbl {
    font-size: 0.67rem;
    color: #5a6480;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-top: 0.2rem;
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    margin-top: 3.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid #1c2030;
    font-size: 0.76rem;
    color: #3a4260;
}
.footer b { color: #5a6480; }
</style>
""", unsafe_allow_html=True)


# ── Load model & encoders ─────────────────────────────────────────────────────
@st.cache_resource
def load_artifacts():
    with open('optimized_rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('label_encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
    return model, encoders

try:
    optimized_rf_model, label_encoders = load_artifacts()
except Exception as e:
    st.error(f"Could not load model files: {e}")
    st.stop()


# ── NAVBAR ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
    <div class="nav-logo">Deliver<span>IQ</span></div>
    <div class="nav-badge"><span class="dot-green"></span>Model Active</div>
</div>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">⚡ AI-Powered Prediction</div>
    <div class="hero-h1">Know your delivery time<br><span>before you order.</span></div>
    <div class="hero-p">Enter a few details and our Random Forest model instantly
    estimates how long your food will take down to the minute.</div>
</div>
""", unsafe_allow_html=True)


# ── TRUST STRIP ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="trust-strip">
    <div class="trust-item">
        <div class="trust-num">98<span>%</span></div>
        <div class="trust-label">Accuracy</div>
    </div>
    <div class="trust-item">
        <div class="trust-num">7</div>
        <div class="trust-label">Features</div>
    </div>
    <div class="trust-item">
        <div class="trust-num">&lt;1<span>s</span></div>
        <div class="trust-label">Prediction</div>
    </div>
    <div class="trust-item">
        <div class="trust-num">RF</div>
        <div class="trust-label">Algorithm</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── SECTION: Route & Timing ───────────────────────────────────────────────────
st.markdown("""
<div class="sec-head">
    <div class="sec-icon">📍</div>
    <div class="sec-title">Route &amp; Timing </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    distance_km = st.number_input(
        'Distance (km)', min_value=0.1, max_value=100.0, value=10.0, step=0.1,
        help="Distance from restaurant to delivery point"
    )
with col2:
    preparation_time_min = st.number_input(
        'Preparation time (min)', min_value=1, max_value=60, value=20,
        help="How long the restaurant takes to prepare the order"
    )
time_of_day_options = label_encoders['Time_of_Day'].classes_
time_of_day_selected = st.selectbox(
    'Time of day', time_of_day_options,
    help="The time period when the order is placed"
)


# ── SECTION: Weather & Traffic ────────────────────────────────────────────────
st.markdown("""
<div class="sec-head">
    <div class="sec-icon">🌦</div>
    <div class="sec-title">Weather &amp; Traffic</div>
</div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    weather_options = label_encoders['Weather'].classes_
    weather_selected = st.selectbox(
        'Weather conditions', weather_options,
        help="Current weather at time of delivery"
    )
with col4:
    traffic_level_options = label_encoders['Traffic_Level'].classes_
    traffic_level_selected = st.selectbox(
        'Traffic level', traffic_level_options,
        help="Current road traffic density"
    )


# ── SECTION: Courier ──────────────────────────────────────────────────────────
st.markdown("""
<div class="sec-head">
    <div class="sec-icon">🏍</div>
    <div class="sec-title">Courier Details</div>
</div>
""", unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
    vehicle_type_options = label_encoders['Vehicle_Type'].classes_
    vehicle_type_selected = st.selectbox(
        'Vehicle type', vehicle_type_options,
        help="Mode of transport used by the courier"
    )
with col6:
    courier_experience_yrs = st.number_input(
        'Courier experience (yrs)', min_value=0.0, max_value=20.0, value=2.0, step=0.1,
        help="Years of experience the courier has on the job"
    )


# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown('<div style="margin-top:1.5rem;"></div>', unsafe_allow_html=True)

if st.button('🔮  Predict My Delivery Time'):

    weather_encoded       = label_encoders['Weather'].transform([weather_selected])[0]
    traffic_level_encoded = label_encoders['Traffic_Level'].transform([traffic_level_selected])[0]
    time_of_day_encoded   = label_encoders['Time_of_Day'].transform([time_of_day_selected])[0]
    vehicle_type_encoded  = label_encoders['Vehicle_Type'].transform([vehicle_type_selected])[0]

    input_data = pd.DataFrame(
        [[distance_km, weather_encoded, traffic_level_encoded, time_of_day_encoded,
          vehicle_type_encoded, preparation_time_min, courier_experience_yrs]],
        columns=['Distance_km', 'Weather', 'Traffic_Level', 'Time_of_Day',
                 'Vehicle_Type', 'Preparation_Time_min', 'Courier_Experience_yrs']
    )

    prediction = optimized_rf_model.predict(input_data)[0]

    if prediction < 25:
        speed_label = "⚡ Express"
    elif prediction < 40:
        speed_label = "🟢 On-time"
    elif prediction < 55:
        speed_label = "🟡 Standard"
    else:
        speed_label = "🔴 Slow conditions"

    transit = max(0, prediction - preparation_time_min)

    st.markdown(f"""
<div class="result-wrap">
    <div class="result-card">
        <div class="result-eyebrow">Estimated Delivery Time</div>
        <div class="result-time">{prediction:.0f}</div>
        <div class="result-unit">minutes</div>
        <div class="pill-row">
            <div class="pill">📍 {distance_km} km</div>
            <div class="pill">🌤 {weather_selected}</div>
            <div class="pill">🚦 {traffic_level_selected}</div>
            <div class="pill">🏍 {vehicle_type_selected}</div>
            <div class="pill">{speed_label}</div>
        </div>
    </div>
    <div class="breakdown-grid">
        <div class="bk-card">
            <div class="bk-icon">🍳</div>
            <div class="bk-val">{preparation_time_min} min</div>
            <div class="bk-lbl">Prep time</div>
        </div>
        <div class="bk-card">
            <div class="bk-icon">⏱</div>
            <div class="bk-val">{transit:.0f} min</div>
            <div class="bk-lbl">Transit time</div>
        </div>
        <div class="bk-card">
            <div class="bk-icon">🎯</div>
            <div class="bk-val">{courier_experience_yrs:.0f} yrs</div>
            <div class="bk-lbl">Courier exp.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Powered by <b>Random Forest ML</b> · Built with Streamlit · DeliverIQ © 2025
</div>
""", unsafe_allow_html=True)



# python3 -m streamlit run app.py