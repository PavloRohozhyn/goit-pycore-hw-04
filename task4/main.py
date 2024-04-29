""" sys modules """
import sys


def parse_input(user_input):
    """ parse input data """

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts) -> str:
    """ add contact """

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts) -> str:
    """ change contact """

    name, phone = args
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts) -> dict:
    """ show phone """

    name = args
    return [contacts[name]]


def show_all(args, contacts):
    """ shoa all """
    res = []
    for name, phone in contacts:
        res.append({"name": name, "phone": phone})    
    return res


# Main
def main():
    """ bot commands hendler """
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        # close, exit
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # hello
        elif command == "hello":
            print("How can I help you?")
        
        # add
        elif command in ["add"]:
            add_contact('add', ['test', '00000000000'])
            print("Contact added.")
        
        # change
        elif command in ['change']:
            change_contact(command, ['name1', '11111111111'])
            print("Contact updated.")

        # phone
        elif command in ['phone']:
            show_phone(command, ['test2'])

        # all
        elif command in ['all']:
            show_all(command, [])

        
        # something else
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
