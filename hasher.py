import hashlib
import tkinter as tk
from tkinter import messagebox

def generate_hash():
    password = password_entry.get()
    hash_algorithm = hash_option.get()
    
    if password:
        if hash_algorithm == "SHA-256":
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
        elif hash_algorithm == "SHA-1":
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
        elif hash_algorithm == "MD5":
            hashed_password = hashlib.md5(password.encode()).hexdigest()
        elif hash_algorithm == "SHA-512":
            hashed_password = hashlib.sha512(password.encode()).hexdigest()
        elif hash_algorithm == "SHA-384":
            hashed_password = hashlib.sha384(password.encode()).hexdigest()
        elif hash_algorithm == "SHA-224":
            hashed_password = hashlib.sha224(password.encode()).hexdigest()
        
        hash_output.config(state=tk.NORMAL)
        hash_output.delete("1.0", tk.END)
        hash_output.insert(tk.END, hashed_password)
        hash_output.config(state=tk.DISABLED)
    else:
        messagebox.showwarning("Empty Password", "Please enter a password.")

def copy_to_clipboard():
    hash_text = hash_output.get("1.0", tk.END).strip()
    if hash_text:
        root.clipboard_clear()
        root.clipboard_append(hash_text)
        messagebox.showinfo("Copied", "Hashed password copied to clipboard.")
    else:
        messagebox.showwarning("No Hash", "No hash to copy. Generate a hash first.")

root = tk.Tk()
root.title("Password Hash Generator")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

hash_option = tk.StringVar(root)
hash_option.set("SHA-256")

hash_dropdown = tk.OptionMenu(root, hash_option, "SHA-256", "SHA-1", "MD5", "SHA-512", "SHA-384", "SHA-224")
hash_dropdown.pack()

generate_button = tk.Button(root, text="Generate Hash", command=generate_hash)
generate_button.pack()

output_label = tk.Label(root, text="Hashed Password:")
output_label.pack()
hash_output = tk.Text(root, height=1, width=64)
hash_output.config(state=tk.DISABLED)
hash_output.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
