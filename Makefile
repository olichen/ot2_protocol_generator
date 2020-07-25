build:
	pyinstaller --onefile -w --name ot2_protocol_generator cli.py

test:
	python -m unittest discover -s tests

lint:
	flake8

run:
	python cli.py
