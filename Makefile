init:
	pip install -r requirements.txt

test:
	py.test --cov-report term --cov=flightradar24
