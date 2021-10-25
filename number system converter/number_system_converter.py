from tkinter import *
from tkinter import messagebox
import math


def get_bin(input_string, base):
    first = str()
    second = str()
    while True:
        first_half, half = input_string.split(".")
        try:
            int(first_half, base)
            int(half, base)
        except ValueError:
            messagebox.showerror("Number converter", "Wrong input number type")
            break
        last_half = "." + half
        if base == 2:
            temp = first_half + last_half
            return temp

        elif base == 10:
            first = str(bin(int(first_half)))
            count = int(0)
            new_str = str()
            while True:
                new_1st, new_2nd = str(float(last_half) * 2).split(".")
                if float(last_half) == 0 or count == 30:
                    break
                new_str += new_1st
                last_half = "." + new_2nd
                count += 1
            second = new_str
            if not bool(second):
                second += "0"

        elif base == 8 or base == 16:
            second_bin = str()
            first = bin(int(first_half, base))
            for i in half:
                second_bin += str(bin(int(i, base)))[2::]
                if len(half) * round(math.sqrt(base)) != len(second_bin):
                    zeros = str()
                    for j in range(len(half) * round(math.sqrt(base)) - len(second_bin)):
                        zeros += "0"
                    second = zeros + second_bin
        break
    temp = first[2::] + "." + second
    return temp


def get_converted_nums(input_string):
    number_holder = list()
    final = str()
    temp_carrier = 0.0
    first_half, half = input_string.split(".")
    first_half = str(int(first_half, 2))
    first_half = str(int(first_half, 10))
    for i in range(len(half)):
        second_half = float(half[i]) * pow(2, i + 1)
        if bool(second_half):
            temp_holder = 1 / second_half
            temp_carrier = temp_holder + temp_carrier
        second_half = str(temp_carrier)[1::]
        final = first_half + second_half
    number_holder.append(final)
    first_half, half = input_string.split(".")
    first_half = str(oct(int(first_half, 2)))[2::]
    temp = str()
    oct_second = str()
    while True:
        if len(half) % 3 != 0:
            half += "0"
        else:
            break
    for i in range(len(half)):
        if (i + 1) % 3 != 0:
            temp += half[i]
        else:
            temp += half[i]
            oct_second += str(oct(int(temp, 2)))[2::]
            temp = " "
    number_holder.append(first_half + "." + oct_second)
    first_half, half = input_string.split(".")
    first_half = str(hex(int(first_half, 2)))[2::]
    hex_temp = str()
    hex_second = str()
    while True:
        if len(half) % 4 != 0:
            half += "0"
        else:
            break
    for i in range(len(half)):
        if (i + 1) % 4 != 0:
            hex_temp += half[i]
        else:
            hex_temp += half[i]
            hex_second += str(hex(int(hex_temp, 2)))[2::]
            hex_temp = " "
    number_holder.append(first_half + "." + hex_second)
    return number_holder


bin_holder = str()
nums_holder = list()
root = Tk()
root.title("Number converter")
photo = PhotoImage(file="converter.png")
root.iconphoto(True, photo)
root.resizable(0, 0)
frame1 = LabelFrame(root, text="Enter a number", padx=10, pady=10)
input_field = Entry(frame1, borderwidth=5, width=40)
frame2 = LabelFrame(root, text="Conversions", padx=10, pady=10)
frame1.pack(padx=5, pady=5, anchor=W, fill='both', expand=False)
label1 = Label(frame2)
label2 = Label(frame2)
label3 = Label(frame2)

clicked = StringVar()
clicked.set("Binary")
frame1['text'] = "Convert" + " " + clicked.get() + " " + "to others"


def update_txt(foo):
    frame1['text'] = "Convert" + " " + clicked.get() + " " + "to others"
    input_field.delete(0, END)


drop = OptionMenu(frame1, clicked, "Decimal", "Binary", "Octal", "Hexadecimal", command=update_txt).pack(anchor=W)
input_field.pack(padx=5, pady=5, anchor=W)


def get_base():
    temp = int()
    if clicked.get() == "Decimal":
        temp = 10
    elif clicked.get() == "Binary":
        temp = 2
    elif clicked.get() == "Octal":
        temp = 8
    elif clicked.get() == "Hexadecimal":
        temp = 16
    return temp


def show_results():
    temp_base = get_base()
    global label1, label2, label3
    if temp_base == 2:
        label1['text'] = "decimal: " + nums_holder[0]
        label2['text'] = "octal: " + nums_holder[1]
        label3['text'] = "hexadecimal: " + nums_holder[2].upper()
    elif temp_base == 8:
        label1['text'] = "decimal: " + nums_holder[0]
        label2['text'] = "binary: " + bin_holder
        label3['text'] = "hexadecimal: " + nums_holder[2].upper()
    elif temp_base == 10:
        label1['text'] = "binary: " + bin_holder
        label2['text'] = "octal: " + nums_holder[1]
        label3['text'] = "hexadecimal: " + nums_holder[2].upper()
    elif temp_base == 16:
        label1['text'] = "decimal: " + nums_holder[0]
        label2['text'] = "binary: " + bin_holder
        label3['text'] = "octal: " + nums_holder[1]
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label1.pack(anchor=W)
    label2.pack(anchor=W)
    label3.pack(anchor=W)


def get_input():
    global bin_holder
    global nums_holder
    entry_holder = input_field.get().lower()
    if not bool(entry_holder):
        messagebox.showerror("Number converter", "Empty input")
    else:
        if "." not in entry_holder:
            entry_holder += ".0"
        bin_holder = get_bin(str(entry_holder), get_base())
        nums_holder = get_converted_nums(bin_holder)
    frame2.pack_forget()
    frame2.pack(padx=5, pady=5, anchor=W, fill='both', expand=False)
    show_results()


button1 = Button(frame1, text="convert", width=10, command=get_input)
button1.pack(padx=5, pady=5, anchor=W)
root.mainloop()

# check if results are 99.99 % accurate
