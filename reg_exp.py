from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
def fix_the_phonebook():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    for value in contacts_list:
        phones_raw = r"(\+7|8)[\s-]*\(*(\d{3})\)*[ -]*(\d*)[ -]*(\d*)[ -]*(\d*)([ -]\(*(\w+.)\s*(\d+)\)*)*"
        phones_fixed = r"+7(\2)\3\4\5 \7\8"
        value[5] = re.sub(phones_raw, phones_fixed, value[5]).strip()
        if ' ' in value[0]:
            splitted_name = value[0].split()
            if len(splitted_name) == 2:
                value[1] = ''.join(splitted_name[1])
            else:
                value[1] = ''.join(splitted_name[1])
                value[2] = ''.join(splitted_name[2])
            value[0] = ''.join(splitted_name[0])
        if ' ' in value[1]:
            splitted_surname = value[1].split()
            value[1] = ''.join(splitted_surname[0])
            value[2] = ''.join(splitted_surname[1])
    contacts_dict = {}
    for value in contacts_list:
        if (value[0], value[1],) not in contacts_dict.keys():
            contacts_dict[(value[0], value[1],)] = value[2:]
        else:
            contacts_dict[(value[0], value[1],)] += [value[2:]]
    for index in list(contacts_dict.values()):
        if type(index[-1]) is list:
            for number, value in enumerate(index):
                if value == "":
                    index[number] = index[-1][number]
            index = index.pop(-1)
    naming_list = [list(index) for index in contacts_dict.keys()]
    info_list = [index for index in contacts_dict.values()]
    formated_list = [naming_list[index] + info_list[index] for index in range(len(naming_list))]
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
    ## Вместо contacts_list подставьте свой список:
        datawriter.writerows(formated_list)

if __name__ == "__main__":
    fix_the_phonebook()