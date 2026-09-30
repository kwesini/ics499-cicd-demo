# ICS 499 CI/CD Demo: Grade Calculator

![CI-CD](https://github.com/YOUR-GITHUB-USERNAME/ics499-cicd-demo/actions/workflows/ci-cd.yml/badge.svg)

**Live site (GitHub Pages):** https://YOUR-GITHUB-USERNAME.github.io/ics499-cicd-demo/  
**Live site (Render):** https://YOUR-RENDER-SITE.onrender.com

A tiny project used in ICS 499 (Week 6) to show Git, GitHub, CI, and CD working together.

## What happens when code changes

1. You push a commit (or open a pull request).
2. **CI** (`build-test` job): GitHub Actions installs Python, lints the code with ruff, and runs the tests with pytest.
3. **CD** (`deploy` job): only if CI passes **and** the change is on `main`, the website in `site/` is published to GitHub Pages.
4. If a test fails, the deploy job is **skipped**, so the live site never gets the broken change.

## Project layout

| Path | What it is |
|---|---|
| `site/grading_scale.json` | The grading scale. Shared by the Python code and the website (one source of truth). |
| `src/grades.py` | Python function `letter_grade(percent)` |
| `tests/test_grades.py` | Tests that CI runs on every change |
| `site/index.html` | The web page that CD publishes |
| `.github/workflows/ci-cd.yml` | The CI/CD recipe GitHub Actions follows |
| `requirements.txt` | Tools CI installs: pytest, pytest-cov, ruff |

## Run it on your own computer

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
ruff check .                       # lint
python -m pytest -v                # tests
python -m http.server -d site 8000 # preview the site at http://localhost:8000
```
