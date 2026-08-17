import os


def generate_readme():
    # Read template file directly to eliminate Python string parsing issues
    with open("README_template.md", "r", encoding="utf-8") as template_file:
        content = template_file.read()

    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(content)

    print("[✓] README.md updated successfully from template!")


if __name__ == "__main__":
    generate_readme()
