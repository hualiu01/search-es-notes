VENV = .venv
PYTHON = $(VENV)/bin/python3.9
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
	$(PYTHON) -m pip install pip-tools
	$(PIP_COMPILE) requirements.in -o requirements.txt
	$(PIP) install -r requirements.txt

.PHONY: test
test: $(VENV)/bin/activate
	@echo "Running tests in tests folder..."
	pytest -s
	@echo "Tests finished."

.PHONY: format
format: $(VENV)/bin/activate
	$(VENV)/bin/black src tests  
	$(VENV)/bin/flake8 src tests
	$(VENV)/bin/mypy src tests

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf $(VENV)