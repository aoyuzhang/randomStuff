def prescomplex_builder(pres_str):
	"""Builds a presentation complex from a string description

	The generators and the relators must be separated by a pipe,
	generators and relators must be separated by commas,
	and the different letters of a generator must be separated by a space"""

	(generator_str, relator_str) = pres_str.split("|", 2)

	generator_list = generator_str.split(",")
	relator_list = relator_str.split(",")

	z = ZeroCell("")

	onecell_dict = []
	twocell_list = []

	for g in generator_list:
		onecell_dict[g] = OneCell(g, z, z)
	
	for r in relator_list:
		token_list = r.split(" ")
		
		boundary_map = []

		for t in token_list:
			inverse = false
			if '\'' in t:
				inverse = true
			

			if onecell_dict.has_key(t):
				boundary_map += (onecell_dict[t], inverse)
			else:
				raise AttributeError('invalid generator in a relator')

		
		twocell_list += TwoCell(boundary_map)

	return Complexes(z, onecell_dict.values(), twocell_list)
