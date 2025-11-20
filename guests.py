names = ['Sam','Claire','David','Ryan']

print("Hello "+ names[0] +" You are invited to dinner" )
print("Hello "+ names[1] +" You are invited to dinner" )
print("Hello "+ names[2] +" You are invited to dinner" )
print("Hello "+ names[3] +" You are invited to dinner \n" )

"""
Manual Entry Of Names

listOfNames = []
for x in range(4):
    names = input("Enter Names Of Invites: ")
    listOfNames.append(names)
    print(listOfNames)

print("Hello " +listOfNames[0]+ " You have been Invited to dinner")
print("Hello " +listOfNames[1]+ " You have been Invited to dinner")
print("Hello " +listOfNames[2]+ " You have been Invited to dinner")
print("Hello " +listOfNames[3]+ " You have been Invited to dinner")
"""
names[3] = 'Prince'

print("\t New List Of Invites")
names.insert(0, 'Jude')
names.insert(4, 'cassie')
names.insert(6, 'Blaire')

print("Hello "+ names[0] +" You are invited to dinner \n" )
print("Hello "+ names[1] +" You are invited to dinner \n" )
print("Hello "+ names[2] +" You are invited to dinner \n" )
print("Hello "+ names[3] +" You are invited to dinner \n" )
print("Hello "+ names[4] +" You are invited to dinner \n" )
print("Hello "+ names[5] +" You are invited to dinner \n" )
print("Hello "+ names[6] +" You are invited to dinner \n" )