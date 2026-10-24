# 🤖 AIML · Semester 4 · GM University

<p align="center">
  <img src="https://img.shields.io/badge/Course-UE24CS2401-6C5CE7?style=for-the-badge" alt="Course UE24CS2401" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/Learning-Labs%20%7C%20Notes%20%7C%20Practice-00A884?style=for-the-badge" alt="Learning resources" />
</p>

A student-focused collection of **Artificial Intelligence and Machine Learning** lab programs, module resources, assignments, question banks, datasets, and practical examples for GM University.

> **Learn the idea → trace the algorithm → run the code → explain the result.**

## 🧭 Start here

| Goal | Start with |
|---|---|
| Set up Python and dependencies | [Environment setup](docs/SETUP.md) |
| Find existing lab and study resources | [Lab & resource catalog](docs/LAB_CATALOG.md) |
| Follow a structured learning order | [Learning path](docs/ROADMAP.md) |
| Revise modules 1–5 | [Module study guides](docs/INDEX.md#module-guides) |
| Prepare for practicals and viva | [Exam preparation](docs/EXAM_PREP.md) · [Viva questions](docs/VIVA_QUESTIONS.md) |
| Explore runnable examples | [Examples directory](examples/README.md) |
| Contribute a fix or new example | [Contribution guide](CONTRIBUTING.md) |

## 📚 What is already in this repository?

- Original Python lab programs and assignments.
- Module notes, presentations, PDFs, and question banks.
- AIML practical reports and supporting output files.
- Dataset and visualisation resources.

Use the [resource catalog](docs/LAB_CATALOG.md) to locate the existing material. Original course files are retained; the new guides and examples supplement them rather than claiming to replace official faculty material.

## 🧪 Practical examples

The `examples/` directory contains small, focused demonstrations for:

- **Search:** breadth-first search, depth-first search, A* and AO* concepts.
- **Preprocessing:** missing values, encoding, scaling and train/test splitting.
- **Supervised learning:** KNN, linear regression, decision trees and Naive Bayes.
- **Unsupervised learning:** K-means clustering.
- **Evaluation:** confusion matrices, classification metrics and cross-validation.

Each example is intended to be readable and runnable independently. Check its docstring and the examples guide before running it.

## ⚙️ Quick start

Requires Python 3.10 or newer.

```bash
git clone https://github.com/Atharva-ark06/AIML-SEM-4-GM-university-Lab-programs-IMPQ-s-Modules-.git
cd AIML-SEM-4-GM-university-Lab-programs-IMPQ-s-Modules-
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies and run the tests:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest
```

Run an example:

```bash
python examples/search/bfs.py
python examples/ml/linear_regression.py
```

For existing root-level lab programs, follow the individual program's imports and instructions; some legacy scripts may open plots or require interactive input.

## 🗂️ Repository map

```text
.
├── AIMI ALL/             # Additional module resources and course files
├── docs/                 # Study guides, exam prep, reference sheets
├── examples/
│   ├── search/           # Classical AI search demonstrations
│   └── ml/               # Preprocessing and machine-learning examples
├── datasets/             # Small, clearly documented practice datasets
├── tests/                # Automated checks for maintained examples
├── scripts/              # Repository maintenance helpers
├── README.md
├── requirements.txt
└── pyproject.toml
```

## 🎓 Course information

| Field | Detail |
|---|---|
| University | GM University |
| Course | Artificial Intelligence & Machine Learning |
| Course code | UE24CS2401 |
| Original collection | Semester 4 lab programs, modules, assignments and IMPQs |

Course outlines and assessment requirements can change. Confirm the latest syllabus, deadlines, and exam pattern with your faculty. Practice question lists in this repository are study aids, **not guarantees of exam questions**.

## 🤝 Contributions

Improvements are welcome: fix a bug, clarify a concept, add a tested example, or improve resource indexing. Please avoid uploading private student information, copyrighted materials you are not allowed to redistribute, generated outputs presented as real results, or duplicate files. See [CONTRIBUTING.md](CONTRIBUTING.md).

## ⚠️ Learning note

Use these resources to understand the algorithms and practise explaining them. Verify results, cite sources where appropriate, and follow your university's academic-integrity requirements.

<p align="center"><b>Learn · Implement · Evaluate · Explain</b></p>
