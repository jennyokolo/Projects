print("The Cursed Antique Shop Part 1")


cursed_antiques = [
    "Talisman",
    "Monkeys Paw",
    "Cursed Mirror",
    "Haunted Painting",
    "Voodoo Doll",
    "Crystal Ball",
    "Cursed Locket",
    "Ancient Amulet",
    "Phantom Clock",
    "Dorian Gray's Portrait",
    "Cursed Ring",
]

cursed_antiques.append("Demon Key")
cursed_antiques.append("Horcrux")


print("After adding cursed antiques (part 1.1)") 
print(cursed_antiques) 




cursed_antiques.sort()
for index in sorted([4,8], reverse=True):
    cursed_antiques.pop(index)



print("After sorting and removing (part 1.2)") 
print(cursed_antiques) 

print("All cursed antiques and their index in point form (part 1.3)") 


for i, item in enumerate(cursed_antiques, start=1):
    print(f"-{i}: {item}")

