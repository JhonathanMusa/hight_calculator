from tkinter import Tk, Button, Label, DoubleVar, Entry

# Windows properties
window = Tk()
window.title("Feet to meter Converter App")
window.config(background="grey")
window.geometry("340x200")
window.resizable(width=False, height=False)

# functions


def convert():
    value = float(ft_value.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)


def clear():
    ft_value.set("")
    mt_value.set("")


# labels properties
# feet label properties
ft_lb = Label(window, text="Feet", bg="#184059", fg="white", width=14)
ft_lb.grid(column=0, row=0, padx=50, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0, pady=30)
ft_entry.delete(0, 'end')

# meter label properties
mt_lb = Label(window, text="Meter", bg="#184059", fg="white", width=14)
mt_lb.grid(column=0, row=1, padx=10, pady=15)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=1, row=1, pady=30)
mt_entry.delete(0, 'end')

# buttons
btn_convert = Button(window, text="Convert",
                     bg="#184059", fg="white", widt=14, command=convert)
btn_convert.grid(column=0, row=2)

btn_clear = Button(window, text="Clear", bg="#184059", fg="white", width=14, command=clear)
btn_clear.grid(column=1, row=2)

window.mainloop()
