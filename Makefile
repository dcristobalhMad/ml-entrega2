include Makefile.local

deps:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

dev: deps
	@echo "Starting development server..."
	@jupyter notebook entrega.ipynb