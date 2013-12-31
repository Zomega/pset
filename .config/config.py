# LOTS TO DO HERE.
# First, finish this up. Comment on the way.
# Second, split it up. formatting to it's own file?
from formats import *
from tree import *

def prompt( prompt_string ):
	return input(prompt_string + ' ')

def prompt_int( prompt_string ):
	return int( prompt( prompt_string ) )

def prompt_subproblem( subproblem ):
	print 'Entering ' + format_subproblem( subproblem )
	tree = []
	num_subproblems = prompt_int( 'How many subproblems for ' + format_subproblem( subproblem ) + '?' )
	for index in range( num_subproblems ):
		tree.append( prompt_subproblem( subproblem + [ index ] ) )
	return tree

def prompt_pset():
	return prompt_subproblem([])

def subproblem_filename( subproblem ):
	return 'problem' + ''.join([ '.' + format_index( subproblem[ depth ], depth ) for depth in range( len( subproblem ) ) ]) + '.tex.part'

def immediate_subproblem_files( subproblem, tree ):
	for child in children( subproblem, tree ):
		yield subproblem_filename( child )

from template import texenv

#prompt basic stuff like titles, etc.
#prompt_subformats()
tree = prompt_pset()

# Create final files.
texpart_template = texenv.get_template('subproblems.tex')
pdf_base_template = texenv.get_template('pdf_base.tex')

# Create all the .tex.part files, one for each subproblem.
for subproblem in nodes( tree ):
	if subproblem == []:
		continue
	with open( subproblem_filename( subproblem ), "wb") as f:
		f.write( texpart_template.render( immediate_subproblem_files = list( immediate_subproblem_files( subproblem, tree ) ) ) )

# Create a document containing all the problems...
with open( 'pset.tex', "wb" ) as f:
	f.write( pdf_base_template.render(
		title = "TITLE",
		content = texpart_template.render( immediate_subproblem_files = list( immediate_subproblem_files( [], tree )))
	))
