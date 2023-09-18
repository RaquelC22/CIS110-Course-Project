print(f"Hello there! Today a story about a curious kitten is going to be told!")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")


breed = input("\nWhat breed is the kitten: ")
while len(breed) == 0:
   breed = input(f"Please enter a breed: ")
typeFood = input("What type of food did the kitten eat: ")
while len(typeFood) == 0:
   typeFood = input(f"Please enter a food type: ")
kittenColor = input("What color is the kitten: ")
while len(kittenColor) == 0:
   kittenColor = input(f"Please enter a color: ")
kittenName = input("What is the kitten's name: ")
while len(kittenName) == 0:
   kittenName = input(f"Please enter a name: ")
number = input("How many stray kittens were there: ")
while len(number) == 0:
   number = input(f"Please enter a number: ")
city = input("What city is the kitten exploring: ")
while len(city) == 0:
   city = input(f"Please enter a city: ")
    
print(f"\nLET'S GO!!")
print(f"\nOnce upon a time there was a curious{kittenColor} {breed} named {kittenName}.")
print(f"{kittenName}'s family had just moved to {city} and {kittenName} was curious about it.")
print(f"After waking up from a nap {kittenName} decided to sneek out of the front door ,that was left open, to explore the new city.")
print(f"After leaving his home, {kittenName} was stuck on which side of {city} to start with first!")

eatFoodonSidewalk =input(f"\nShould {kittenName} eat {typeFood} on the sidewalk? Type yes or no: ")
while eatFoodonSidewalk.lower() != "yes" and eatFoodonSidewalk.lower() != "no":
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
    print(f"While following the baby deer, {kittenName} gets distracted by multicolred butterfly that lands on his nose.He tries to catch the butterfly with his tiny paws and falls over.")
    print("Getting up from his fall, he spots a rabbit munching on the leaves that fell from the tall trees.")
else:
    print(f"\n{kittenName} had decided not to take the road that led to the forest.")
    print(f"He'd decided to take trhe route that led to an alley way behind some buildings.")
    print(f"While exploring the alley, {kittenName} had came across {number} stray kittens.")
    print(f"While {kittenName} was scared, he'd slowly approached them to get a better look.")
    print(f"The {number} kittens were also scared and had backed away from {kittenName}.")
    print(f"Deciding that {kittenName} was not a threat, the {number} kittens sniffed him and they all had started to play.")
    
    if eatFoodonSidewalk == "yes" and exploreTheForest == "yes":
        print(f"\nAfter eating the piece of {typeFood} on the sidewalk and feeling sick, {kittenName} had still decided to continue his exploration.")
        print(f"{kittenName} enters the forest and sees the baby deer roaming around. {kittenName} had decided to follow it slowly as he was still feeling sick.")
        print(f"After slowly following the deer, {kittenName} had got distracted by a multicolor butterfly that had landed on his nose.")
        print(f"Instead of trying to catch it with his tiny paws, {kittenName} had decided to trace his steps back home as he was too sick to continue his exploration.")
    elif eatFoodonSidewalk =="no" and exploreTheForest =="no" :
        print(f"After spotting a peice of {typeFood} on the sidewalk, {kittenName} had decided not to eat it knowing it would be bad for him.")
        print(f"Seeing the two diffrent roads, {kittenName} had decided to take the one that leads to the alley way.")
        print(f"Coming upon the alley way, he sees {number} stray kittens huddling together against a building.")
        print(f"Being the curious kitten that he is,{kittenName} had slowly walked up to them to invetigate.All of the stray kittens and {kittenName} decided that neither one weas a threat.")
        print(f"{kittenName} and the {number} stray kittens played with each other until sunset.")
    else:
      print(f"\nAfter eating the food on the sidewalk, {kittenName} had continued to walk his neighborhood instead of taking a different route.")
      print(f"While exploring the neighborhood, {kittenName} met many other pets during exploration.")
      print(f"During the exploration, {kittenName} had began to feel sick from eating the piece of {typeFood} from earlier and had decided to trace his steps back home.")
      print(f"Arriving home on the front porch, {kittenName} owners were in a panic that he was missing.Once they saw {kittenName} on the porch looking ill, they'd brough him inside.")
      print(f"After getting better from the vet visit and constint care of his owners, {kittenName} layed out on his bed infront of the window dreaming of the day that he can have another exploration.")
    print(f"\nThe End")
    
keepPlaying = input(f"\nDo you want to play again? Enter yes or no: ")
while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
    keepPlaying = input(f"Please type yes or no: ")



