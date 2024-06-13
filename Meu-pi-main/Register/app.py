from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
import re

# Define the output path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Function to validate phone number
def is_valid_phone(phone):
    return re.match(r"^\d{10,15}$", phone)

# Function to check if password and confirm password match
def passwords_match(password, confirm_password):
    return password == confirm_password

# Function to validate all inputs
def validate_inputs():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    error_message = ""

    if not name:
        error_message += "Nome não pode estar vazio.\n"
    if not email or not is_valid_email(email):
        error_message += "Email inválido.\n"
    if not phone or not is_valid_phone(phone):
        error_message += "Telefone inválido. Deve conter apenas números e ter entre 10 e 15 dígitos.\n"
    if not password:
        error_message += "Senha não pode estar vazia.\n"
    if not confirm_password:
        error_message += "Confirme a Senha não pode estar vazio.\n"
    if password and confirm_password and not passwords_match(password, confirm_password):
        error_message += "As senhas não correspondem.\n"

    if error_message:
        error_label.config(text=error_message, fg="red")
    else:
        error_label.config(text="Cadastro realizado com sucesso!", fg="green")
        print("Cadastro realizado")
        # Aqui você pode adicionar o código para realmente realizar o cadastro

# Create the main window
window = Tk()
window.geometry("800x800")
window.configure(bg="#F39421")

# Create a canvas
canvas = Canvas(
    window,
    bg="#F39421",
    height=800,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Add title text
canvas.create_text(
    50.0,
    20.0,
    anchor="nw",
    text="Cadastro",
    fill="#FFFDFD",
    font=("MontserratItalic Medium", 48 * -1)
)

# Create entry fields with larger font
entry_name = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 16)
)
entry_name.place(
    x=35.0,
    y=140.0,
    width=730.0,
    height=50.0
)

entry_email = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 16)
)
entry_email.place(
    x=35.0,
    y=240.0,
    width=730.0,
    height=50.0
)

entry_phone = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 16)
)
entry_phone.place(
    x=35.0,
    y=340.0,
    width=730.0,
    height=50.0
)

entry_password = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 16),
    show="*"
)
entry_password.place(
    x=35.0,
    y=440.0,
    width=730.0,
    height=50.0
)

entry_confirm_password = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 16),
    show="*"
)
entry_confirm_password.place(
    x=35.0,
    y=540.0,
    width=730.0,
    height=50.0
)

# Add labels
canvas.create_text(
    45.0,
    110.0,
    anchor="nw",
    text="Nome",
    fill="#FFFFFF",
    font=("Lato Medium", 18 * -1)
)

canvas.create_text(
    45.0,
    210.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Lato Medium", 18 * -1)
)

canvas.create_text(
    45.0,
    310.0,
    anchor="nw",
    text="Telefone",
    fill="#FFFFFF",
    font=("Lato Medium", 18 * -1)
)

canvas.create_text(
    45.0,
    410.0,
    anchor="nw",
    text="Senha",
    fill="#FFFFFF",
    font=("Lato Medium", 18 * -1)
)

canvas.create_text(
    45.0,
    510.0,
    anchor="nw",
    text="Confirme a Senha",
    fill="#FFFFFF",
    font=("Lato Medium", 18 * -1)
)

# Add a Register button
register_button = Button(
    text="Register",
    font=("Helvetica", 16),
    bg="#4CAF50",
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    command=validate_inputs,
    relief="flat"
)
register_button.place(
    x=250.0,
    y=620.0,
    width=278.0,
    height=78.0
)

# Add error label
error_label = Label(
    window,
    text="",
    bg="#F39421",
    font=("Helvetica", 14)
)
error_label.place(
    x=35.0,
    y=710.0,
    width=730.0,
    height=50.0
)

# Run the main loop


window.resizable(False, False)
window.mainloop()
