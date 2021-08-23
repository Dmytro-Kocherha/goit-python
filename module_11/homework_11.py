from collections import UserDict
import re
from datetime import datetime


class Field:
    pass


class Phone(Field):
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        flag = False
        if phone.startswith('+380') or phone.startswith('380'):
            res = re.search(
                r'(\+?380(67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7})', phone)
            if res:
                flag = True
                self.__phone = res.group()
        elif phone.startswith('0'):
            res = re.search(
                r'(0(67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7})', phone)
            if res:
                flag = True
                self.__phone = res.group()
        if not flag:
            print('Incorrect phone!')

    def __str__(self):
        return f'{self.__phone}'


class Name(Field):
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            print('Incorrect name!')

    def __str__(self):
        return f'{self.__name}'


class Birthday(Field):
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        flag = False
        date = birthday.split('.')
        if len(date) == 3:
            if int(date[0]) <= 31 and int(date[1]) <= 12:
                res = re.search(r'\d{1,2}\.\d{1,2}\.\d{4}', birthday)
                if res:
                    birthday_formatted = datetime.strptime(
                        res.group(), '%d.%m.%Y')
                    flag = True
                    self.__birthday = birthday_formatted
        if not flag:
            print('Incorrect date or format!\nTry to enter like the example: 14.06.2002')

    def __str__(self):
        if self.__birthday:
            return f'{self.__birthday.date()}'
        return 'None'

    def __repr__(self):
        if self.__birthday:
            return f'{self.__birthday.date()}'
        return 'None'


class Record:
    def __init__(self, name, phone, birthday):
        self.name = Name(name)
        self.phone = Phone(phone)
        if birthday:
            self.birthday = Birthday(birthday).__str__()
        else:
            self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday != 'None' and self.birthday:
            date_now = datetime.now()
            birth_date = datetime.strptime(self.birthday, '%Y-%m-%d')
            birth_date = birth_date.replace(year=date_now.year)
            if (birth_date - date_now).days < 0:
                birth_date = birth_date.replace(year=birth_date.year + 1)
                return (birth_date - date_now).days
            return -(date_now - birth_date).days

    def __str__(self):
        if self.birthday != 'None' and self.birthday:
            return f'{self.name},{self.phone},{Record.days_to_birthday(self)} days left to the birthday'
        return f'{self.name},{self.phone}'


class AddressBook(UserDict):
    def add_record(self, rec):
        self.data[rec.name.__str__()] = rec.__str__()
        if 'None' in self.data.keys():
            self.data.pop('None')

    def change_phone(self, rec):
        self.data[rec.name.__str__()] = rec.__str__()

    def find_phone(self, name):
        if name in self.data.keys():
            value = self.data[name]
            res = re.search(r'\+?\d+', value)
            return res.group()
        return 'Does not exist in database!'


def main():
    main_address_book = AddressBook()
    while True:
        command = input('Command: ').lower()
        sep_val = command.split(' ')
        if sep_val[0] == 'add' and len(sep_val) > 2:
            main_address_book.add_record(
                Record(sep_val[1].title(), sep_val[2], sep_val[3] if len(sep_val) == 4 else None))
        elif sep_val[0] == 'change' and len(sep_val) > 2:
            main_address_book.change_phone(
                Record(sep_val[1].title(), sep_val[2], sep_val[3] if len(sep_val) == 4 else None))
        elif sep_val[0] == 'phone':
            print(main_address_book.find_phone(sep_val[1].title()))
        elif sep_val[0] == 'show' and sep_val[1] == 'all':
            print(main_address_book)
        elif sep_val[0] in ['good bye', "close", "exit", '.']:
            print('Good bye!')
            break
        elif sep_val[0] == 'hello':
            print('How can I help you?')
        else:
            print('Incorrect! Try again')


if __name__ == '__main__':
    main()
