class LOT:
	""" Labelled Oriented Trees. Stores and constructs presentation complexes associated to LOTs"""
	class edge:
		source = None
		dest = None
		label = None

	edge_list = []

	def complex():
		"""Makes a LOT into a complex"""
		onecell_set = set()		
		twocell_list = []

		for e in edge_list:
			onecell_set.add(e.source)
			onecell_set.add(e.dest)
			onecell_set.add(e.label)

			twocell_list.add(TwoCell([(e.source, True), (e.label,True), (e.dest, True), (e.label, False)]))

		
		w = onecell_set[1][1] #acquiring the zero-cell

		return Complexes(w, list(onecell_set), twocell_list)		
