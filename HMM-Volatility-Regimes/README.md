# 📈 HMM & SV-HMM for Volatility Regime Analysis and Strategy Design

This repository contains a full implementation of regime-switching models for financial volatility, including:

- Static and rolling **Hidden Markov Models (HMM)**
- **Stochastic Volatility HMMs (SV-HMM)** with AR(1)-based volatility forecasting
- Filters like **MA100**, **dynamic risk control**, and **regime remapping**
- Applications to several assets: BTC, ETH, SP500, AAPL, WTI

---

## 🧠 Project Overview

All experiments were conducted and explained in the PDF report.  
Strategies include:

- **HMM Static** (fixed sample, full fit)
- **HMM Rolling** (with MA100 filter and reclassification by volatility)
- **SV-HMM** (AR(1) forecast of volatility per regime)
- **SV-HMM with trend filter** (modulated signal if volatility is high or trend is negative)

---

## 📁 Repository Structure

├── notebooks/
│ └── CompletedNB.ipynb # Central notebook with all strategies
├── report/
│ ├── Complete_article-23.pdf # Final report (full analysis)
│ └── results/
│ ├── HMM_static.png
│ ├── HMM_panic_rolling.png
│ ├── SVHMM_BTC.png
│ ├── SVHMM_ETH.png
│ ├── SVHMM_WTI.png
│ ├── SVHMM_rolling_panic.png
│ └── SVHMM_Static.png
├── src/
│ ├── analysis/
│ ├── backtests/
│ ├── benchmarks/
│ ├── hmm_static_analysis/
│ ├── models/
│ └── optimization/

---

## 📄 Final Report

👉 The full write-up is available here:  
[`report/Complete_article-23.pdf`](report/Complete_article-23.pdf)

It includes:

- Explanation of HMM and SV-HMM logic
- Volatility regime classification
- Trend and volatility filtering
- Strategy design choices
- Comparative performance
- Asset-specific insights

All results and visualizations are also included in the `report/results/` folder.

---

## 💻 Run the Notebook

```bash
# Clone the repo
git clone https://github.com/your_username/your_repo_name.git
cd your_repo_name

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook notebooks/CompletedNB.ipynb
```
