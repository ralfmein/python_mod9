def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid input"
        except IndexError:
            return "Invalid command"

    return wrapper


def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added"


def change_phone(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Phone number updated"
    else:
        raise KeyError


def get_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


def show_all(contacts):
    if not contacts:
        return "No contacts found"
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


@input_error
def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            parts = command.split(" ")
            if len(parts) == 3:
                _, name, phone = parts
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid input")
        elif command.startswith("change "):
            parts = command.split(" ")
            if len(parts) == 3:
                _, name, phone = parts
                print(change_phone(contacts, name, phone))
            else:
                print("Invalid input")
        elif command.startswith("phone "):
            name = command.split(" ", 1)[-1]
            print(get_phone(contacts, name))
        elif command == "show all":
            print(show_all(contacts))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
