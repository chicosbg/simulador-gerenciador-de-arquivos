from tkinter import *
window =Tk()
keys = ["foo", "bar"]
count = 0
labels=[]
def change_text():
    for j,l in enumerate(labels):
        l.config(text=str(keys[j])+str(j))
for key in keys:
    # I can access the first variable created statically, but what about the others?
    labels.append(Label(window,text=key))
    labels[count].grid(row = count, column = 1)
    count += 1
print(labels)
Button(window,text="Change Text",command=change_text).grid(row=count, column=0)
window.mainloop()