all: build/v511.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

build/quer.pdf: quer.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python quer.py

# hier weitere Abhängigkeiten für build/v511.pdf deklarieren:
build/v511.pdf: build/plot.pdf build/quer.pdf

build/v511.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v511.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
