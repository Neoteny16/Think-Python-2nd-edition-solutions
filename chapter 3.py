# Functions

#repeat_lyrics()
# def print_lyrics():
#     print("I'm a limberjack, and I'm okay.")
#     print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a limberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
# Fucntion defs do not alter flow of execution of the program
repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)
name = "Otar, the half a bee."
print_twice("spam")
print_twice("spam " * 4)
print_twice(name)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = "Toddler eater "
line2 = "Eatler toder."
cat_twice(line1, line2)























