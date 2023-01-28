commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']

def main_menu() -> int:
    print ('Главное меню:')
    for i, item in enumerate(commands, 1) :
        print(f'\t{i}. {item}')
    choice = int(input('Выберите пункт меню: '))
    return choice
def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()
def input_error():
    print('Некорректный выбор. Введите корректный пункт меню.')
def create_new_contact():
    name = input ('Введите имя и фамилию: ')
    phone = input ('Введите телефон: ')
    comment = input ('Введите комментарий: ')
    return name, phone, comment
def find_contact():
    find = input('Введите искомый контакт: ')
    return find                    
def exit_program():
    print()
    print("Выход из программы...")
    print()
    exit()

def empty_request():
    print('Искомый контакт не найден!')

def many_request():
    print('Введите более точные данные. Очень много совпадений')

def select_contact(massage: str):
    contact = input(massage)
    return contact

def change_contact():
    print('Введите новые данные (если вы передумали - нажмите Enter)')
    name = input ('Введите имя и фамилию: ')
    phone = input ('Введите телефон: ')
    comment = input ('Введите комментарий: ')
    return name, phone, comment
def delete_confirm(contact: str):
    result =  input(f"Вы действительно хотите удалить контакт {contact[0]} {contact[1]} {contact[2]}? (y/n): ").lower()
    if result == 'y':
        return True 
    else:
        return False 
