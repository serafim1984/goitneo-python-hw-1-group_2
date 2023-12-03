contacts = {}


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


def phone_contact(args, contacts):
    name = args[0]
    contact_phone = contacts[name]
    return contact_phone


def all_contact():
    global contacts
    all_contacts = ""
    for name, phone in contacts.items():
        all_contacts = all_contacts + name + " " + phone + "\n"
    return all_contacts[:-1]


def main():
    global contacts
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "all":
            print(all_contact())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
