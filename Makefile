LATEX_OBJS = $(wildcard *.tex)

%.pdf: %.tex
	pdflatex $<

all: precheck $(patsubst %.tex,%.pdf,$(LATEX_OBJS)) clean check

precheck:
	@echo "Doing Precheck?"

clean:
	@echo "\nCleaning up!"
	@rm *.log
	@rm *.aux
	@echo ""

check:
	@echo "\nWarnings."
	@grep -c TODO *.pseudo | grep -v :0 | awk -F':' '{print "WARNING: "$$1" has "$$2" things left to do!"}'
	@grep -c TODO *.tex | grep -v :0 | awk -F':' '{print "WARNING: "$$1" has "$$2" things left to do!"}'
	@echo ""
