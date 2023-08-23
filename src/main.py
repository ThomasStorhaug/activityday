"""
groups: two units with half of the groups; each group has two classes

post names: 1-15

30 posts, 15 unique posts per unit

documents:
    one for each post with a table:
        Four columns - class 1 | points | class 2 | points

values needed for table: postname, rotation
        
"""
from docx import Document

from word_functions import create_table


def rotate_list(l:list, n:int):
    return l[n:] + l[:n]

def main():
    groups = []

    posts = [str(x) for x in range(1, 16)]

    for i, post in enumerate(posts):
        # rotate group list
        rotation = rotate_list(groups, i)
        # create document
        doc = Document()
        # add table
        create_table(doc, post, rotation)
        # save document
        doc.save("test.docx")

if __name__ == "__main__":
    main()