# 📄 Resume Analyzer CLI Tool

A simple Python command-line tool that analyzes your PDF resume, counts the presence of key technical and soft skills, and suggests improvements based on missing keywords.

Built using `PyMuPDF` and `Rich` for stylish terminal output.

---

## ✅ Features

- 📥 Accepts any `.pdf` resume
- 🔍 Extracts text using **PyMuPDF**
- 📊 Counts mentions of key skills (e.g., Python, SQL, ML, etc.)
- 💡 Suggests missing skills to improve your resume
- 🎨 Beautiful terminal display using the `rich` library

---

## 🧰 Tech Stack

- Python 3.x
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- [Rich](https://github.com/Textualize/rich) for CLI formatting

---

## 📦 Installation

Install required packages:

```bash
pip install PyMuPDF rich
