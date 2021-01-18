import csf


def mapcolor():
    class MapColorConstraint(csf.Constraint):
        def __init__(self, r1, r2):
            super().__init__(variables=[r1, r2])
            self.r1 = r1
            self.r2 = r2

        def is_satisfied(self, assignment):
            if self.r1 not in assignment:
                return True
            if self.r2 not in assignment:
                return True
            return assignment[self.r1] != assignment[self.r2]
        

    variables = ["Western Australia", "Northern Territory", "South Australia", "Queensland", "New South Wales", 
    "Victoria", "Tasmania"]
    domain_vals = ["red", "blue", "green", "grey"]

    domains = {}
    for var in variables:
        domains[var] = domain_vals

    csp = csf.CSF(variables, domains)
    neighbors_pairs = [
            ["Western Australia", "Northern Territory"],
            ["Western Australia", "South Australia"],
            ["South Australia", "Northern Territory"],
            ["Queensland", "Northern Territory"],
            ["Queensland", "South Australia"],
            ["Queensland", "New South Wales"],
            ["New South Wales", "South Australia"],
            ["Victoria", "South Australia"],
            ["Victoria", "New South Wales"],
            ["Victoria", "Tasmania"], 
    ]
    for pair in neighbors_pairs:
        constraint = MapColorConstraint(pair[0], pair[1])
        csp.add_constraint(constraint)


    return csp.backtrack()

def eightqueen(size=4):
    import itertools
    BOARD_SIZE = size
    class EightQueenConstraint(csf.Constraint):
        def __init__(self, qname):
            super().__init__([qname])
            self.qname = qname

        def is_satisfied(self, assignment):
            if self.qname not in assignment:
                return True
            q1r, q1c = assignment[self.qname]
            for other_queen_name, other_queen_pos in assignment.items():
                if other_queen_name == self.qname:
                    continue
                else:
                    q2r, q2c = other_queen_pos
                    if q1r == q2r or q1c == q2c or abs(q1r-q2r) == abs(q1c-q2c): # same row, same column, same diagonal
                        return False
            return True

    variables = [f"q{i}" for i in range(BOARD_SIZE)]
    domain_vals = list(itertools.product(range(BOARD_SIZE), range(BOARD_SIZE)))

    domains = {}
    for v in variables:
        domains[v] = domain_vals

    csp = csf.CSF(variables, domains)
    # for q1, q2 in list(itertools.zip_longest(variables[:-1], variables[1:])):
    for qname in variables:
        csp.add_constraint(EightQueenConstraint(qname))
    return csp.backtrack()



eight_queen_8 = lambda: eightqueen(8)
for prob in [mapcolor, eightqueen, eight_queen_8]:
    print("sol: ", prob())