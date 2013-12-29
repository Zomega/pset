LATEX_OBJS = $(wildcard *.tex)

%.pdf: %.tex
	pdflatex $<

init:
	@echo "TODO Need to do setup/config here ..."

init-sample:
	@echo "Populating with sample pset from ./.sample/"
	@cp .sample/* .

all: $(patsubst %.tex,%.pdf,$(LATEX_OBJS)) clean check

clean:
	@echo "\nCleaning up!"
	@rm *.log
	@rm *.aux
	@echo ""

distclean:
	git stash save "Automatic make distclean stash."

check:
	@echo "\nWarnings."
	@grep -c TODO *.pseudo | grep -v :0 | awk -F':' '{print "WARNING: "$$1" has "$$2" things left to do!"}'
	@grep -c TODO *.tex | grep -v :0 | awk -F':' '{print "WARNING: "$$1" has "$$2" things left to do!"}'
	@echo ""
