from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(colleagues_list):

    birthdays_per_week = {'Monday' : [], 'Tuesday' : [], 'Wednesday' : [], 'Thursday' : [], 'Friday' : []}

    today = datetime.today().date()

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday', 'Monday']

    string_full = ''

    for colleague in colleagues_list:

        name = colleague["name"]

        birthday = colleague["birthday"].date()

        birthday_this_year = birthday.replace(year = datetime.today().year)

        if birthday_this_year < today:

            birthday_this_year = birthday_this_year.replace(year = datetime.today().year + 1)

        if (birthday_this_year - today).days < 7:

            birthdays_per_week[week[birthday_this_year.weekday()]].append(name)

    for day, names in birthdays_per_week.items():

        if names:

            string = day + ': '

            for name in names:

                string = string + name

                if names.index(name) < len(names) - 1:

                    string = string + ', '

                else:
                    
                    string_full = string_full + string + "\n"
    
    return print(string_full[:-1])


# get_birthdays_per_week([{"name": "Bill Gates", "birthday": datetime(1955, 12, 5)}, {"name": "Elon Musk", "birthday": datetime(1966, 12, 6)}, {"name": "Madonna", "birthday": datetime(1970, 12, 5)}, {"name": "Bill Murrey", "birthday": datetime(1970, 12, 3)}, {"name": "Jeff Frisker", "birthday": datetime(1970, 12, 2)}, {"name": "Elen Glister", "birthday": datetime(1970, 11, 2)}, {"name": "Viven Pfafer", "birthday": datetime(1970, 12, 25)}])