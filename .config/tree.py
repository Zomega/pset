# Represents an ordered (valueless) tree.

def nodes( tree ):
	yield []
	for index in range( len( tree ) ):
		# Recurse on sub topologies.
		for subpart in nodes( tree[ index ] ):
			yield [index] + subpart

def subtree( node, tree ):
	if len( node ) == 0:
		return tree
	assert node[0] < len( tree )
	return subtree( node[1:], tree[ node[0] ] )

def children( node, tree ):
	for index in range( len( subtree( node, tree ) ) ):
		yield node + [ index ]

def parent( node ):
	return node[:-1]
