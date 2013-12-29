LATEX_OBJS = $(wildcard *.tex)

%.pdf: %.tex
	pdflatex $<

# TODO: .dot?

init:
	@python .config/config.py
	@echo "\n\033[1mTemplate pset files have been created! Run \`make\` to create PDFs.\033[0m\n"

init-sample:
	cp .sample/* .
	@echo "\n\033[1mThe repo has been populated with sample content from .sample/\033[0m\n"

all: $(patsubst %.tex,%.pdf,$(LATEX_OBJS)) clean check

clean:
	git clean -fdX
	@echo "\n\033[1mFiles matching the .gitignore have been removed.\033[0m\n"

distclean:
	git stash save "Automatic make distclean stash."
	@echo "\n\033[1mYour changes have been stashed using git.\033[0m\n"

check:
	@echo "\nWarnings."
	@grep -c TODO *.pseudo | grep -v :0 | awk -F':' '{print "WARNING: "$$1" has "$$2" things left to do!"}'
	@grep -c TODO *.tex | grep -v :0 | awk -F':' '{print "WARNING: "$$1" has "$$2" things left to do!"}'
	@echo ""
