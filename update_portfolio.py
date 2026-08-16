import os

# ==============================================================================
# CONFIGURATION: Replace these placeholder URLs with your actual links
# ==============================================================================
CONFIG = {
    "GITHUB_USERNAME": "stefan931025-sys",
    "LINKEDIN_URL": "https://www.linkedin.com/in/YOUR_LINKEDIN_PROFILE",
    "DRIVE_MASTER_FOLDER": "https://drive.google.com/drive/folders/YOUR_MASTER_FOLDER_ID",
    
    # Pillar 1 Repositories
    "REPO_GARCH_LSTM": "https://github.com/stefan931025-sys/YOUR_GARCH_LSTM_REPO",
    "REPO_MACRO_ENGINE": "https://github.com/stefan931025-sys/YOUR_MACRO_ENGINE_REPO",
    
    # Pillar 2 Research Artifacts
    "DRIVE_PITCH_DECK": "https://drive.google.com/file/d/YOUR_PITCH_DECK_FILE_ID",
    "DRIVE_VALUATION_MODEL": "https://drive.google.com/file/d/YOUR_VALUATION_MODEL_FILE_ID",
    "DRIVE_SIMULATIONS_FOLDER": "https://drive.google.com/drive/folders/YOUR_SIMULATIONS_FOLDER_ID",
}


def generate_readme_content(config: dict) -> str:
    """Generates the Master Portfolio README markdown content with dynamic links."""
    return f"""# Tshepo Stefan Kotelo | Quantitative & Discretionary Macro Portfolio

> **Buy-Side Trading & Financial Analytics** | CFA Level 1 Candidate • FMVA Candidate  
> *Specializing in quantitative volatility forecasting, automated macro execution engines, and fundamental equity research.*

---

## Executive Summary & Technical Architecture

This portfolio showcases an end-to-end suite of quantitative trading systems, discretionary macro execution tools, and institutional equity research. The work bridges **data science (Python, GARCH, LSTM, PyTorch)** with **discretionary macro trading** and **buy-side financial modeling**.

