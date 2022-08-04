install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


format: 
	black *.py --line-length 79

lint:
	pylint --disable=R,C, main.py	


all: install format lint  

