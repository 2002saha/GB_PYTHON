
phone_book = []
path = 'hometask\lesson_7\data.txt'

def get_phone_book():
    global phone_book
    return phone_book

def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if  find in field:
                result.append(contact)
                break
    return result

def open_file():
    global phone_book
    global path
    with open (path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))

def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open (path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))

def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)

def get_contact(text: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if  text in field:
                result.append(contact)
                break
    if len(result) > 1:
        return False
    else:
        return result 
def delete_contact(contact: list):
    global phone_book
    phone_book.remove(contact)


