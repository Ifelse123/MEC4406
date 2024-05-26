#Quiz 1 part 2
#Created by James Morgan 0061108510

#Write code that prints your name and counts up to your favourite number squared
my_name = "James Morgan"
print(my_name)

fav_num = 9

for x in range(fav_num):
    hold = (x + 1)**2
    print(hold)

#Update the code to contain a class Engineers, with a fixed class attribute skill
#equal to "problem solver", and initial attributes name, type and years of experience. 
#Create two different engineers (objects) and print out their attributes.

class Engineers:
    
    skill = "problem solver"

    def __init__(person, name, type, exp):
        person.name = name
        person.type = type
        person.exp = exp

    def __str__(person):
        return f"{person.name} is a {person.type} engineer with {person.exp} years experience."

p1 = Engineers("Kate Goggins","Control Systems",12)
p2 = Engineers("Andrew Column","Civil",25)
print("\n")
print(p1)
print(p2)

#Also change your name to be the reverse. I.e. Jim becomes Mij
back_name = my_name[::-1]
print("\n")
print(back_name.title())