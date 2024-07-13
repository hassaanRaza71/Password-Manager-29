from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    search_website = website_input.get().strip().lower()
    if len(search_website) == 0:
        messagebox.showwarning(title="Oops!", message="Please enter the website name.")
    else:
        try:
            with open("password.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No Data File Found.")
        else:
            if search_website in data:
                email_searched = data[search_website]["email"]
                password_searched = data[search_website]["password"]
                messagebox.showinfo(title=search_website.title(), message=f"Email: {email_searched}\nPassword: {password_searched}")
            else:
                messagebox.showwarning(title="Error", message="Website Not Found.")


    
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
    new_data={
        website_name:{"email":email_name,
                 "password":password
                 }
    }
    if len(website_name)==0 or len(password)==0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")
    
    
    else:
        try:
            with open("password.json","r") as file:
                data=json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("password.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            with open("password.json","w") as file:
                json.dump(data,file,indent=4)  
        finally:
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

website_input=Entry(width=32)
website_input.grid(column=1,row=1)
website_input.focus()

email_input=Entry(width=51)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(END,"faculty123@gmail.com")

password_input=Entry(width=32)
password_input.grid(column=1,row=3)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

search_button=Button(text="Search",width=14,command=search)
search_button.grid(column=2,row=1)

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)

add_button=Button(text="Add",width=44,command=save)
add_button.grid(column=1,row=4,columnspan=2)






window.mainloop()