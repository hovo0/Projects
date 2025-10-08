import random

print("Choose a story template (1, 2, or 3):")
print("1 - Hospital Visit")
print("2 - Camping Trip")
print("3 - Enchanted Castle")
print("4 - Surprise Me (Random Template)")

template_choice = input("Enter the number of your chosen template: ")

if template_choice == "4":
    template_choice = str(random.choice(["1", "2", "3"]))
    print(f"\nRandomly selected template {template_choice}!\n")
else:
    print(f"\nYou selected template {template_choice}.\n")

# Even though the user can choose between 1, 2, or 3 (or get a random one with 4),
# this program always uses Template 1 (Hospital Visit) regardless of the selection.
if template_choice == "1" or "2" or "3":
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
        f"""It was about {number} {time_measure} ago when I arrived at the hospital in a {transport}.The hospital is a/an {adj1} place, there are a lot of {adj2} {noun1} here.
        There are nurses here who have {color} {body_part1}.If someone wants to come into my room I told them that they have to {verb1} first.I’ve decorated my room with
        {number2} {noun2}.Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. I heard that all doctors {verb2} {noun4} every day for breakfast.
        The most {adj3} thing about being in the hospital is the {silly_word} {noun1}!"""
    )

    print("\nHere is your story:\n")
    print(story)
