movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total_budget = 0

for movie in movies:
    total_budget += movie[1]

avg_budget = total_budget / len(movies)

print(avg_budget)

above_avg_movies = []

for movie in movies:
    if movie[1] > avg_budget:
        above_avg_movies.append(movie[0])

print(above_avg_movies)