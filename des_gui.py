import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(plain_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def decrypt(encrypted_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()

def handle_encrypt():
    plain_text = input_entry.get()
    key = key_entry.get()

    if len(key) != 8:
        messagebox.showerror("Error", "Key must be exactly 8 characters long!")
        return

    encrypted_text = encrypt(plain_text, key)
    output_entry.delete(0, tk.END)
    output_entry.insert(0, encrypted_text)

def handle_decrypt():
    encrypted_text = input_entry.get()
    key = key_entry.get()

    if len(key) != 8:
        messagebox.showerror("Error", "Key must be exactly 8 characters long!")
        return

    try:
        decrypted_text = decrypt(encrypted_text, key)
        output_entry.delete(0, tk.END)
        output_entry.insert(0, decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", "Invalid encrypted text or key!")

# GUI setup
root = tk.Tk()
root.title("DES Encryption")

# Input text
input_label = tk.Label(root, text="Input Text:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1, padx=5, pady=5)

# Key
key_label = tk.Label(root, text="Key (8 chars):")
key_label.grid(row=1, column=0, padx=5, pady=5)
key_entry = tk.Entry(root, width=40)
key_entry.grid(row=1, column=1, padx=5, pady=5)

# Output text
output_label = tk.Label(root, text="Output Text:")
output_label.grid(row=2, column=0, padx=5, pady=5)
output_entry = tk.Entry(root, width=40)
output_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=handle_encrypt)
encrypt_button.grid(row=3, column=0, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=handle_decrypt)
decrypt_button.grid(row=3, column=1, pady=10)

root.mainloop()