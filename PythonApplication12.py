import random

def game_who_or_what():
    objects = ["stone", "cat", "dragon", "book", "sun"]
    secret_object = random.choice(objects)
    attempts = 3

    print("\nGame 1: I've guessed something. Try to guess!")

    while attempts > 0:
        try:
            guess = input("Your guess: ").lower()
            if guess == secret_object:
                print("Correct!")
                return
            else:
                attempts -= 1
                if attempts > 0:
                    print("Incorrect. Try again.")
                else:
                    print(f"You didn't guess. It was {secret_object}.")
        except:
            print("Incorrect input. Try again.")

def game_famous_person():
    people = {
        "Albert Einstein": ["Physicist", "Theory of relativity", "Nobel Prize", "Hair"],
        "Leonardo da Vinci": ["Artist", "Mona Lisa", "Inventor", "Renaissance"],
        "Marie Curie": ["Scientist", "Radioactivity", "Two Nobel Prizes", "Polish"],
    }
    secret_person = random.choice(list(people.keys()))
    hints = people[secret_person]
    attempts = 4
    used_hints = []

    print("\nGame 2: I've guessed a famous person. Try to guess!")

    while attempts > 0:
        try:
            guess = input("Your guess: ").lower()
            if guess == secret_person.lower():
                if random.choice([True, False]):
                    print("Incredible! You guessed it!")
                else:
                    print("It seems you guessed it by chance...")
                return
            else:
                attempts -= 1
                if attempts > 0:
                    print("Incorrect. Try again.")
                    if len(used_hints) < len(hints):
                        hint = random.choice(hints)
                        while hint in used_hints:
                            hint = random.choice(hints)
                        used_hints.append(hint)
                        print(f"Hint: {hint}")
                else:
                    print(f"You didn't guess. It was {secret_person}.")
        except:
            print("Incorrect input. Try again.")

def game_i_think_it_is_maybe_not():
    all_objects = ["apple", "mystery", "paradox", "fantasy", "silence"]
    objects = random.sample(all_objects, random.randint(2, 4))
    secret_object = random.choice(objects)
    attempts = 0

    print("\nGame 3: I've guessed something... I don't know what. Try to guess!")

    while True:
        try:
            guess = input("Your guess: ").lower()
            attempts += 1
            if guess == secret_object:
                if attempts % 2 == 0:
                    print("Congratulations! You guessed it!")
                else:
                    print("It's a coincidence, but you guessed it.")
                return
            else:
                if random.choice([True, False]):
                    hint = random.choice(all_objects)
                    print(f"Hint: {hint}")
                else:
                    hint = random.choice(list(set(all_objects) - set(objects)))
                    print(f"Hint: {hint}")
            if attempts > 10 and random.random() < 0.3:
                print("Maybe it's too difficult. Game over.")
                if guess == secret_object:
                    print("But you still guessed it!")
                else:
                    print(f"It was {secret_object}.")
                return
        except:
            print("What was that? Try again.")

def main():
    while True:
        print("\nChoose a game:")
        print("1. Who or what")
        print("2. Is it a famous person?")
        print("3. I think it is... maybe not")
        print("4. Exit")

        try:
            choice = int(input("Your choice: "))
            if choice == 1:
                game_who_or_what()
            elif choice == 2:
                game_famous_person()
            elif choice == 3:
                game_i_think_it_is_maybe_not()
            elif choice == 4:
                break
            else:
                print("Incorrect choice. Try again.")
        except ValueError:
            print("Incorrect input. Try again.")

if __name__ == "__main__":
    main()