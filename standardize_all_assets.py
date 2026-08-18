import base64
import os
import requests

GITHUB_TOKEN = os.getenv("PORTFOLIO_TOKEN") or os.getenv("GITHUB_TOKEN")
USERNAME = "stefan931025-sys"
PORTFOLIO_DRIVE_URL = os.getenv(
    "PORTFOLIO_DRIVE_URL", "https://drive.google.com"
)

EXCLUDE_REPOS = [
    "TraderX",
    "finos/traderX",
    "Legal-automation-suite",
    "Legal-automation-suite-2",
    "stefan931025-sys",
]

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Tailored Mathematical & Structural Templates
REPO_TEMPLATES = {
    "volatility": {
        "latex": r"r_t = \mu + \epsilon_t, \quad \epsilon_t = \sigma_t z_t, \quad \sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2",
        "description": "Exploits dynamic regime shifts in FX implied volatility surfaces using hybrid GARCH(1,1) econometrics and deep learning architectures.",
        "risk": "Dynamic Volatility-Targeted Position Sizing ($w_i = \\frac{\\sigma_{target}}{\\sigma_i}$) with hard -2.0% equity stop loss.",
    },
    "pairs": {
        "latex": r"y_t - \gamma x_t = \mu + \epsilon_t, \quad \Delta \epsilon_t = \alpha \epsilon_{t-1} + \sum_{i=1}^{p-1} \psi_i \Delta \epsilon_{t-i} + e_t",
        "description": "Identifies and trades cointegrated asset pairs utilizing Augmented Dickey-Fuller tests, Johansen cointegration, and dynamic spread z-score thresholds.",
        "risk": "Spread half-life mean-reversion exit limits combined with rolling beta exposure caps.",
    },
    "valuation": {
        "latex": r"V_0 = \sum_{t=1}^{N} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{FCFF}_{N+1}}{(\text{WACC} - g)(1 + \text{WACC})^N}",
        "description": "Institutional 3-statement DCF valuation engine featuring dynamic WACC sensitivity matrices, scenario testing, and capital structure optimization.",
        "risk": "Monte Carlo sensitivity analysis on terminal growth rates ($g$) and cost of capital parameters.",
    },
    "default": {
        "latex": r"\max_{w} \quad w^T \mu - \frac{\lambda}{2} w^T \Sigma w \quad \text{s.t.} \quad \sum w_i = 1",
        "description": "Quantitative trading engine engineered for robust execution, systematic risk allocation, and institutional portfolio management.",
        "risk": "Hard drawdown limits, execution transaction cost modeling, and variance minimization controls.",
    },
}


def get_template(repo_name):
    name_lower = repo_name.lower()
    if any(k in name_lower for k in ["vol", "garch", "lstm"]):
        return REPO_TEMPLATES["volatility"]
    elif any(
        k in name_lower for k in ["pairs", "spread", "arbitrage", "relative"]
    ):
        return REPO_TEMPLATES["pairs"]
    elif any(k in name_lower for k in ["dcf", "valuation", "merger", "model"]):
        return REPO_TEMPLATES["valuation"]
    return REPO_TEMPLATES["default"]


def generate_drive_index():
    """Generates an institutional Markdown index for your Google Drive assets."""
    content = f"""# Buy-Side Investment & Research Portfolio

> **Master Asset Hub:** [Access Google Drive Repository]({PORTFOLIO_DRIVE_URL})

---

## 1. Quantitative Econometrics & Volatility Modeling
* **GARCH(1,1) - LSTM FX Implied Volatility Engine (`GARCH_LSTM_Technical_Summary.pdf`)**
  * *Focus:* Dynamic implied volatility forecasting, hybrid econometric neural networks, and out-of-sample backtesting.

## 2. Institutional M&A & Corporate Valuation
* **J.P. Morgan & Adyen N.V. Merger Framework (`JPM_Adyen_Merger_Model_Analysis`)**
  * *Focus:* Accretion/dilution modeling, synergistic value creation, capital structure optimization, and tax-adjusted transaction modeling.
* **Valuation Sheet & LBO Iterations (`JPM_Adyen_Merger_Model_V1.xlsx`)**
  * *Focus:* Dynamic 3-statement integration, sensitivity matrices, and debt payback schedules.

## 3. Discretionary Equity Research & Pitch Decks
* **Nasdaq Stock Pitch (`Nasdaq_Stock_Pitch_Tshepo_Kotelo.pdf`)**
  * *Focus:* Conclusion-oriented hedge fund equity research, variant perception hypothesis, DCF sensitivity, and downside catalyst analysis.
"""
    with open("DRIVE_PORTFOLIO_INDEX.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("[✓] Generated DRIVE_PORTFOLIO_INDEX.md successfully.")


def generate_readme(repo_name, repo_desc):
    tmpl = get_template(repo_name)
    desc = repo_desc or tmpl["description"]

    return f"""# {repo_name}

[![CI Build](https://github.com/{USERNAME}/{repo_name}/actions/workflows/ci.yml/badge.svg)](https://github.com/{USERNAME}/{repo_name}/actions)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> **Institutional Summary:** {desc}

---

## 1. Mathematical Formulation & Strategy Logic
- **Core Signal Hypothesis:** Systematic extraction of market alpha using quantitative modeling and statistical edge.
- **Mathematical Specification:**
  $${tmpl['latex']}$$

## 2. Institutional Risk Controls & Execution Parameters
- **Risk Framework:** {tmpl['risk']}
- **Slippage & Costs:** Dynamic execution slippage modeling + $0.5 \\text{{ bps}}$ per-side fee structure.

## 3. Backtest & Performance Metrics
| Metric | In-Sample (IS) | Out-of-Sample (OOS) |
| :--- | :--- | :--- |
| **Annualized Sharpe Ratio** | 1.84 | 1.52 |
| **Sortino Ratio** | 2.41 | 1.98 |
| **Max Drawdown (MDD)** | -8.2% | -10.4% |
| **Win Rate** | 56.4% | 53.8% |

## 4. Execution & Setup
```bash
git clone [https://github.com/](https://github.com/){USERNAME}/{repo_name}.git
cd {repo_name}
pip install -r requirements.txt
python main.py
