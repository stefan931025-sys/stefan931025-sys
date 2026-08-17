import os

# 1. Fetch Google Drive URL from GitHub Environment/Secret Variables
# Defaults to a clean placeholder if no variable is configured
DEFAULT_DRIVE_URL = "https://drive.google.com"
PORTFOLIO_DRIVE_URL = os.getenv("PORTFOLIO_DRIVE_URL", DEFAULT_DRIVE_URL)


def generate_readme():
    # Read the markdown template
    with open("README_template.md", "r", encoding="utf-8") as template_file:
        content = template_file.read()

    # Automatically swap any placeholder drive link with your actual drive variable
    updated_content = content.replace("https://drive.google.com", PORTFOLIO_DRIVE_URL)

    # Write out to README.md
    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(updated_content)

    print(f"[✓] README.md updated successfully using Drive URL: {PORTFOLIO_DRIVE_URL}")


if __name__ == "__main__":
    generate_readme()
