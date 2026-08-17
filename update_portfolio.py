import os

# Fetch Drive URL from GitHub Repository Variables (defaults to placeholder if unconfigured)
DEFAULT_DRIVE_URL = "https://drive.google.com"
PORTFOLIO_DRIVE_URL = os.getenv("PORTFOLIO_DRIVE_URL", DEFAULT_DRIVE_URL)


def generate_readme():
    # Read the master template
    with open("README_template.md", "r", encoding="utf-8") as template_file:
        content = template_file.read()

    # Prepend dynamic status badges
    badges = (
        "![Sync Status](https://github.com/stefan931025-sys/stefan931025-sys/actions/workflows/auto_update_portfolio.yml/badge.svg)\n"
        "![Python](https://img.shields.io/badge/Python-3.10-blue.svg)\n"
        "![License](https://img.shields.io/badge/License-MIT-green.svg)\n\n"
    )

    # Automatically swap placeholder URLs with your environment variable
    updated_content = content.replace("https://drive.google.com", PORTFOLIO_DRIVE_URL)

    final_readme = badges + updated_content

    # Overwrite README.md
    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(final_readme)

    print(f"[✓] README.md dynamic build completed using Drive URL: {PORTFOLIO_DRIVE_URL}")


if __name__ == "__main__":
    generate_readme()
