import sys

trail = []
assigned_variables = []
unassigned_variables = []


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


def decide(nvars):
	if len(assigned_variables) == nvars:
		return False;
	x = unassigned_variables.pop()	
	assigned_variables.append(x)
	trail.append([x , 0 , False])
	return True


# TODO
def BCP(formula):
	return True
	# for clause in formula:
	# 	for literal in clause:
	# 		if abs(int(literal)) not in unassigned_variables: 
				
	# while (there is a unit clause implying that a variable x must be set to a value v ):
	# 	trail.push([x , v , True])
	# if (there is an unsatisfied clause): return False


def backtrack():
	while True:
		if len(trail) == 0: 
			return False
		backtrackEntry = trail.pop()
		if not backtrackEntry[2]:
			trail.append([backtrackEntry[0] , not backtrackEntry[1] , True])
			return True

def DPLL(nvars, formula):
	trail.clear()

	# if not BCP(formula): # conflict
	# 	print("unsat")
	# 	sys.exit(20)

	while True:
		if not decide(nvars):
			print("sat")
			sys.exit(10)
		# while not BCP(formula): # conflict
		if not backtrack():
			print("unsat")
			sys.exit(20)

def main():
	nvars, nclauses, formula = parse_dimacs(sys.argv[1])
	for clause in formula:
		for literal in clause:
			if abs(int(literal)) not in unassigned_variables: 
				unassigned_variables.append(abs(int(literal)))
	DPLL(nvars, formula)

	print(trail)
	print(assigned_variables)
	print(unassigned_variables)


if __name__ == '__main__':
	main()
