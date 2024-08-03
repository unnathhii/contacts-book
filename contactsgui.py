import tkinter as tk
from tkinter import ttk, messagebox

contacts = {}

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

def view_contacts():
    for row in contact_tree.get_children():
        contact_tree.delete(row)
    
    for name, details in contacts.items():
        contact_tree.insert("", tk.END, values=(name, details['phone'], details['email'], details['address']))

def search_contact():
    search_term = entry_search.get()
    for row in contact_tree.get_children():
        contact_tree.delete(row)
    
    results = {name: details for name, details in contacts.items() if search_term in name or search_term in details['phone']}
    if not results:
        messagebox.showinfo("No Results", "No matching contacts found.")
    else:
        for name, details in results.items():
            contact_tree.insert("", tk.END, values=(name, details['phone'], details['email'], details['address']))

def update_contact():
    selected_item = contact_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No contact selected.")
        return

    name = contact_tree.item(selected_item)['values'][0]
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    messagebox.showinfo("Success", f"Contact {name} updated successfully!")
    view_contacts()

def delete_contact():
    selected_item = contact_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No contact selected.")
        return

    name = contact_tree.item(selected_item)['values'][0]
    del contacts[name]
    messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
    view_contacts()

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Manager")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Name").grid(row=0, column=0, sticky=tk.W)
ttk.Label(frame, text="Phone").grid(row=1, column=0, sticky=tk.W)
ttk.Label(frame, text="Email").grid(row=2, column=0, sticky=tk.W)
ttk.Label(frame, text="Address").grid(row=3, column=0, sticky=tk.W)

entry_name = ttk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, pady=5)
entry_phone = ttk.Entry(frame, width=30)
entry_phone.grid(row=1, column=1, pady=5)
entry_email = ttk.Entry(frame, width=30)
entry_email.grid(row=2, column=1, pady=5)
entry_address = ttk.Entry(frame, width=30)
entry_address.grid(row=3, column=1, pady=5)

button_frame = ttk.Frame(frame)
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

ttk.Button(button_frame, text="Add Contact", command=add_contact).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Update Contact", command=update_contact).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text="Delete Contact", command=delete_contact).grid(row=0, column=2, padx=5)

ttk.Label(root, text="Search").grid(row=1, column=0, pady=10)
entry_search = ttk.Entry(root, width=40)
entry_search.grid(row=2, column=0, pady=5)

ttk.Button(root, text="Search Contact", command=search_contact).grid(row=3, column=0, pady=5)
ttk.Button(root, text="View All Contacts", command=view_contacts).grid(row=4, column=0, pady=5)

contact_tree = ttk.Treeview(root, columns=("Name", "Phone", "Email", "Address"), show="headings")
contact_tree.heading("Name", text="Name")
contact_tree.heading("Phone", text="Phone")
contact_tree.heading("Email", text="Email")
contact_tree.heading("Address", text="Address")
contact_tree.grid(row=5, column=0, pady=10, sticky=(tk.W, tk.E))

root.mainloop()
