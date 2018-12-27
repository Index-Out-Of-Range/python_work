import json


def MainList():
    print("*" * 60, "\n")
    print("南开大学软件学院通讯录管理系统V0.01a".center(55), "\n")
    print("添加数据请按[a]".center(55, '-'))
    print("删除数据请按[d]".center(55))
    print("修改数据请按[m]".center(55))
    print("查询数据请按[s]".center(55))
    print("返回主菜单请按[q]".rjust(55))
    print("退出程序请输入[quit]".rjust(55))
    print("\n", "*" * 60)


def append_list():
    print("请输入你要添加的数据：")
    name = input("请输入姓名:").strip()
    qq = input("请输入QQ:").strip()
    phone = input("请输入电话:").strip()
    email = input("请输入邮箱:").strip()
    contact_list.append({"name": name,
                         "qq": qq,
                         "phone": phone,
                         "email": email})
    print("添加数据成功!结果如下:")
    show_list(name, qq, phone, email)


def modify_list():
    show_list(print_all=True)
    index = int(input("请输入你要修改的数据序号:"))
    modify_dict = contact_list[index-1]
    name = input("请输入要修改的姓名(按下回车跳过):")
    qq = input("请输入要修改的QQ(按下回车跳过):")
    phone = input("请输入要修改的电话(按下回车跳过):")
    email = input("请输入要修改的邮箱(按下回车跳过):")
    if name:
        modify_dict['name'] = name
    if qq:
        modify_dict['qq'] = qq
    if phone:
        modify_dict['phone'] = phone
    if email:
        modify_dict['email'] = email
    print("信息修改成功!结果如下:")
    show_list(name, qq, phone, email)


def show_list(name='', qq='', phone='', email='', print_all=False):
    print("{:~^60}".format("通讯录数据列表"))
    if not print_all:
        print("{:<15}{:<15}{:<15}{:<15}".
              format('name', 'qq', 'phone', 'email'))
        print("{:<15}{:<15}{:<15}{:<15}".
              format(name, qq, phone, email))
    else:
        print("{:<15}{:<15}{:<15}{:<15}{:<15}".
              format('index', 'name', 'qq', 'phone', 'email'))
        for item in contact_list:
            print("{:<15}{:<15}{:<15}{:<15}{:<15}".
                  format(int(contact_list.index(item)) + 1, item['name'],
                         item['qq'], item['phone'], item['email']))
    print("{:~^60}".format("End"))


if __name__ == "__main__":
    with open("output.json", "r") as f:
        try:
            contact_list = json.load(f)
        except:
            contact_list = []
    while True:
        MainList()
        command = input("请输入指令(按q返回主菜单, 输入quit退出程序):").lower()
        if command in ['a', 'd', 'm', 's', 'q', 'quit']:
            print("你选择的指令是[{}]".format(command.upper()))
            if command == 'a':
                append_list()
            elif command == 'd':
                show_list(print_all=True)
                index = int(input("请输入要删除的数据序号:"))
                del contact_list[index-1]
                print("删除数据成功!结果如下:")
                show_list(print_all=True)
            elif command == 'm':
                modify_list()
            elif command == 's':
                show_list(print_all=True)
            elif command == 'q':
                MainList()
                quit_flag = True
            elif command == 'quit':
                with open("output.json", "w") as f1:
                    f1.write("[\n")
                    for item in contact_list:
                        load_dict = json.dump(item, f1)
                        if contact_list.index(item) != len(contact_list) - 1:
                            f1.write(",\n")
                    f1.write("\n]")
                break
        else:
            print("请输入正确的指令！")
