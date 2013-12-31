LATEX_OBJS = $(wildcard *.tex)

# Default target, when run it...
# * Compiles supporting non-LaTeX documents (TODO: Add targets for dot, svg, etc?)
# * Compiles all the .tex documents (not tex.part!)
# * Cleans out temp files
# * Runs checks for unfinished files.
all: $(patsubst %.tex,%.pdf,$(LATEX_OBJS)) clean check

# General target describing how to make PDF files from .tex files.
%.pdf: %.tex
	pdflatex $<

# TODO: .dot -> .svg, .svg -> .pdf ?

# Launches an interactive prompt to create a skeleton pset.
init:
	@python .config/config.py
	@echo "\n\033[1mTemplate pset files have been created! Run \`make\` to create PDFs.\033[0m\n"

# Copies a sample (completed) pset into the main folder for demonstration and testing purposes.
init-sample:
	cp .sample/* .
	@echo "\n\033[1mThe repo has been populated with sample content from ./.sample/\033[0m\n"

# Removes temporary files as defined by the .gitignore.
clean:
	git clean -fdX
	@echo "\n\033[1mFiles matching the .gitignore have been removed.\033[0m\n"

# TODO: This one needs some work to work properly. Possibly -fdx?
# Packages the repo for distribution, deleting files that should not be committed.
# If you are going to add a new file (as opposed to editing existing files), you will
# need to commit that file separately before running `make distclean`. An initial commit
# followed by testing followed by a final commit/rebase is an excellent idea. 
distclean:
	git stash save "Automatic make distclean stash."
	@echo "\n\033[1mYour changes have been stashed using git.\033[0m\n"

# TODO: This is an outdated mess.
check:
	@echo "\nWarnings."
	@grep -c TODO *.pseudo | grep -v :0 | awk -F':' '{print "WARNING: "$$1" has "$$2" things left to do!"}'
	@grep -c TODO *.tex | grep -v :0 | awk -F':' '{print "WARNING: "$$1" has "$$2" things left to do!"}'
	@echo ""
