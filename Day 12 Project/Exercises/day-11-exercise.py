set1 = set()

set1.update([1, 2, 3])

set2 = {1, 4, 5}

union = set1.union(set2)

symmetric_difference = set1.symmetric_difference(set2)

intersection = set1.intersection(set2)

print(f"Union: {union}\nSymmetric Difference: {symmetric_difference}\nIntersection: {intersection}")

num_range = set()

num_range.update(range(0, 100, 3))

while True:
    guess = input("\nGuess a number between 0 and 100:\n")

    if int(guess) in num_range:
        print("You guessed the number!")
        break
    else:
        print("You guessed wrong!")

