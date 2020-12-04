#Task 1
def primes(upper_limit):

    for num in range(2, int(upper_limit)):
        for integer in range(2, num):
            if num % integer == 0:
                break
        else:
            yield num


x = primes(11)

print(next(x))
print(next(x))
print(next(x))


#Task 2

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]

title_names = (name.strip().title() for name in names)

print(next(title_names))
print(next(title_names))
print(next(title_names))
print(next(title_names))
print(next(title_names))


#Task 3
import random as rand

class deck:

    def __init__(self):
        self.cards = []

    def shuffle(self):
        #use a mapping (tupple of indexes) with randomly generated numbers to swap as follows shuffled[tuple[1]] = cards[tuple[2]] 
        shuffled_indexes = []
        shuffle_buffer = []
        
        for _ in range(len(self.cards)):
            index = rand.randint(0, len(self.cards) - 1)
            shuffled_indexes.append(index)
            shuffle_buffer.append(self.cards[index])

        self.cards = shuffle_buffer

    def print_cards(self):
        ctr = 0
        for card in self.cards:
            print(f"({card.number}, {card.colour})")
            ctr += 1

        print(ctr)

    def generate_deck(self):

        colours = ["Hearts", "Clubs", "Spades", "Diamonds"]

        for colour in colours:
            for number in range(1, 14):
                self.cards.append(card(number, colour)) 


class card:

    def __init__(self, number, colour):
        self.number = number
        self.colour = colour

    




deck = deck()

deck.generate_deck()

deck.shuffle()






