PIP := pip install
PROJECT_NAME := aws-chalice
PYTHON_VERSION := 3.12.4
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

# Setup dependencies
.pip:
	pip install --upgrade pip

# Create virtualenv
.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

setup-dev: .pip
	$(PIP) requirements/requirements-dev.txt

code-convention:
	flake8
	pycodestyle

deploy:
	chalice deploy

delete:
	chalice delete
