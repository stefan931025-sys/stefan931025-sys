import os

# Set your master portfolio link here (or load from environment variable)
GOOGLE_DRIVE_URL = os.getenv(
    "PORTFOLIO_DRIVE_URL",
    "https://drive.google.com/drive/folders/YOUR_ACTUAL_FOLDER_ID",
)


def generate_readme():
    with open("README_template.md", "r", encoding="utf-8") as template_file:
        content = template_file.read()

    # Dynamic status badges header
    badges = (
        "![Sync Status](https://github.com/stefan931025-sys/stefan931025-sys/actions/workflows/auto_update_portfolio.yml/badge.svg)\n"
        "![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)\n"
        "![License](https://img.shields.io/badge/License-MIT-green.svg)\n\n"
    )

    # Automatically replace placeholding URLs
    content = content.replace(
        "https://drive.google.com", GOOGLE_DRIVE_URL
    )

    # Prepend badges to the top
    final_readme = badges + content

    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(final_readme)

    print("[✓] README.md dynamic build completed!")


if __name__ == "__main__":
    generate_readme()
