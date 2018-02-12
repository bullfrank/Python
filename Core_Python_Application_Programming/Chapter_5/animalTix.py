from tkinter import tix, Label, END
#from tix import ComboBox

top = tix.Tk()

lb = tix.Label(top, text = 'Animal(in pairs; min: pair, max: dozen)')
lb.pack()

ct = tix.Control(top, label = 'Number:', integer = True, max = 12, min = 2, value = 2, step = 2)
ct.label.config(font = 'Helvetica -14 bold')
ct.pack()

cb = tix.ComboBox(top, label = 'Type:', editable = True)
for animal in ('dog', 'cat', 'hamster', 'python'):
    cb.insert(END, animal)
cb.pack()

bt = tix.Button(top, text = 'QUIT', command = top.destroy, bg = 'red', fg = 'white')
bt.pack()


top.mainloop()
