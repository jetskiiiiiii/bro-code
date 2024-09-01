a = [{1, 2, 3}, {1, 5, 9}, {1, 4, 7}, {3, 6, 9}, {3, 4, 7}, {7, 8, 9}, {2, 5, 8}]
b = {"p": {1, 4, 9, 7}}
c = {2, 4, 5, 8, 1, 9}
c = {2, 4}

# for i in a:
# print(i, c)
# print(i - c, c - i)
x = [True for i in a if ((i - c) == set())]

print(x)

# x = True if ((i - c) == set()) else False
# print(all(a))

# else:
#     print(False)

# if any(a) in b["p"]:
#     print(1)
# else:
#     print(0)

###
# from tkinter import *


# def onObjectClick(event):
#     print("Got object click", event.x, event.y)
#     print(event.widget.find_closest(event.x, event.y))


# root = Tk()
# canv = Canvas(root, width=100, height=100)
# obj1Id = canv.create_line(0, 30, 100, 30, width=5, tags="obj1Tag")
# obj2Id = canv.create_text(50, 70, text="Click", tags="obj2Tag")

# canv.tag_bind(obj1Id, "<ButtonPress-1>", onObjectClick)
# canv.tag_bind("obj2Tag", "<ButtonPress-1>", onObjectClick)
# print("obj1Id: ", obj1Id)
# print("obj2Id: ", obj2Id)
# canv.pack()
# root.mainloop()

###
# a = [0, 1, 2]


# def x(a, b, c):
#     print(a, b, c)


# x(*a)
###
