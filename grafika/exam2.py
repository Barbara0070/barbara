import tkinter
root = tkinter.Tk()
root.columnconfigure(1, weight=1)

def suma():
    print("nacisnieto przycisk")
    a = a_entry.get()
    b= b_entry.get()
    suma=int(a)+int(b)
    wynik.configure(text=f"{suma}")

a_label = tkinter.Label(master=root,text="costam")
a_label.grid(row=0,column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0,column=1)


b_label = tkinter.Label(master=root,text="costam")
b_label.grid(row=1,column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1,column=1)

button = tkinter.Button(master=root,text="sum", command=suma)
a_label.grid(row=2,column=0)

wynik = tkinter.Label(master=root,text="costam")
a_label.grid(row=3,column=0)



root.mainloop()