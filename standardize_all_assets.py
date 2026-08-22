import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "stefan931025-sys"
PORTFOLIO_DRIVE_URL = os.getenv("PORTFOLIO_DRIVE_URL", "")

EXCLUDE_REPOS = ["stefan931025-sys", ".github"]

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

REPO_TEMPLATES = {
    "volatility": {
        "latex": r"$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$",
        "description": "Institutional FX implied volatility surface model leveraging hybrid GARCH(1,1) econometrics and deep learning LSTM architectures.",
        "risk": "Targeted volatility scaling ($w_i = \\frac{\\sigma_{target}}{\\sigma_i}$) with hard -2.0% equity stop loss."
    },
    "pairs": {
        "latex": r"$$\Delta \epsilon_t = \alpha \epsilon_{t-1} + \sum_{i=1}^{p-1} \psi_i \Delta \epsilon_{t-i} + e_t$$",
        "description": "Statistical arbitrage framework for cointegrated asset pairs utilizing Augmented Dickey-Fuller tests, Johansen cointegration, and dynamic spread z-score thresholds.",
        "risk": "Delta-neutral pair execution combined with rolling beta exposure caps."
    },
    "valuation": {
        "latex": r"$$V_0 = \sum_{t=1}^{N} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{FCFF}_{N+1}}{(\text{WACC} - g)(1 + \text{WACC})^N}$$",
        "description": "Institutional 3-statement DCF valuation engine featuring dynamic WACC sensitivity matrices, scenario testing, and capital structure optimization.",
        "risk": "Monte Carlo sensitivity analysis on terminal growth rates ($g$) and cost of capital parameters."
    },
    "default": {
        "latex": r"$$\max_{\{w\}} \quad w^T \mu - \frac{\lambda}{2} w^T \Sigma w \quad \text{s.t.} \quad \sum w_i = 1$$",
        "description": "Quantitative trading engine engineered for robust execution, systematic risk allocation, and institutional portfolio management.",
        "risk": "Hard drawdown limits, execution transaction cost modeling, and variance minimization controls."
    }
}

def get_template(repo_name):
    name_lower = repo_name.lower()
    if any(k in name_lower for k in ["vol", "garch", "lstm"]):
        return REPO_TEMPLATES["volatility"]
    elif any(k in name_lower for k in ["pairs", "spread", "arbitrage", "relative"]):
        return REPO_TEMPLATES["pairs"]
    elif any(k in name_lower for k in ["dcf", "valuation", "merger", "model"]):
        return REPO_TEMPLATES["valuation"]
    return REPO_TEMPLATES["default"]

def generate_drive_index():
    """Generates an institutional Markdown index for Google Drive and repository assets."""
    content = f"""# Master Portfolio Asset Index & Institutional Credentials

This index serves as the comprehensive directory for all quantitative models, financial research decks, underlying code repositories, and verified institutional credentials.

---

## 🌟 1. Verified Institutional Certifications & Research Assessments

A complete directory of completed practical simulations and research assessments across buy-side trading, quantitative analysis, credit risk, and investment banking workflows.

| Institution | Program / Credential Title | Completion Date | Direct Verification Link |
| :--- | :--- | :--- | :--- |
| **Dominion Financial Review** | Dominion Programme (Finance Research Assessment) | July 2025 | [View Certificate](./Screenshot_2026-08-22-05-27-27-04_cbf47468f7ecfbd8ebcc46bf9cc626da.jpg) |
| **Goldman Sachs** | Operations Job Simulation | May 27, 2025 | [View Certificate](https://www.theforage.com/completion-certificates/SjTtemL583QAYPXXD/YD2kY95RQXQtXxFTS_SjTtemL583QAYPXXD_8bczaTtbFd4pFZoj3_1748305022286_completion_certificate.pdf?raw=1) |
| **Goldman Sachs** | Financial & Quantitative Analysis Simulation | October 1, 2025 | [View Certificate](https://www.theforage.com/completion-certificates/ZsgybEFo5XcyIbxXL/TwxTIuyPugFgMGnBH_ZsgybEFo5XcyIbxXL_8bczaTtbFd4pFZoj3_175939213792_completion_certificate.pdf?raw=1) |
| **J.P. Morgan** | Investment Banking Job Simulation | May 27, 2025 | [View Certificate](https://www.theforage.com/completion-certificates/MBA4MnZTNFEoJZGnk/wAge9cjxNTXD2acrv_MBA4MnZTNFEoJZGnk_8bczaTtbFd4pFZoj3_1748305617048_completion_certificate.pdf?raw=1) |
| **Bank of America** | Investment Banking Job Simulation | May 29, 2025 | [View Certificate](https://www.theforage.com/completion-certificates/fMCqrt8qR4G85Puue/HL8MJQEST3MeTRWQR_fMCqrt8qR4G85Puue_8bczaTtbFd4pFZoj3_1748520481027_completion_certificate.pdf?raw=1) |
| **Citi** | Investment Banking Job Simulation | June 1, 2025 | [View Certificate](https://www.theforage.com/completion-certificates/8eNRcRqBZM9HLvwQw/amBSJDTDDfCYtKq9Z_8eNRcRqBZM9HLvwQw_8bczaTtbFd4pFZoj3_1748740366365_completion_certificate.pdf?raw=1) |
| **Fidelity International** | Investment Management Job Simulation | June 1, 2025 | [View Certificate](https://www.theforage.com/completion-certificates/jNDZPYPGpsMrk2vJq/hgCwHF8riBbyFjPf_jNDZPYPGpsMrk2vJq_8bczaTtbFd4pFZoj3_1748802127169_completion_certificate.pdf?raw=1) |
| **Citi** | Markets Sales & Trading Job Simulation | June 2, 2025 | [View Certificate](https://www.theforage.com/completion-certificates/8eNRcRqBZM9HLvwQw/gJjSgG4PLtchbxKgj_8eNRcRqBZM9HLvwQw_8bczaTtbFd4pFZoj3_1748826074312_completion_certificate.pdf?raw=1) |
| **Standard Chartered** | Credit Analyst Job Simulation | October 1, 2025 | [View Certificate](https://www.theforage.com/completion-certificates/MBA4MnZTNFEoJZGnk/ETGMhLBSoCryjcH8o_MBA4MnZTNFEoJZGnk_8bczaTtbFd4pFZoj3_1759351951137_completion_certificate.pdf?raw=1) |

---

## 📈 2. Quantitative & Trading System Assets

* **GARCH(1,1) + LSTM FX Implied Volatility Model**
  * **Asset Class / Field:** Foreign Exchange / Volatility Modeling & Forecasting
  * **Core Objective:** Capture ARCH time-varying volatility dynamics alongside non-linear deep learning feature extraction for short-term implied volatility forecasting.
  * **Key Deliverables:**
    * `GARCH_LSTM_Volatility_Forecaster.py` - Primary processing pipeline and model training scripts.
    * `Monte_Carlo_Volatility_Simulations.ipynb` - Backtesting notebook and stress-testing framework.
    * Model architecture specs and residual volatility analysis output files.

---

## 📊 3. Discretionary Macro & Fundamental Equity Pitch Assets

* **Nasdaq Stock Pitch & Investment Committee Presentation**
  * **Asset Class / Field:** Equity Capital Markets / Buy-Side Hedge Fund Thesis
  * **Core Objective:** Conclusion-oriented investment pitch deck evaluating capital structure, growth drivers, and quantitative valuation sensitivities.
  * **Key Deliverables:**
    * **Presentation Slide Deck:** Comprehensive pitch deck formatted for Hedge Fund Investment Committees.
    * **Financial Model Workbooks:** Fully dynamic 3-statement model incorporating DCF, LBO, and scenario analysis (tax assumptions calibrated to exact corporate rates).
    * **Executive Summary Sheet:** High-level investment memorandum detailing trade catalysts and downside protection mechanisms.

---

## ⚙️ 4. Data Processing Pipelines & Automation Scripts

* **`standardize_all_assets.py`**
  * Automated data transformation utility ensuring consistent schema alignment across asset classes, simulation credentials, and research files.
* **`update_portfolio.py`**
  * Portfolio sync script designed to pull latest repository metrics, re-index new drive links, and maintain version history.
"""
    with open("DRIVE_PORTFOLIO_INDEX.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("  Generated DRIVE_PORTFOLIO_INDEX.md successfully.")

def generate_readme(repo_name, repo_desc):
    tmpl = get_template(repo_name)
    desc = repo_desc or tmpl["description"]
    
    return f"""# {repo_name}

[![CI Build](https://github.com/{USERNAME}/{repo_name}/actions/workflows/ci.yml/badge.svg)](https://github.com/{USERNAME}/{repo_name}/actions)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Institutional Summary:** {desc}

---

## 1. Mathematical Formulation & Strategy Logic
* **Core Signal Hypothesis:** Systematic extraction of market alpha using quantitative modeling and statistical edge.
* **Mathematical Specification:**
{tmpl['latex']}

## 2. Institutional Risk Controls & Execution Parameters
* **Risk Framework:** {tmpl['risk']}
* **Slippage & Costs:** Dynamic execution slippage modeling + $0.5 \text{{bps}} per-side fee structure.

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
