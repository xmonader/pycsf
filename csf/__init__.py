import copy


## This is based on some manning books on (classical computer science)

class Constraint:
    def __init__(self, variables):
        self.variables = variables

    def is_satisfied(self, assignment):
        return True



class CSF:
    def __init__(self, variables, domains):
        # variables :list of variables
        # domains dict of variables to list of domains
        # constraints dict vars to constraints list.
        self._varslist = variables
        self._domainsdict = domains
        self._constraintsdict = {}

        for v in self._varslist:
            if v not in self._domainsdict:
                raise ValueError(f"variable {v} doesn't exist in domains {domains}")
            else:
                self._constraintsdict[v] = [] # list of constraints for v

    def add_constraint(self, constraint):
        for v in constraint.variables:
            if v not in self._varslist:
                raise ValueError(f"variable {v} in constraint {constraint} doesn't exist in the CSF variables {self._varslist}")
            else:
                self._constraintsdict[v].append(constraint)

    def consistent(self, variable, assignment):
        for constraint in self._constraintsdict[variable]:
            if not constraint.is_satisfied(assignment):
                return False
        return True

    def backtrack(self, assignment:dict=None):
        assignment = assignment or {}
        # print(len(assignment), len(self._varslist))
        if len(assignment) == len(self._varslist):
            # means we assigned everything
            return assignment
        
        else:
            unassigned_var = list(set(self._varslist) - set(assignment.keys()))[0]
            domains = self._domainsdict[unassigned_var]
            for dom in domains:
                local_assignment = copy.deepcopy(assignment)
                local_assignment[unassigned_var] = dom  
                # print(local_assignment)
                if self.consistent(unassigned_var, local_assignment):
                    solution = self.backtrack(local_assignment)
                    if solution:
                        return solution
