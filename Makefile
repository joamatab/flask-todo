install:
	pip install pre-commit
	pre-commit install

run:
	export FLASK_ENV=development
	export FLASK_APP=run.py
	python run.py

docker-build:
	 docker build -t flask-todo:latest .

docker-run:
	 docker run -d -p 5000:5000 flask-todo
