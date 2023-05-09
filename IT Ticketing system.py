import tkinter as tk
from tkinter import messagebox

class TicketingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Ticketing System")

        # This part create widgets
        self.title_label = tk.Label(self.master, text="Ticketing System", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack()

        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        self.category_label = tk.Label(self.master, text="Category:")
        self.category_label.pack()
        self.category_var = tk.StringVar()
        self.category_dropdown = tk.OptionMenu(self.master, self.category_var, "General", "Technical", "Sales")
        self.category_dropdown.pack()

        self.message_label = tk.Label(self.master, text="Message:")
        self.message_label.pack()
        self.message_text = tk.Text(self.master, height=5)
        self.message_text.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_ticket)
        self.submit_button.pack(pady=10)

    def submit_ticket(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        category = self.category_var.get()
        message = self.message_text.get("1.0", tk.END)

        # This is the databas this txt file stores all the tickets that a customer create.
        with open("tickets.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Category: {category}\n")
            file.write(f"Message: {message}\n")
            file.write("=" * 50 + "\n")

        # These are the self code.
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.category_var.set("General")
        self.message_text.delete("1.0", tk.END)

        # This is the conformation message code.
        messagebox.showinfo("Ticket Submitted successfully", "Please wait until a techinition reach out to you thanks.")

root = tk.Tk()
app = TicketingSystem(root)
root.mainloop()
