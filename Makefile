PY := .venv/Scripts/python

install:
	uv venv --python 3.12 .venv && uv pip install --python $(PY) -e ".[test]"

test:
	$(PY) -m pytest -q

pilot:
	$(PY) -m wired_partners.run --n 3 --out results/pilot

analyze:
	$(PY) -m wired_partners.analyze results/*/trials.jsonl

# rebuild every number, table and figure in the paper from the logs, then the PDF
reproduce:
	$(PY) scripts/analyze_all.py
	$(PY) scripts/make_macros.py
	$(PY) scripts/make_permodel_table.py
	$(PY) scripts/fig_study4.py
	cd paper && pdflatex -interaction=nonstopmode main.tex && bibtex main && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
