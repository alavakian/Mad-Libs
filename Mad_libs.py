import random

# Saludar
print("Hello and welcome to our Mad Libs game!")


# Función para obtener entradas del usuario
def get_user_inputs():
    return {
        "person_name": input("Person name: "),
        "noun": input("Noun: "),
        "adjective": input("Provide an adjective (feeling): "),
        "verb": input("Provide a verb: "),
        "adjective2": input("Provide another adjective: "),
        "animal": input("Provide an animal: "),
        "verb2": input("Provide another verb: "),
        "color": input("Provide a color: "),
        "verb3": input("Provide another verb: "),
        "adverb": input("Provide an adverb: "),
        "number": input("Provide a number: "),
        "silly_word": input("Provide a silly word: "),
        "noun2": input("Provide another noun: "),
        "measure_of_time": input("Provide a measure of time: "),
        "transportation": input("Provide a mode of transportation: "),
        "part_of_body": input("Provide a part of the body: "),
        "number2": input("Provide one more number please: "),
        "noun3": input("Provide one more noun please: "),
        "part_of_body2": input("Provide another part of the body: "),
        "noun4": input("Provide one more noun please: "),
        "adjective3": input("Provide one more adjective please: "),
    }


# Historias con saltos de línea
templates = [
    ("It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transportation}.\n"
     "The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here.\n"
     "There are nurses here who have {color} {part_of_body}.\n"
     "If someone wants to come into my room I told them that they have to {verb} first.\n"
     "I’ve decorated my room with {number2} {noun2}.\n"
     "Today I talked to a doctor and they were wearing a {noun3} on their {part_of_body2}.\n"
     "I heard that all doctors {verb2} {noun4} every day for breakfast.\n"
     "The most {adjective3} thing about being in the hospital is the {silly_word} {noun}!\n"),

    ("This weekend I am going camping with {person_name}.\n"
     "I packed my lantern, sleeping bag, and {noun}.\n"
     "I am so {adjective} to {verb} in a tent.\n"
     "I am {adjective2} we might see a {animal}, I hear they’re kind of dangerous.\n"
     "While we’re camping, we are going to hike, fish, and {verb2}.\n"
     "I have heard that the {color} lake is great for {verb3}.\n"
     "Then we will {adverb} hike through the forest for {number} {measure_of_time}.\n"
     "If I see a {color} {animal} while hiking, I am going to bring it home as a pet!\n"
     "At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!\n"),

    ("Dear {person_name},\n"
     "I am writing to you from a {adjective} castle in an enchanted forest.\n"
     "I found myself here one day after going for a ride on a {color} {animal} in a magical place.\n"
     "There are {adjective2} fairies and {adjective3} dragons here!\n"
     "In the grand hall there is a pool full of {noun}.\n"
     "I fall asleep each night on a {noun2} of golden feathers and dream of {adjective} adventures.\n"
     "It feels as though I have lived here for {number} {measure_of_time}.\n"
     "I hope one day you can visit, although the only way to get here now is {verb3} on a {adjective2} unicorn!\n")
]


# Elegir y mostrar historia
def generate_story():
    user_inputs = get_user_inputs()
    selected_template = random.choice(templates)  # Elegir historia aleatoriamente
    story = selected_template.format(**user_inputs)
    print("\nHere is your Mad Libs story:\n")
    print(story)


# Ejecutar el programa
generate_story()
