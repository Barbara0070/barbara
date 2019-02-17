import tkinter
root = tkinter.Tk()
root.columnconfigure(1, weight=1)

def policz():
    print("nacisnieto przycisk")
    a = float(a_entry.get())
    b= float(b_entry.get())
    razem=a*b/100
    wynik.configure(text=f"{razem}")

a_label = tkinter.Label(master=root,text="spalanie")
a_label.grid(row=0,column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0,column=1)


b_label = tkinter.Label(master=root,text="cena")
b_label.grid(row=1,column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1,column=1)

button = tkinter.Button(master=root,text="sum", command=policz)
button.grid(row=2,column=0)

wynik = tkinter.Label(master=root,text="costam")
wynik.grid(row=3,column=0)



root.mainloop()