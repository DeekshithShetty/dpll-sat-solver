import sys

# dictionary of variables
trail = {}
trail_assignment = []

class Variable:
	def __init__(self, value, is_decision):
		self.value, self.is_decision = value, is_decision


def find_and_update_unit_clauses(formula):
	is_unit_clause_updated = 0
	for clause in formula:
		literal_counter = 0
		conjunction_result = False
		possible_unit_literal = 0

		for literal in clause:
			variable = abs(literal)
			if variable in trail: 
				literal_counter += 1
				conjunction_result = conjunction_result or (trail[variable].value if literal > 0 else not trail[variable].value)
			else:
				possible_unit_literal = literal

		if literal_counter == len(clause) - 1 and conjunction_result == False: # found a unit clause:
				trail[abs(possible_unit_literal)] = Variable(True if possible_unit_literal > 0 else False, True)
				trail_assignment.append(abs(possible_unit_literal))
				is_unit_clause_updated = 1
		elif literal_counter == len(clause) and not conjunction_result:
			return -1	# unsatisfied clause
	
	return is_unit_clause_updated


def BCP(formula):
	is_unit_clause_found = 1
	# there is a unit clause implying that a variable x must be set to a value v
	while (is_unit_clause_found == 1):
		is_unit_clause_found = find_and_update_unit_clauses(formula)

	if is_unit_clause_found == -1: return False # there is an unsatisfied clause
	
	return True	
	

def decide(nvars):
	# check if all variables are assigned
	if len(trail) == nvars: return False;
	# choose an unassigned variable and set a value
	unassigned_variable = [item for item in variable_list if item not in trail.keys()][0]
	trail[unassigned_variable] = Variable(False, False)
	trail_assignment.append(unassigned_variable)
	return True


def backtrack():
	while True:
		if len(trail) == 0: 
			return False
			
		x = trail_assignment.pop()	
		backtrack_variable = trail.pop(x)		
		if not backtrack_variable.is_decision:
			trail[x] = Variable(not backtrack_variable.value, True)
			trail_assignment.append(x)
			return True


def DPLL(nvars, formula):
	trail.clear()

	if not BCP(formula): # conflict
		print("unsat")
		sys.exit(20)

	while True:
		if not decide(nvars):
			print("sat")
			sys.exit(10)
		while not BCP(formula): # conflict
			if not backtrack():
				print("unsat")
				sys.exit(20)


def parse_dimacs(filename):
	formula = []
	with open(sys.argv[1], 'r') as input_file:
		for line in input_file:
			if line.startswith('c'): continue
			if line.startswith('p'):
				nvars, nclauses = line.split()[2:4]
				continue
			literals = list(map(int, line.split()))
			assert literals[-1] == 0
			literals = literals[:-1]
			formula.append(literals)
	return int(nvars), int(nclauses), formula


def main():
	global variable_list
	nvars, nclauses, formula = parse_dimacs(sys.argv[1])
	variable_list = list(range(1, nvars + 1))

	DPLL(nvars, formula)


if __name__ == '__main__':
	main()
