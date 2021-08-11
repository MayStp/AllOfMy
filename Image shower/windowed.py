import tkinter

main_window = tkinter.Tk()

gambar = tkinter.PhotoImage(file= 'susah.png')

def event_pencet():
    label2 = tkinter.Label(main_window, image= gambar)
    label2.pack()

label  = tkinter.Label(main_window, text="Welcome")
tombol = tkinter.Button(main_window, text="click here" ,command= event_pencet) 


label.pack()
tombol.pack()
main_window.mainloop()