import re

CONTACTS_DICT = {}


def input_error(func):
    def inner(*args):
        if 1 < len(args) <= 2:
            result = re.search(r'\+?380\d+|0\d+', args[1])
            if not args[0].isalpha():
                print('Enter correct username!')
            if result:
                if len(args[1]) != len(result.group()) or len(args[1]) < 10:
                    print('Enter correct number!')
                else:
                    func(args[0], args[1])
            else:
                print('Enter correct number!')
        else:
            if not args[0] in CONTACTS_DICT.keys():
                print('Contact does not exist!')
            else:
                print(func(args[0]))

    return inner


@input_error
def add_change_handle(name, contact):
    CONTACTS_DICT[name] = contact


@input_error
def handle_phone(name):
    return CONTACTS_DICT[name]


def handle_show_all():
    return CONTACTS_DICT


def main():
    while True:
        command = input('Command: ').lower()
        sep_value = command.split(' ')
        if sep_value[0] == 'add' and len(sep_value) > 2 or sep_value[0] == 'change' and len(sep_value) > 2:
            add_change_handle(sep_value[1].title(), sep_value[2])
        elif sep_value[0] == 'phone':
            handle_phone(sep_value[1].title())
        elif sep_value[0] == 'show' and sep_value[1] == 'all':
            print(handle_show_all())
        elif sep_value[0] in ['good bye', "close", "exit", '.']:
            print('Good bye!')
            break
        elif sep_value[0] == 'hello':
            print('How can I help you?')
        else:
            print('Incorrect! Try again')


main()
