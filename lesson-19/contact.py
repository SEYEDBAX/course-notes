import json
from rich.console import Console

console = Console()

class ContactManager:

    def __init__(self):
        self.contacts = {}
        try:
            self.load_contacts()
        except FileNotFoundError:
            self.save_contacts()

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            f.write(json.dumps(self.contacts))

    def load_contacts(self):
        with open("contacts.json", "r") as f:
            self.contacts = json.loads(f.read())

    def add_contact(self, name, phone, email=None, address=None):
        if name in self.contacts:
            console.print(f"[red]{name} is already in the contact list.[/red]", style="bold")
            return
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        console.print(f"[green]{name} has been added to the contact list.[/green]", style="bold")
        self.save_contacts()

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            console.print(f"[red]{name} has been removed from the contact list.[/red]", style="bold")
        else:
            console.print(f"[blue]{name} is not in the contact list.[/blue]", style="bold")

    def search_contact(self, query):
        finds = []
        for key in self.contacts:
            if query in key:
                finds.append(key)
        
        if finds:
            for name in finds:
                console.print(f"[green]{name} :[/green] {self.contacts[name]['phone']} - {self.contacts[name]['email']}", style="bold")
        else:
            console.print(f"[blue]No contact found.[/blue]", style="bold")
        
    def list_contacts(self):
        i = 1
        for name, contact in self.contacts.items():
            console.print(f"{i}. {name} ([green]phone :[/green] {contact['phone']}) - ([yellow]email:[/yellow] {contact['email']})")
            i += 1
    @staticmethod
    def get_input(message, force=False):
        value = input(message)
        if force and not value:
            return ContactManager.get_input(message, force)
        return value if value else None

    def menu(self):
        console.print("[magenta]Contact Manager[/magenta]", style="bold")
        console.print("1. Add Contact")
        console.print("2. Remove Contact")
        console.print("3. List Contacts")
        console.print("4. Search Contact")
        console.print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = self.get_input("Enter name: ", force=True)
            phone = self.get_input("Enter phone number: ", force=True)
            email = self.get_input("Enter email (optional): ")
            address = self.get_input("Enter address (optional): ")
            self.add_contact(name, phone, email, address)
            self.goto_menu()
        elif choice == 2:
            name = self.get_input("Enter name: ", force=True)
            self.remove_contact(name)
            self.goto_menu()
        elif choice == 3:
            self.list_contacts()
            self.goto_menu()
        elif choice == 4:
            query = self.get_input("Enter query: ", force=True)
            self.search_contact(query)
            self.goto_menu()
        elif choice == 5:
            console.print("Goodbye!")
            exit()
    
    def goto_menu(self):
        goto = self.get_input("Enter 'q' to exit or any other key to go to menu: ")
        if goto == "q":
            exit()
        else:
            self.menu()

contact_manager = ContactManager()
contact_manager.menu()