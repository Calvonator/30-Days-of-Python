
# Use sort to alpabetise the following:


students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

students.sort(key=lambda student: student["grade_average"])

print(students)



# Convert the following into lambda and assign to exp
# def exponentiate(base, exponent):
#	return base ** exponent


exp = lambda base, exponent: base ** exponent

print(exp(3, 2))

print(exp)

