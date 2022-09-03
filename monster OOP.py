class Monster:
    def __init__(self,name,origin,description,attack,magicalforce,magicaldefence,defence,intelligence,health,experience):
        self.name = name
        self.origin = origin
        self.description = description
        self.attack = attack
        self.magicalforce = magicalforce
        self.magicaldefence = magicaldefence
        self.defence = defence
        self.intelligence = intelligence
        self.health = health
        self.experience = experience
listofIDS=[]

with open("monstershard.txt",'r') as file:
    for line in file:

        line = line.strip('\n')
        parts = line.rsplit(",")
        listofIDS.append(Monster(parts[1],parts[2],parts[3],parts[4],parts[5],parts[6],parts[7],parts[8],parts[9],parts[10]))

ID = int(input("What is the ID of the monster you want to find?"))
Attribute = input("What stat do you want to know about it?")

Stat = getattr(listofIDS[ID-1],Attribute)

print(Stat)
