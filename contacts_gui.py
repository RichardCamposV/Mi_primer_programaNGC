import pickle

from time import sleep
from tkinter import *
from tkinter import ttk


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


def add_contact(contacts, name, phone, email):
    contact = {
            "name": name,
            "phone": phone,
            "email": email
    }
    contacts.append(contact)
    return contact


def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact = add_contact(contacts, name, phone, email)
    cols, row = frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=row, sticky=W)
    ttk.Label(frame_contact_list, text=contact["phone"]).grid(column=2, row=row, sticky=W)
    ttk.Label(frame_contact_list, text=contact["email"]).grid(column=3, row=row, sticky=W)
    # se restaura el padding anterior con el que sigue, ya que cuenta en total los 7 widgets
    configure_grid(frame_contact_list, 20, 0)

    save_contacts(contacts)


def configure_grid(frame, x, y):
    for child in frame.winfo_children():
        child.grid_configure(padx=x, pady=y)


def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(contacts, input("Nombre: "), input("Teléfono: "), input("Email: "))
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
    search_term = ""
    user_action = int(input("Buscar por nombre (1) / Buscar por correo electronico (2): "))
    if user_action == 1:
        search_term = input("Introducir el nombre o parte de él: ")
    elif user_action == 2:
        search_term = input("Introducir el correo electronico o parte de él: ")

    found_contacts = []

    print("He encontrado los siguientes contactos: ")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"] and contact["email"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        user_action = int(input("Buscar contacto (1) / Regresar al menu principal (2): "))
        if user_action == 1:
            return find_contact(contacts)
        else:
            sleep(TIME_QUERY)
            return

    print("\nInformación sobre {}\n\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(TIME_QUERY)

    return found_contacts


def export_contacts():
    pass


def print_contacts_ttk(contacts, frame):
    contact = contacts

    for data in contact:
        cols, row = frame.grid_size()
        cols = 1
        for member in data:
            ttk.Label(frame, text=data[member]).grid(column=cols, row=row, sticky=W)
            cols += 1


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
    # contacts = []
    contacts = load_contacts()

    root = Tk()
    root.title("Contacts")

    frame_add_contact = ttk.Frame(root, padding="30 30 30 20")
    frame_add_contact.grid()

    frame_contact_list = ttk.Frame(root, padding="30 0 30 50")
    frame_contact_list.grid()

    name = StringVar()
    email = StringVar()
    phone = StringVar()

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1, sticky=(W, E))
    ttk.Label(frame_add_contact, text="Telefono").grid(column=3, row=1, sticky=W)

    ttk.Entry(frame_add_contact, width=30, textvariable=name).grid(column=1, row=2, sticky=W)
    ttk.Entry(frame_add_contact, width=30, textvariable=email).grid(column=2, row=2, sticky=(W, E))
    ttk.Entry(frame_add_contact, width=15, textvariable=phone).grid(column=3, row=2, sticky=E)

    ttk.Label(frame_contact_list, text="Diary:").grid(column=1, row=1, sticky=W)

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=2, sticky=W)
    ttk.Label(frame_contact_list, text="Telefono").grid(column=2, row=2, sticky=(W, E))
    ttk.Label(frame_contact_list, text="Email").grid(column=3, row=2, sticky=W)

    print_contacts_ttk(contacts, frame_contact_list)

    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3)

    configure_grid(frame_contact_list, 20, 10)

    # root.bind('<Return>', add_contact_tk)

    root.mainloop()

    print("hi8")


if __name__ == "__main__":
    main()
