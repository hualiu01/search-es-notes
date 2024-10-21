VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PIP_COMPILE = $(VENV)/bin/pip-compile
PYTEST = $(VENV)/bin/pytest

# You can add a default target to create the venv
.DEFAULT_GOAL := install

# create a new virtual env if none existed yet
$(VENV)/bin/activate:
	python3 -m venv $(VENV)

.PHONY: install
install: $(VENV)/bin/activate
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install pip-tools
	$(PIP_COMPILE) requirements.in -o requirements.txt
	$(PIP) install -r requirements.txt

.PHONY: test
test: $(VENV)/bin/activate
	@echo "Running tests in tests folder..."
	$(PYTEST) -s
	@echo "Tests finished."

.PHONY: data
data: $(VENV)/bin/activate
	@echo "query movie metadata from IMDB API and save locally in ../../data/imdb/raw"
	export PYTHONPATH=src:PYTHONPATH && \
	$(PYTHON) ./src/data_import/imdb_movie_lists.py --mode only_add_new IMDB_TOP_250 OSCAR_BEST_PICTURE_NOMINEES 
	@echo "movie metadata preparation finished"

.PHONY: index
index: $(VENV)/bin/activate
	@echo "running data indexing on Elastic Search cluster..."
	export PYTHONPATH=src:PYTHONPATH && \
	$(PYTHON) ./src/index/es_indexer.py
	@echo "successfully indexed ES with data in ../../data/imdb/raw"

.PHONY: format
format: $(VENV)/bin/activate
	$(VENV)/bin/black src tests  
	$(VENV)/bin/flake8 src tests
	$(VENV)/bin/mypy src tests

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf $(VENV)