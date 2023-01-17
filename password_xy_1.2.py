import random
import string
import customtkinter

customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("600x370")
root.title("Passwort Generator")

def generate_password():
  digits = entry.get()
  password = ""
  characters = string.ascii_letters + string.digits + string.punctuation
  for i in range(int(digits)):
    password += random.choice(characters)
    password_label.configure(text=password) 

def copy_password():
  password = password_label.cget("text")
  print(password)
  frame.clipboard_clear()
  frame.clipboard_append(password) 
  done_label.configure(text="kopiert!")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(frame, text="Passwort Generator", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(frame, width=95, placeholder_text="Anzahl Stellen", placeholder_text_color="#F0FFFF")
entry.pack(pady=12, padx=10)

generate_button = customtkinter.CTkButton(frame, text="Passwort generieren", command=generate_password)
generate_button.pack(pady=12, padx=10)

copy_button = customtkinter.CTkButton(frame, text="Passwort kopieren", command=copy_password)
copy_button.pack(pady=12, padx=10)


password_label=customtkinter.CTkLabel(frame, text="", font=("Roboto", 24))
password_label.pack(pady=12, padx=10)

done_label = customtkinter.CTkLabel(frame, text="", font=("Roboto", 20))
done_label.pack(pady=12, padx=10)

root.mainloop()


