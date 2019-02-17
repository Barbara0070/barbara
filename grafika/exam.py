import tkinter
root = tkinter.Tk()
#pyinstaller --onefile file
def suma():
    print("nacisnieto przycisk")
    a = a_entry.get()
    b= b_entry.get()
    suma=int(a)+int(b)
    wynik.configure(text=f"{suma}")

a_label = tkinter.Label(master=root,text="costam")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()


b_label = tkinter.Label(master=root,text="costam")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

button = tkinter.Button(master=root,text="sum", command=suma)
button.pack()

wynik = tkinter.Label(master=root,text="costam")
wynik.pack()



root.mainloop()