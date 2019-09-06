import pickle

from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5
TIME_QUERY = 2

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Que opcion deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponibles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto o agenda")
    print("3 - Buscar contacto")
    print("4 - Exportar contacto a un CSV")
    print("5 - Salir")

    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(TIME_QUERY)


def remove_contact(contacts):
    print("\n\nEliminar contacto\n")
    print("1 - Eliminar contacto \n2 - Borrar agenda de contactos")
    user_action = int(input("¿Qué deseas hacer? "))
    if user_action == 1:
        if len(contacts) != 0:
            contact_delete = input("Nombre de la persona que desea eliminar: ")
            contact_counter = 0

            for contact in contacts:
                if contact_delete == contact["name"]:
                    del contacts[contact_counter]
                    save_contacts(contacts)
                contact_counter += 1

            if contact_delete not in contacts:
                print("No se encontro ningun contacto con el nombre de {}\n\n".format(contact_delete))
            sleep(TIME_QUERY)
            return contacts

        else:
            print("No existe ninguna agenda actualmente\n\n")

    elif user_action == 2:
        del contacts
        save_contacts([])

    sleep(TIME_QUERY)
    return


def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introducir el nombre o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos: ")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.\n\n")
        sleep(TIME_QUERY)
        return

    print("\nInformación sobre {}\n\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(TIME_QUERY)

    return found_contacts


def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.\n\n")


def main():
    contacts = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()

        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()
