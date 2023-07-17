.PHONY: all
all: chaizi-jt.txt chaizi.schema.yaml chaizi.dict.yaml

chaizi-jt.txt:
	curl https://raw.githubusercontent.com/kfcd/chaizi/master/chaizi-jt.txt >> chaizi-jt.txt

chaizi.schema.yaml:
	mkdir -p build && cp src/chaizi.schema.yaml build/chaizi.schema.yaml

chaizi.dict.yaml: chaizi-jt.txt chaizi.schema.yaml build.py
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
	python build.py

clean:
	rm -f chaizi-jt.txt build/*
