from roman import *

def f_numeral( index ):
	return str( index + 1 )

def f_letter_lower( index ):
	assert index < 26
	return chr( index + 97 )

def f_letter_upper( index ):
	return f_letter_lower( index ).upper()

def f_roman_lower( index ):
	return f_roman_upper( index ).lower()

def f_roman_upper( index ):
	return int_to_roman( index + 1 )

def format_index( index, depth, f_by_depth = [ f_numeral, f_letter_lower, f_roman_lower ] ):
	assert index >= 0
	assert depth >= 0
	assert depth < len( f_by_depth )
	return f_by_depth[ depth ]( index )

def format_subproblem( subproblem ):
		if len( subproblem ) == 0:
			return 'the whole pset'
		return ''.join([ '(' + format_index( subproblem[ depth ], depth ) + ')' for depth in range( len( subproblem ) ) ])
