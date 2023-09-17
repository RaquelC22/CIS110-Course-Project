print(f"Hello there! Today a story about a curious kitten is going to be told!")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")

breed = input("\nWhat breed is the kitten?")
typeFood = input("What type of food did the kitten eat?")
kittenColor = input("What color is the kitten?")
kittenName = input("What is the kitten's name?")
number = input("How many stray kittens were there?")
city = input("What city is the kitten exploring?")

print(f"\nLET'S GO!!")
print(f"\nOnce upon a time there was a curious{kittenColor} {breed} named {kittenName}.")
print(f"{kittenName}'s family had just moved to {city} and {kittenName} was curious about it.")
print(f"After waking up from a nap {kittenName} decided to sneek out of the front door ,that was left open, to explore the new city.")
print(f"After leaving his home, {kittenName} was stuck on which side of {city} to start with first!")

eatFoodonSidewalk =input(f"\nShould {kittenName} eat {typeFood} on the sidewalk? Type yes or no: ")
if eatFoodonSidewalk == "yes":
    print(f"\nWhile walking to explore {city}, {kittenName} had ate a piece of {typeFood} on the sidewalk.")
    print(f"Continuing on his way to exploring, his belly had started to rumble and his mouth was beginning to get dry.")
    print(f"Realizing that he shouldn't have ate the {typeFood} from the sidewalk, he'd started to make his way back home ending his exploraiton early.")
    print(f"Upon returning home, his owners were extremely concern due to {kittenName} sneaking out and appearing as if he was sick.")
    print(f"The owners had taken {kittenName} to the vet to get a check up, and {kittenName} had decided that next time he sneaks out to explore he will not eat food on the side walk.")
else:
    print(f"\n{kittenName} had decided not to eat the piece of {typeFood} on the sidewalk.")
    print(f"Knowing that eating outside food isn't good for him, he continues on his way.")
    print(f"Getting father from his home, his scenery has began to change from houses to buildings and forestry.")
    print(f"{kittenName} has now come across another desicion to make in order to continue his exploration.")
exploreTheForest =input(f"\nShould {kittenName} take the road that leads to the forest? Type yes or no: ")
while exploreTheForest.lower() != "yes" and exploreTheForest.lower() != "no" :
    exploreTheForest =input(f"Please type yes or no:")
                            
if exploreTheForest == "yes":
    print(f"\n{kittenName} had decided to take the road that leads to the forest.")
    print(f"When he comes to the foreest entry he spots any things and begins to enter the forest.")
    print(f"{kittenName} sees a baby deer roaming around and had decided to follow it, as he was curious as to what it does.")
    print(f"While following the baby deer, {kittenName} gets distracted by butterfly that lands on his nose.He tries to catch the butterfly with his tiny paws and falls over.")
    print("Getting up from his fall, he spots a rabbit munching on the leaves taht fell from the tall trees.")
    
    




