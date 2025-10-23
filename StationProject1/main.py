import random

print("Choose a story template (1, 2, or 3):")
print("1 - Hospital Visit")
print("2 - Camping Trip")
print("3 - Enchanted Castle")
print("4 - Surprise Me (Random Template)")

template_choice = input("Enter the number of your chosen template: ").strip()


while True:
    if not template_choice:
        template_choice = input("You must enter a number (1–4): ").strip()
    elif not template_choice.isdigit():
        template_choice = input("Invalid input. Please enter a numeric value (1–4): ").strip()
    elif template_choice not in ["1", "2", "3", "4"]:
        template_choice = input("Please choose 1, 2, 3, or 4: ").strip()
    else:
        break


if template_choice == "4":
    template_choice = str(random.choice(["1", "2", "3"]))
    print(f"\nRandomly selected template {template_choice}!\n")
else:
    print(f"\nYou selected template {template_choice}.\n")


if template_choice in ["1", "2", "3"]:
    print("Great! Let's create your story. Please answer the following prompts:")

    number = input("Type a number: ")
    time_measure = input("Type a measure of time (e.g., minutes, hours): ")
    transport = input("Type a mode of transportation: ")
    adj1 = input("Type an adjective: ")
    adj2 = input("Type another adjective: ")
    noun1 = input("Type a noun: ")
    color = input("Type a color: ")
    body_part1 = input("Type a part of the body: ")
    verb1 = input("Type a verb: ")
    number2 = input("Type another number: ")
    noun2 = input("Type another noun: ")
    noun3 = input("Type one more noun: ")
    body_part2 = input("Type another part of the body: ")
    verb2 = input("Type another verb: ")
    noun4 = input("Type another noun: ")
    adj3 = input("Type another adjective: ")
    silly_word = input("Type a silly word: ")

    story = (
        f"""It was about {number} {time_measure} ago when I arrived at the hospital in a {transport}.
The hospital is a/an {adj1} place, there are a lot of {adj2} {noun1} here.
There are nurses here who have {color} {body_part1}.
If someone wants to come into my room, I told them they have to {verb1} first.
I’ve decorated my room with {number2} {noun2}.
Today I talked to a doctor who was wearing a {noun3} on their {body_part2}.
I heard that all doctors {verb2} {noun4} every day for breakfast.
The most {adj3} thing about being in the hospital is the {silly_word} {noun1}!"""
    )

    print("\nHere is your story:\n")
    print(story)
