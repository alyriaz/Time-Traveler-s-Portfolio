# 🚀 Time Traveler's Portfolio

**Course Name:** AF3005 – Programming for Finance  
**Instructor:** Usama Janjua

---

## 🧠 App Overview

**Time Traveler’s Portfolio** is a futuristic finance simulation dashboard built using Streamlit. This app enables users to analyze historical stock data, predict future prices using machine learning, visualize growth over time, and explore correlations with major tech stocks.

Inspired by **cyberpunk aesthetics**, the app features a **neon-on-dark theme**, matrix-style intro animation, custom fonts, and interactive charts to create an immersive analytical experience.

---

## 🔍 Features

### 📈 Stock Simulation
- Input stock ticker, amount, and start date
- Auto-fetch from Yahoo Finance or upload custom CSV
- Calculate ROI, price change, and investment performance

### 🧠 Machine Learning Forecasting
- Implements **Linear Regression** to predict stock prices
- Uses `sklearn` to train and evaluate the model
- Model is trained on daily closing prices with time (day index) as the independent variable
- Evaluates accuracy using **Mean Squared Error (MSE)**
- Predicts up to 180 future prices and allows downloading results

### 📊 Visualizations
- Interactive investment growth line chart (Plotly)
- Neon-themed correlation matrix with tech stocks (Seaborn)
- Custom matrix-style animated background for intro

### 🧙 Investment Advice Generator
- Randomly cycles investment tips to simulate market wisdom

---

## 🌌 Thematic Design

- **Theme**: Cyberpunk, hacker-console aesthetic
- **Font**: [Orbitron](https://fonts.google.com/specimen/Orbitron) (monospace, futuristic)
- **Color Scheme**:  
  - Background: `#0e0e1f`  
  - Primary Highlight: `#00ffe5`  
  - Accent Color: `#ff00cc`  
- **Animations**: Matrix-style falling code using HTML canvas and JavaScript

---

## 🚀 Deployment

**Live App:** [Click here to try it on Streamlit Cloud]([https://your-streamlit-deployment-link](https://time-traveler-s-portfolio-jggufziou5u3lfhcqverk3.streamlit.app/))


---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/time-travelers-portfolio.git
   cd time-travelers-portfolio

