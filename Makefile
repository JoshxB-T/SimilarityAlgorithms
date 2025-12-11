PY=python3

all: run

run: main.py
	$(PY) $<

clean:
	rm -f *.pyc