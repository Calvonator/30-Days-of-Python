# 1) Convert the following to a list comprehension
#
#numbers = [1, 2, 3, 4, 5]
#squares = []
#
#for number in numbers:
#	squares.append(number ** 2)


numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]

print(squares)


#Use a dictionary comprehension to create a new dictionary from the dictionary below
# where each of the values is title case.

movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

titled_movies = {title.title(): movie.title() for title, movie in movie.items()}

print(titled_movies)