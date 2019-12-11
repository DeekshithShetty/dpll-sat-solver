import sys

def parse_dimacs(filename):
	clauses = []
	with open(sys.argv[1], 'r') as input_file:
		for line in input_file:
			if line[0] in ['c', 'p']:
				continue
			literals = list(map(int, line.split()))
			assert literals[-1] == 0
			literals = literals[:-1]
			clauses.append(literals)
	return clauses

clauses = parse_dimacs(sys.argv[1])
print(clauses)
