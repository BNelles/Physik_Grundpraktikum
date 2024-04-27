all: build/v408.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
build/abbe.pdf: abbe.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python abbe.py


# hier weitere Abhängigkeiten für build/v408.pdf deklarieren:
build/v408.pdf: build/plot.pdf build/abbe.pdf

build/v408.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v408.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
