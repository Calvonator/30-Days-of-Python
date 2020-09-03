
#Exercise 1

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for character, actor, species in main_characters:
    print(f"{character} is a {species} voiced by {actor}")



#Exercise 2

varTuple = ("John Smith", 11743, ("Computer Science", "Mathematics"))

name, id, (major, minor) = varTuple

print(f"{name} ({id}) studies {major} as a major and {minor} for his minor")


#Excercise 3

#Investiate ziping different size value list/tuple

list1 = ['1', '2', '3']
tup = ('1', '2', '3', '4')

var1 = zip(list1, tup)

for each in var1:
    print(each)

list2 = ['1', '2', '3', '4']
tup2 = ('1', '2', '3', '4')

var2 = zip(list2, tup2)

for each in var2:
    print(each)