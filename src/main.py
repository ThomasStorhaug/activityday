"""
groups: two units with half of the groups; each group has two classes

32 posts, 16 unique posts per unit

documents:
    one for each post with a table:
        Five columns - times | class 1 | points | class 2 | points

"""

with open("classes.txt", "r") as file:
    full_str = file.read()
    classes = full_str.split(",")

