install:
	pip install pre-commit
	pre-commit install

debug:
	export FLASK_ENV=development
	export FLASK_APP=run.py
	python run.py

build:
	 docker build -t flask-todo:latest .

run:
	 docker run -p 5000:5000 flask-todo

tag:
	docker-tag flask-todo:latest joamatab/flask-todo:latest

push:
	docker push joamatab/flask-todo
