.PHONY: all ui1

PYTHON := python
PYUIC := $(PYTHON) -m PyQt5.uic.pyuic

FOLDER := ui
UI1 := mainwindow

all: ui1 run
	$(PYTHON) -u main.py
	
run:
	$(PYTHON) -u main.py

ui1: $(FOLDER)/$(UI1).ui
	cd $(FOLDER) && $(PYUIC) -o "$(UI1).py" "$(UI1).ui"