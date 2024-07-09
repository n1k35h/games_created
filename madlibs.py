MENU_PROMPT = """\n --- Madlibs App ---

Please choose one of the following options:

1) Simple Madlib
2) Haunted House
3) Rush Hour 3
4) Flintstone's Theme
5) Exit

Your selection: """


def menu():
    
    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            print("\nYou have chosen 1 - Simple Madlib\n")
            
            adj = input("Add Adjective: ") # adjective is about feelings e.g: Calm, excited, amazing, awesome, etc
            verb1 = input("Add 1st Verb: ") # verb is taking action e.g: to jump, to walk, to skip, to run, etc
            verb2 = input ("Add 2nd Verb: ")
            famous_name = input("Add a Famous Name: ") # famous name is like an object,

            madlib = f"\nToday I feel so {adj}! It makes me want to {verb1}.\n Stay hydrated and {verb2} like you are {famous_name}!\n"

            print(madlib)
            
        elif user_input == "2":
            print("\nYou have chosen 2 - Haunted House\n")

            your_name = input("Enter your name: ")
            your_friends_name = input("Enter your Friend's name: ")
            a_city_or_town = input("Enter a city or town: ")
            monster = input("Enter a type of a Monster: ")

            madlib = f"""\n
            There was a haunted house in {a_city_or_town}. "It is very scary," said {your_name} and {your_friends_name} replied,
            "Yes, I am very scared!" They both went through the black, creaky gates. As they walked to the house they saw a {monster} lurking in the
            dark. They both screamed very loud saying, "Argghhh! Its a {monster}!" And they both got torn to shreds.\n"""

            print(madlib)

        elif user_input == "3":
            print("\nYou have chosen 3 - Rush Hour 3\n")
            
            number = input("Enter a number: ")
            occupation1 = input("Enter the 1st Occupation: ")
            occupation2 = input("Enter the 2nd Occupation: ")
            place1 = input("Enter the place 1: ")
            male_name = input("Enter a male name: ")
            place2 = input("Enter the place 2: ")
            occupation3 = input("Enter the 3rd Occupation: ")
            body_part1 = input("Enter 1st Body Part: ")
            adjective = input("Enter an Adjective: ") # adjective (describes a person/ place/ thing) such as: exact, part-time, modest, straight, back, forward, etc
            noun = input("Enter a Noun: ") # noun (person/ place/ thing) such as: cloud, storm, carpet, doubt, control, die, etc
            body_part2 = input("Enter 2nd Body Part: ")
            celebrity = input("Enter a Celebrity name: ")
            verb_ending_in_ing = input("Enter a Verb ending in 'ing': ") # verb (is an action) such as: excusing, counting, readying, developing, etc
            adverb = input("Enter an Adverb: ") # adverb (ending in "ly") describe an action such as: slowly, prejudgementally, inconceivably, cowardly etc
            verb_ending_in_s = input("Enter a Verb ending in 's': ") # verb (is an action) such as: excuses, gathers, whimpers, tastes, etc

            madlib = f"""\n
            {number} years after the of Rush Hour 2, James Carter is no longer a {occupation1}, but a {occupation2} on the streets of {place1}.
            Lee is now the bodyguard for his friend {male_name}. Lee is still upset with Carter about an incident in {place2} when Carter accidentally
            shot Lee's girlfriend, {occupation3} Isabella Molina, in the {body_part1}.
            
            During the World Criminal Court discussions, as {male_name} addresses the importance to fight the Triad, he announces that he knows the
            {adjective} of the Triad leadership known as cdthe Shy Shen. Suddenly, {male_name} takes a {noun} in the {body_part2}, disrupting the 
            conference. Lee pursues the assassin and corners him, discovering that the assassin is his brother, {celebrity}. When Lee
            hesitates to shoot {celebrity}, Carter shows up {verb_ending_in_ing} towards the two and {adverb} {verb_ending_in_s} Lee
            over, allowing {celebrity} to escape.\n"""

            print(madlib)
      
        elif user_input == "4":
            print("\nYou have chosen 4 - Flintstone's Theme\n")

            noun1 = input("Enter 1st Noun (Plural): ")
            adjective1 = input("Enter 1st Adjective: ")
            city = input("Enter a City: ")
            noun2 = input("Enter 2nd Noun: ")
            verb = input("Enter a Verb: ")
            noun3 = input("Enter 3rd Noun: ")
            name_of_person_in_room = input("Enter the Name of the Person in the room: ")
            number = input("Enter a Number: ")
            silly_word1 = input("Enter 1st Silly Word: ")
            silly_word2 = input("Enter 2nd Silly Word: ")
            noun4 = input("Enter 4th Noun: ")
            adjective2 = input ("Enter 2nd Adjective: ")

            madlib = f"""\n
            Flint{noun1}, meet the Flint{noun1},
            They're a modern {adjective1} family.
            From the town of {city},
            They're a {noun2} right out of history.\n
            
            Let's {verb}, with the family down the {noun3},
            Through the courtesy of {name_of_person_in_room}'s {number} feet.
            When you're with the Flint{noun1},
            Have a {silly_word1} {silly_word2} doo {noun4} -- A {silly_word2} doo {noun4},
            You'll have a {adjective2} old {noun4}!\n"""

            print(madlib)
      
        else:
            print("Invalid input, please try again!")

menu()