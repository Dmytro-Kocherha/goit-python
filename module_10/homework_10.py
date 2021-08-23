from collections import UserDict


class Name:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Phone:

    def __init__(self, phone=[]):
        self.phone = phone

    def add_number(self, number):
        self.phone.append(number)

    def del_number(self, number):
        self.phone.remove(number)

    def change_number(self, old_number, new_number):
        if old_number in self.phone:
            self.del_number(old_number)
            self.add_number(new_number)

    def __str__(self):
        return str(self.phone)


class Record:

    def __init__(self, name, phone=Phone()):
        self.phone = phone
        self.name = Name(name)

    def add_number(self, number):
        if number.startswith('+38'):
            self.phone.add_number(number)

    def del_number(self, number):
        self.phone.del_number(number)

    def __str__(self):
        return f'{self.name},{self.phone}'


class AddressBook(UserDict):

    def add_record(self, name, number=[]):
        self.data[name] = Record(name, Phone(number))

    def change_phone(self, name, number):
        self.data[name] = Record(name, Phone(number))

    def find_phone(self, name):
        return self.data[name]

    def del_number(self, name):
        self.data.pop(name)

    def __str__(self):
        temp = ''
        for key, val in self.data.items():
            temp += f'{str(key)}:{str(val)}\n'
        return temp


def main():
    main_address_book = AddressBook()
    while True:
        command = input('Command: ').lower()
        sep_val = command.split(' ')
        if sep_val[0] == 'add' and len(sep_val) > 2:
            main_address_book.add_record(sep_val[1].title(), sep_val[2])
        elif sep_val[0] == 'change' and len(sep_val) > 2:
            main_address_book.change_phone(sep_val[1].title(), sep_val[2])
        elif sep_val[0] == 'phone':
            print(main_address_book.find_phone(sep_val[1].title()))
        elif sep_val[0] == 'show' and sep_val[1] == 'all':
            print(main_address_book)
        elif sep_val[0] == 'del':
            print(main_address_book)
            main_address_book.del_number(sep_val[1].title())
            print(main_address_book)
        elif sep_val[0] in ['good bye', "close", "exit", '.']:
            print('Good bye!')
            break
        elif sep_val[0] == 'hello':
            print('How can I help you?')
        else:
            print('Incorrect! Try again')


main()
