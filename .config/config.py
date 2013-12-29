# LOTS TO DO HERE.
# First, finish this up. Comment on the way.
# Second, split it up. formatting to it's own file?

def prompt( prompt_string ):
	return input(prompt_string + ' ')

def prompt_int( prompt_string ):
	return int( prompt( prompt_string ) )

### FORMATS ###

def f_numeral( index ):
	return str( index + 1 )

def f_letter_lower( index ):
	assert index < 26
	return chr( index + 97 )

def f_roman_lower( index ):
	return int_to_roman( index + 1 ).lower()

from roman import *

f_by_depth = [ f_numeral, f_letter_lower, f_roman_lower ] # Default to 1ai

def format_index( index, depth ):
	assert index >= 0
	assert depth >= 0
	assert depth < len( f_by_depth )
	return f_by_depth[ depth ]( index )

def format_subpart( subpart ):
		if len( subpart ) == 0:
			return 'the whole pset'
		return ''.join([ '(' + format_index( subpart[ depth ], depth ) + ')' for depth in range( len( subpart ) ) ])

def prompt_subpart( subpart ):
	print 'Entering ' + format_subpart( subpart )
	topology = []
	num_subparts = prompt_int( 'How many subparts for ' + format_subpart( subpart ) + '?' )
	for index in range( num_subparts ):
		topology.append( prompt_subpart( subpart + [ index ] ) )
	return topology

def prompt_pset():
	return prompt_subpart([])

def iterate_over_topology( topology ):
	yield []
	for index in range( len( topology ) ):
		# Recurse on sub topologies.
		for subpart in iterate_over_topology( topology[ index ] ):
			yield [index] + subpart

def subpart_filename( subpart ):
	return 'problem' + ''.join([ '.' + format_index( subpart[ depth ], depth ) for depth in range( len( subpart ) ) ]) + '.tex.part'

#prompt_subformats()
topology = prompt_pset()
for subpart in iterate_over_topology( topology ):
	if subpart == []:
		continue
	print format_subpart( subpart ), subpart_filename( subpart )
