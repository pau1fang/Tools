import re
import os

filename = "students.txt"


def main():
    ctrl = True
    while ctrl:
        menu()
        option = input("请选择:")
        option_str = re.sub("\D", "", option)
        if option_str in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            option_num = int(option_str)
            if option_num == 0:
                print("already exit the system")
                ctrl = False
            elif option_num == 1:
                insert()
            elif option_num == 2:
                search()
            elif option_num == 3:
                delete()
            elif option_num == 4:
                modify()
            elif option_num == 5:
                sort()
            elif option_num == 6:
                total()
            elif option_num == 7:
                show()


def menu():
    print("""
    ———————————————————system——————————————————
    |                                         |
    | ===============function menu ===========|
    |                                         |
    |   1.录入学生信息                          |
    |   2.查找学生信息                          |
    |   3.删除学生信息                          |
    |   4.修改学生信息                          |
    |   5.排序                                 |
    |   6.统计学生总人数                        |
    |   7.显示所有学生信息                       |
    |   0. 退出系统                            |
    |  =====================================  |
    |  说明：通过数字或↑↓方向键选择菜单            |
    ————————————————————————————————————————————
    """)


def save(student):
    try:
        student_txt = open(filename, "a")
    except Exception as e:
        student_txt = open(filename, "w")
    for info in student:
        student_txt.write(str(info) + "\n")
    student_txt.close()


def insert():
    message = []
    mark = True
    while mark:
        id_ = input("请输入ID(如001):")
        if not id_:
            break
        name = input("请输入名字：")
        if not name:
            break
        try:
            math = int(input("please input math score:"))
            english = int(input("please input english score:"))
            biology = int(input("please input biology score:"))
        except:
            print("input wrong or not int...please input again!")
            continue
        student = {"id":id,
                   "name":name,
                   "math":math,
                   "english":english,
                   "biology":biology}
        message.append(student)
        input_mark = input("continue? (y/n):")
        if input_mark == "y":
            mark = True
        else:
            mark = False
    save(message)
    print("students message already add in file!!!")


def search():
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按ID查输入1；按姓名查输入2：")
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(filename, "r") as file:
                student = file.readlines()
                for List in student:
                    d = dict(eval(List))
                    if id is not "":
                        if d["id"] == id:
                            student_query.append(d)
                    elif name is not "":
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询？(y/n):")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息...")
            return


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


def show_student(student_list):
    if not student_list:
        print("无数据信息\n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "name", "math score", "english score", "biology score", "total score"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in student_list:
        print(format_data.format(info.get("id"),
                                 info.get("name"),
                                 str(info.get("math")),
                                 str(info.get("english")),
                                 str(info.get("biology")),
                                 str(info.get("math") + info.get("english") + info.get("biology")).center(12)))


if __name__ == '__main__':
    main()
