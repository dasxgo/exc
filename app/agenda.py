def save_contacts():
    contacts = {} 

    while True:
        name = input("Enter the name of the contact (or 'exit' to finish):")
        if name.lower() == 'exit':
            break

        phone = input('Enter the phone number: ')
        contacts[name] = phone

    return contacts

def view_contacts(contacts):
    print ('Contacts list:')
    for name, phone, in contacts.items():
        print(f'{name}: {phone}') 

def main():
    print('Welcome to the contact list')
    agenda = save_contacts()
    view_contacts(agenda)

if __name__ == '__main__':
    main()




'''def guardar_contactos():
    contactos = {} 

    while True:
        nombre = input("ingresa el nombre del contacto (o 'salir' para terminar):")
        if nombre.lower() == 'salir':
            break

        telefono = input('ingresa el numero de telefono: ')
        contactos[nombre] = telefono 

    return contactos

def mostrar_contactos(contactos):
    print ('lista de contactos:')
    for nombre, telefono, in contactos.items():
        print(f'{nombre}: {telefono}') 

def main():
    print('Bienvenido a la agenda de contactos')
    agenda = guardar_contactos()
    mostrar_contactos(agenda)

if __name__ == '__main__':
    main()'''

