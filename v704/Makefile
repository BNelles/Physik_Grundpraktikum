all: build/v704.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
build/aluminium.pdf: aluminium.py ../matplotlibrc ../header-matplotlib.tex | build
				TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python aluminium.py

build/eisen.pdf: eisen.py ../matplotlibrc ../header-matplotlib.tex | build
				TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python eisen.py

build/beta.pdf: beta.py ../matplotlibrc ../header-matplotlib.tex | build
				TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python beta.py
# hier weitere Abhängigkeiten für build/v704.pdf deklarieren:
build/v704.pdf: build/plot.pdf  build/eisen.pdf  build/aluminium.pdf  build/beta.pdf

build/v704.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v704.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
