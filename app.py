# time_traveler_dashboard.py

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import datetime
import base64
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import time

# Set Page Config
st.set_page_config(page_title="🚀 Time Traveler's Portfolio", layout="wide")

# Custom Fonts and Theme
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"]  {
        font-family: 'Orbitron', monospace;
    }
    body, .main {
        background-color: #0e0e1f;
        color: #E0E0E0;
    }
    .css-1d391kg, .css-1d391kg:hover {
        background-color: #121226;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #00ffe5;
    }
    [data-testid="metric-container"] {
        background-color: #1c1f3a;
        border-left: 4px solid #00ffe5;
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 0 10px #00ffe566;
    }
    .stButton>button {
        background-color: #00ffe5;
        color: black;
        border: none;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff00cc;
        color: white;
    }
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #1c1f3a;
    }
    ::-webkit-scrollbar-thumb {
        background: #00ffe5;
    }
    input, textarea, .stNumberInput input, .stSlider {
        background-color: #1c1f3a;
        color: #fff;
        border: 1px solid #00ffe5;
    }
</style>
""", unsafe_allow_html=True)

# Matrix Animation HTML
matrix_html = """ 
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      margin: 0;
      background: black;
      overflow: hidden;
    }
    canvas {
      display: block;
    }
  </style>
</head>
<body>
  <canvas id="matrixCanvas"></canvas>
  <script>
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');

    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;

    const letters = 'アァイィウヴエェオカガキギクグケゲコゴサザシジスズセゼソゾタダチッヂヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤユヨラリルレロワヲンABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    const fontSize = 14;
    const columns = canvas.width / fontSize;
    const drops = Array.from({ length: columns }).fill(1);

    function draw() {
      ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.fillStyle = '#0F0';
      ctx.font = fontSize + 'px monospace';

      for (let i = 0; i < drops.length; i++) {
        const text = letters.charAt(Math.floor(Math.random() * letters.length));
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
          drops[i] = 0;
        }

        drops[i]++;
      }
    }

    setInterval(draw, 33);
  </script>
</body>
</html>
"""

# Intro Animation
if 'intro_shown' not in st.session_state:
    st.session_state.intro_shown = True
    placeholder = st.empty()
    with placeholder.container():
        components.html(matrix_html, height=600, width=800)
    time.sleep(4)
    placeholder.empty()

st.title("🗭 Time Traveler's Portfolio")
st.write("Welcome to your financial past, present, and future 📊🚀")

# Sidebar Inputs
with st.sidebar.expander("📅 Investment Setup", expanded=True):
    ticker = st.text_input("📈 Stock Symbol", "AAPL")
    start_date = st.date_input("🕰️ Start Date", datetime.date(2015, 1, 1))
    investment_amount = st.number_input("💵 Amount Invested ($)", min_value=100, value=1000)
    future_days = st.slider("📅 Days into the future", 1, 180, 30)
    uploaded_file = st.file_uploader("📤 Or upload CSV with stock data", type=["csv"])
    simulate = st.button("🚀 Simulate")

st.sidebar.markdown("---")
st.sidebar.markdown("🧠 **Simulated Sentiment**:")
sentiments = ["🚀 Bullish", "😐 Neutral", "🐻 Bearish"]
sentiment = np.random.choice(sentiments, p=[0.4, 0.4, 0.2])
st.sidebar.success(f"News Sentiment: {sentiment}")

# Main Logic (same as previous, not changed here for brevity)
# You can insert the rest of your existing code below this comment to complete functionality.


if simulate or uploaded_file is not None:
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        if 'Date' not in data.columns or 'Close' not in data.columns:
            st.error("❌ CSV must contain at least 'Date' and 'Close' columns.")
        else:
            data['Date'] = pd.to_datetime(data['Date'])
            data.sort_values('Date', inplace=True)
    else:
        data = yf.download(ticker, start=start_date)
        if data.empty:
            st.error("❌ No data found for this ticker and date range. Try again.")
        else:
            data = data[['Open', 'High', 'Low', 'Close']].dropna()
            data['Date'] = data.index
            data.reset_index(drop=True, inplace=True)

    if not data.empty and 'Close' in data.columns:
        initial_price = float(data.iloc[0]['Close'])
        final_price = float(data.iloc[-1]['Close'])
        shares = investment_amount / initial_price
        current_value = shares * final_price
        roi = ((current_value - investment_amount) / investment_amount) * 100

        col1, col2, col3 = st.columns(3)
        col1.metric("📉 Initial Price", f"${initial_price:.2f}")
        col2.metric("📈 Final Price", f"${final_price:.2f}")
        col3.metric("📊 ROI", f"{roi:.2f}%", delta=f"{final_price - initial_price:.2f}")

        st.info(f"💰 You own **{shares:.2f} shares** of **{ticker.upper()}**")
        st.success(f"💸 Portfolio Value Today: **${current_value:.2f}**")

        data['Day'] = np.arange(len(data))
        X = data[['Day']]
        y = data['Close']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression().fit(X_train, y_train)
        mse = mean_squared_error(y_test, model.predict(X_test))
        st.code(f"🖐️ Model Mean Squared Error: {mse:.2f}")


        st.subheader("📆 Investment Growth Over Time")
        data['Growth %'] = ((data['Close'] - initial_price) / initial_price) * 100
        fig_growth = go.Figure()
        fig_growth.add_trace(go.Scatter(x=data['Date'], y=data['Growth %'], mode='lines', name='Growth %'))
        fig_growth.update_layout(template="plotly_dark", title="Investment Growth (%)", xaxis_title="Date", yaxis_title="Growth %")
        st.plotly_chart(fig_growth, use_container_width=True)

        st.subheader("🔮 Future Price Prediction")
        future_day_index = len(data) + future_days
        future_price = float(model.predict(np.array([[future_day_index]]))[0])
        st.success(f"📅 In {future_days} days, {ticker.upper()} is predicted to be: **${future_price:.2f}**")

        st.subheader("📁 Download Future Price Forecast")
        last_date = data['Date'].dropna().iloc[-1] if not data['Date'].dropna().empty else data.index[-1]
        future_days_range = np.arange(len(data), len(data)+180).reshape(-1, 1)
        future_prices = model.predict(future_days_range).flatten()
        forecast_df = pd.DataFrame({
            'Date': pd.date_range(start=last_date + pd.Timedelta(days=1), periods=180),
            'Predicted Price': future_prices
        })
        csv_forecast = forecast_df.to_csv(index=False)
        b64_forecast = base64.b64encode(csv_forecast.encode()).decode()
        href_forecast = f'<a href="data:file/csv;base64,{b64_forecast}" download="future_forecast.csv">📅 Download 180-day Forecast</a>'
        st.markdown(href_forecast, unsafe_allow_html=True)

        if not uploaded_file:
            st.subheader("📈 Correlation with Popular Stocks")
            tech_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
            stock_data = yf.download(tech_stocks, start=start_date)['Close']
            stock_data = stock_data.dropna()
            correlation = stock_data.pct_change().corr()
            fig_corr, ax = plt.subplots(figsize=(8, 6), facecolor='#0e0e1f')
            sns.set(style="white")

            sns.heatmap(
                correlation,
                annot=True,
                cmap='mako',  # or try 'rocket_r', 'viridis', 'coolwarm'
                linewidths=0.5,
                linecolor='#1c1f3a',
                cbar_kws={"shrink": 0.7, 'label': 'Correlation'},
                annot_kws={"color": "white", "size": 10},
                ax=ax
            )

# Set background and label colors to match app theme
            ax.set_facecolor('#0e0e1f')
            fig_corr.patch.set_facecolor('#0e0e1f')
            ax.tick_params(colors='cyan')
            ax.xaxis.label.set_color('#00ffe5')
            ax.yaxis.label.set_color('#00ffe5')
            ax.set_title("Tech Stock Correlation Matrix", color='#00ffe5', fontsize=14)

            st.pyplot(fig_corr)


        st.subheader("💬 Investment Oracle Says...")
        advice = [
            "Buy the dip! 🕳️📉",
            "Time in the market beats timing the market ⏳📈",
            "Don’t panic. Zoom out. 📆",
            "Even Warren Buffet sleeps 🛌. Don’t overtrade!",
            "Did you diversify today? 🤔"
        ]
        st.info(np.random.choice(advice))
