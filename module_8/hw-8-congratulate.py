from datetime import datetime, timedelta


def find_users(users, day):
    result_list = []
    for name, birthday in users.items():
        if birthday.date() == day.date():
            result_list.append(name)

    return result_list


def congratulate(users):
    week_days = {1: 'Monday', 2: 'Tuesday',
                 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
    congratulate_list = {i: list() for i in range(1, 6)}

    today = datetime.now()
    today_isoweekday = today.isoweekday()
    monday_date = today - timedelta(days=today_isoweekday - 1)
    congratulate_list[1] = (find_users(users, monday_date))
    congratulate_list[1].extend(find_users(
        users, monday_date - timedelta(days=1)))
    congratulate_list[1].extend(find_users(
        users, monday_date - timedelta(days=2)))
    for d in range(2, 6):
        congratulate_list[d] = find_users(
            users, monday_date + timedelta(days=d - 1))

    for d, list_user in congratulate_list.items():
        if len(list_user) > 0:
            print(f'{week_days[d]}: ' + ", ".join(list_user))


if __name__ == '__main__':
    users = {'Anton': datetime(2021, 8, 21),
             'Alex': datetime(2021, 8, 15),
             'Vika': datetime(2021, 8, 22),
             'Dima': datetime(2021, 8, 23),
             'Olya': datetime(2021, 8, 24),
             'Maryna': datetime(2021, 8, 25),
             'Sasha': datetime(2021, 8, 23),
             'Serhey': datetime(2021, 8, 24),
             'Vanya': datetime(2021, 8, 22),
             'Vova': datetime(2021, 8, 27),
             'Roma': datetime(2021, 8, 28), }

congratulate(users)
