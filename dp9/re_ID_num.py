import re
import json
import datetime

# with open("area.json", "w+", encoding="utf-8") as js_f:
#     with open("area.txt", "r+", encoding='utf-8') as f:
#         for line in f.readlines():
#             js_f.write(line.replace("'", "\""))


def is_ID_num(number, check_code_list, id_code_list):
    with open("area.json", "r", encoding="utf-8") as js_f:
        area_dict = json.load(js_f)
    if len(number) != 18:
        return False, "Length Error"
    elif not re.match(r"^\d{17}(\d|X|x)$", number):
        return False, "Format Error"
    elif number[0:6] not in area_dict:
        return False, "Area Code Error"
    try:
        datetime.date(int(number[6:10]), int(number[10:12]), int(number[12:14]))
    except ValueError as ve:
        return False, f"Datetime Error: {ve}"
    if str(check_code_list[sum([a * int(b) for a, b in zip(id_code_list, number)]) %11]) != str(number.upper()[-1]):
        return False, "Check Code Error"
    return True, f"{area_dict[number[0:2]+'0000']}省 {area_dict[number[0:4]+'00']}市 {area_dict[number[0:6]]}"


if __name__ == '__main__':
    id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    your_ID_num = input("please input your ID num:")
    # print(is_ID_num("430721199911112515", check_code_list, id_code_list))
    print(is_ID_num(your_ID_num, check_code_list, id_code_list))