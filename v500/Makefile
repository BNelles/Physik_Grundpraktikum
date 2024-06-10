all: build/v500.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
build/Ugrenz.pdf: Ugrenz.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python Ugrenz.py
build/Planck.pdf: Planck.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python Planck.py

# hier weitere Abhängigkeiten für build/v500.pdf deklarieren:
build/v500.pdf: build/plot.pdf build/Ugrenz.pdf build/Planck.pdf

build/v500.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v500.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
