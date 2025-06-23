import fitz  # PyMuPDF
import sys
import os
from collections import Counter
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Define key skills to look for
KEY_SKILLS = ["Python", "SQL", "Machine Learning", "Data Analysis", "Pandas",
              "Numpy", "Deep Learning", "AI", "TensorFlow", "Scikit-learn", "Java", "C++", "Communication", "Leadership"]

def extract_text_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        console.print(f"[red]Failed to extract text: {e}[/red]")
        sys.exit(1)

def count_skills(text, skills):
    text_lower = text.lower()
    skill_counts = {}
    for skill in skills:
        count = text_lower.count(skill.lower())
        skill_counts[skill] = count
    return skill_counts

def suggest_missing_skills(skill_counts):
    missing = [skill for skill, count in skill_counts.items() if count == 0]
    return missing

def display_results(skill_counts, missing_skills):
    table = Table(title="Resume Skill Analysis")

    table.add_column("Skill", style="cyan", no_wrap=True)
    table.add_column("Count", style="magenta")

    for skill, count in skill_counts.items():
        table.add_row(skill, str(count))

    console.print(table)

    if missing_skills:
        console.print(Panel(f"⚠️ Consider adding these skills to strengthen your resume:\n[bold yellow]{', '.join(missing_skills)}[/bold yellow]",
                            title="Suggestions", style="red"))
    else:
        console.print(Panel("🎉 Great job! All key skills are present.", title="Suggestions", style="green"))

def main():
    if len(sys.argv) != 2:
        console.print("[bold red]Usage: python resume_analyzer.py <path_to_resume.pdf>[/bold red]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.isfile(pdf_path):
        console.print(f"[bold red]File not found:[/bold red] {pdf_path}")
        sys.exit(1)
    if not pdf_path.lower().endswith('.pdf'):
        console.print(f"[bold red]The file must be a PDF:[/bold red] {pdf_path}")
        sys.exit(1)

    console.print(f"[bold green]Analyzing resume:[/bold green] {pdf_path}")

    text = extract_text_from_pdf(pdf_path)
    skill_counts = count_skills(text, KEY_SKILLS)
    missing_skills = suggest_missing_skills(skill_counts)
    display_results(skill_counts, missing_skills)

if __name__ == "__main__":
    main()
