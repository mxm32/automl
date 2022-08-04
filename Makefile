install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


format: 
	black *.py --line-length 79

lint:
	pylint --disable=R,C,broad-except,bare-except,consider-using-f-string main.py	

test:
	python -m pytest -vv test_main.py
	#python -m pytest --nbval notebook.ipynb

all: install format lint test 

