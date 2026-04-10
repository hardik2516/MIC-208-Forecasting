<div align="center">

# 📈 Sales Forecasting Dashboard

### A premium, interactive time-series forecasting tool built with Streamlit & Plotly

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-22D3EE?style=for-the-badge)](LICENSE)

<br />

<img src="preview.png" alt="Dashboard Preview" width="100%" style="border-radius: 12px; box-shadow: 0 20px 60px rgba(0,0,0,0.3);" />

<br />

*A sleek, dark-themed dashboard for analyzing historical writing‑paper sales using classical forecasting methods — SMA, WMA & Exponential Smoothing.*

---

</div>

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **Premium Dark UI** | Glassmorphism cards, gradient accents, Inter typography, and micro-animations |
| 📉 **Interactive Charts** | Plotly-powered with hover tooltips, unified crosshair, and smooth rendering |
| 📊 **KPI Metric Cards** | At-a-glance view of Latest Sales, Average, Peak, and Best Model |
| 🔧 **Real-time Controls** | Sidebar sliders for window size (n) and smoothing factor (α) |
| ✅ **Toggle Forecasts** | Show/hide individual models (SMA, WMA, Exponential) via checkboxes |
| 📐 **MAE Comparison** | Side-by-side bar chart comparing model accuracy |
| 🗂️ **Data Table** | Last 12 months of data with all computed forecasts |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sales-forecasting-dashboard.git
cd sales-forecasting-dashboard
```

### 2. Install Dependencies

```bash
pip install streamlit pandas numpy plotly matplotlib
```

### 3. Run the Dashboard

```bash
streamlit run app.py
```

The app will open automatically at **http://localhost:8501** 🎉

---

## 📂 Project Structure

```
forecasting/
├── app.py                              # Main Streamlit dashboard application
├── monthly-writing-paper-sales.csv     # Historical sales dataset (147 months)
├── Forcasting.ipynb                    # Jupyter notebook (exploratory analysis)
├── preview.png                         # Dashboard screenshot
└── README.md                           # You are here
```

---

## 📊 Forecasting Methods

### Simple Moving Average (SMA)

Computes the unweighted mean of the previous *n* data points. Best for smoothing out short-term fluctuations.

$$\text{SMA}_t = \frac{1}{n} \sum_{i=0}^{n-1} x_{t-i}$$

### Weighted Moving Average (WMA)

Assigns linearly increasing weights to more recent observations, making it more responsive to recent changes than SMA.

$$\text{WMA}_t = \frac{\sum_{i=0}^{n-1} (n - i) \cdot x_{t-i}}{\sum_{i=1}^{n} i}$$

### Exponential Smoothing

Applies exponentially decreasing weights using smoothing factor *α*. Higher *α* values give more weight to recent data.

$$\hat{x}_t = \alpha \cdot x_t + (1 - \alpha) \cdot \hat{x}_{t-1}$$

---

## 🎛️ Dashboard Controls

| Control | Location | Range | Default | Effect |
|---|---|---|---|---|
| **Window Size (n)** | Sidebar | 2 – 12 | 3 | Adjusts SMA & WMA lookback period |
| **Smoothing Factor (α)** | Sidebar | 0.05 – 1.0 | 0.5 | Controls Exponential Smoothing responsiveness |
| **Show SMA** | Sidebar | On / Off | On | Toggles SMA line on chart |
| **Show WMA** | Sidebar | On / Off | On | Toggles WMA line on chart |
| **Show Exponential** | Sidebar | On / Off | On | Toggles Exponential line on chart |

---

## 📈 Dataset

**Monthly Writing Paper Sales** — 147 monthly observations spanning **January 2001 to March 2013**.

| Property | Value |
|---|---|
| Records | 147 months |
| Time Range | Jan 2001 – Mar 2013 |
| Peak Sales | 2,941 (Oct 2011) |
| Average Sales | 1,746 |
| Format | CSV (Month, Sales) |

---

## 🛠️ Tech Stack

<table>
  <tr>
    <td align="center"><strong>Frontend</strong></td>
    <td>Streamlit, Custom CSS (Glassmorphism + Dark Theme)</td>
  </tr>
  <tr>
    <td align="center"><strong>Visualization</strong></td>
    <td>Plotly (interactive), Matplotlib (fallback)</td>
  </tr>
  <tr>
    <td align="center"><strong>Data Processing</strong></td>
    <td>Pandas, NumPy</td>
  </tr>
  <tr>
    <td align="center"><strong>Typography</strong></td>
    <td>Google Fonts (Inter)</td>
  </tr>
  <tr>
    <td align="center"><strong>Language</strong></td>
    <td>Python 3.8+</td>
  </tr>
</table>

---


<div align="center">

**Built with ❤️ using Streamlit & Plotly**

<sub>⭐ Star this repo if you found it useful!</sub>

</div>
