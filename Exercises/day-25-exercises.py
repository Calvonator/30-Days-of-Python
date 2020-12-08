def greet():

    name = input("Hello, what is your name?").strip()

    name = "".join(name.split())

    if name is None:
        print("Greetings World!")
    else:
        print(f"Greetings {name}!")


greet()

