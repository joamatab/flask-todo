
install:
	pip install pre-commit
	pre-commit install


run:
	export FLASK_APP=run.py
