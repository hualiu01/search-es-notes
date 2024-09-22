VENV = .venv
PYTHON = $(VENV)/bin/python3.9
PIP = $(VENV)/bin/pip

# You can add a default target to create the venv
.DEFAULT_GOAL := test

.PHONY: test
test: create-venv-if-none update-libs
	@echo "Running tests in tests folder..."
	$(PYTHON) tests/test_python_client_basics.py
	@echo "Tests finished."

.PHONY: update-libs
update-libs: create-venv-if-none
	. $(VENV)/bin/activate
	# install pip-tools to have `pip-compile` available
	$(PYTHON) -m pip install pip-tools
	# generate requirements.txt from requirements.in
	pip-compile requirements.in -o requirements.txt
	$(PIP) install -r requirements.txt

.PHONY: create-venv-if-none
create-venv-if-none:
	# create a new virtual env if none existed yet
	@if [ ! -d "$(VENV)" ]; then \
		python3 -m venv $(VENV) && \
		echo "Created virtual environment in '$(VENV)'"; \
	else \
		echo "Virtual environment already exists in '$(VENV)'"; \
	fi
	

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf $(VENV)