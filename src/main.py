"""
groups: two units with half of the groups; each group has two classes

post names: 1-15

30 posts, 15 unique posts per unit

documents:
    one for each post with a table:
        Four columns - class 1 | points | class 2 | points

values needed for table: postname, rotation
        
"""
from random import choice
from docx import Document
from docx.enum.style import WD_STYLE_TYPE

from word_functions import create_table, set_text_color
import settings


def rotate_list(l:list, n:int):
    return l[-n:] + l[:-n]

def main(units:list):
    """
    Creates a document for each post. The document includes a 
    """
    units = units

    posts = [x for x in range(1, 16)]
    for i, unit in enumerate(units):
        for _, post in zip(unit, posts):
            # rotate group list
            rotation = rotate_list(unit, post-1)
            # create document
            doc = Document()
            heading = doc.add_heading(f'Poengliste for post {post}, pulje {i+1}', 0)
            heading_run = heading.runs[0]
            set_text_color(heading_run, settings.COLORS["dark"])
            # add table
            create_table(doc, post, rotation)
            # save document
            doc.save(f"dokumenter/pulje_{i+1}_post_{post}.docx")

def class_documents(units:list):
    """
    Creates a document for each class
    """


def create_groups():
    with open("classes.txt", "r") as file:
        classes = file.read().split(",")
    groups = []
    num_groups = len(classes)/2

    while len(groups) < num_groups:
        class1 = choice(classes)
        classes.remove(class1)
        class2 = choice(classes)
        classes.remove(class2)
        groups.append([class1, class2])
    
    with open("groups.txt", "w") as g_file:
        for group in groups:
            g_file.write(f"{group[0]},{group[1]} ")
    
def get_groups():
    with open("groups.txt", "r", encoding="UTF-8") as file:
        groups_str = file.read().split(" ")
    groups_str.remove("")
    groups = []
    for group in groups_str:
        groups.append(group.split(","))

    return groups

def make_units():
    groups = get_groups()

    unit1 = groups[int(len(groups)/2):]
    unit2 = groups[:int(len(groups)/2)]

    return [unit1, unit2]

if __name__ == "__main__":
    main(make_units())