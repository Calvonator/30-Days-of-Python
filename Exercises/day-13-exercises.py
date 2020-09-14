


def exponentiate(base, power):
    return base ** power



def process_string(string):
    #strList = [char for char in string]
    string = string.split()
    string = ' '.join(string)
    
    return string.lower()

print(exponentiate(2, 3))
print(process_string("bosb Your Uncle"))