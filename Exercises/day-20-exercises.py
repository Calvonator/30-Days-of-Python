import operator

# 1) Use map to call the strip method on each string in the following list:

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]

#humpty = map(lambda sentence: sentence.strip(), humpty_dumpty)

humpty = map(operator.methodcaller("strip"), humpty_dumpty)

print(*humpty)

#for sentence in humpty:
#    print(sentence)


# 2) Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new list. 
# Make sure that every name in the new list is in title case.

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

small_names = [name for name in names if len(name) < 8]

print(*small_names)

#for name in small_names:
#    print(name)


# 3) Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to the console.

def is_pos(num):

    if num < 0:
        return False

    else:
        return True


nums = [x for x in range(-5, 11)]

pos_nums = filter(is_pos, nums)

print(*pos_nums)

#for nums in pos_nums:
    #print(nums)