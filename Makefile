install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint main.py



	
