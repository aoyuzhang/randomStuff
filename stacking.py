class Stacking:
    def __init__(self, complex, vertex_list):
        self.complex = complex
        self.vertexList = vertex_list

    def __repr__(self):
        s = "Complex : " + complex.__repr__() + "\n"

        for v in self.vertex_list:
            s += v.__repr__() + "\n"

        return s
