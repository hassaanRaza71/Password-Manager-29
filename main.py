from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_input.delete(0,END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password_generated = "".join(password_list)
    password_input.insert(END,password_generated)
    pyperclip.copy(password_generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name=website_input.get()
    email_name=email_input.get()
    password=password_input.get()
    if len(website_name)==0 or len(password)==0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")
        return
    
    is_ok=messagebox.askokcancel(title=website_name, message=f"These are the details entered:\nEmail: {email_name}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        with open("password.txt","a") as file:
            file.write(f"{website_name} | {email_name} | {password}\n")
        file.close()
        
        website_input.delete(0,END)
        password_input.delete(0,END)
        website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

website_input=Entry(width=35)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()

email_input=Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(END,"faculty123@gmail.com")

password_input=Entry(width=21)
password_input.grid(column=1,row=3)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)






window.mainloop()