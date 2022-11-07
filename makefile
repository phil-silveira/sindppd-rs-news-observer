setup:
	pip install virtualenv
	python3 -m venv env
	make install_deps

install_deps:
	pip install -r requirements.txt

freeze_deps:
	pip freeze > requirements.txt

run:
	python main.py