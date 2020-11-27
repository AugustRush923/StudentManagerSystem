from student import Student


class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self):
        name = input('请输入学员姓名: ')
        gender = input('请输入学员性别: ')
        tel = input('请输入学员联系方式: ')

        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(f'学员{student.name}添加成功')
        print('*' * 30)

    def del_student(self):
        name = input('请输入要删除学员姓名: ')
        for student in self.student_list:
            if student.name == name:
                print(f'学员{student.name}删除成功')
                self.student_list.remove(student)
                print('*' * 30)
                break
        else:
            print('查无此人')

    def update_student(self):
        name = input('请输入要更改信息的学员名字：')
        for student in self.student_list:
            if student.name == name:
                choice = int(input('需要更新什么信息？1.姓名,2.性别,3电话：'))
                if choice == 1:
                    student.name = input('请输入姓名：')
                elif choice == 2:
                    student.gender = input('请输入性别：')
                elif choice == 3:
                    student.tel = input('请输入电话:')
                print(f'学员{student.name}更新成功')
                print('*' * 30)
                break
        else:
            print('查无此人')

    def get_student_info(self):
        name = input('请输入要查询信息的学员名字：')
        for student in self.student_list:
            if student.name == name:
                print(f'学员{student.name}查询成功')
                print(student)
                print('*' * 30)
                break
        else:
            print('查无此人')

    def list_student_info(self):
        print('姓名\t性别\t联系方式')
        for student in self.student_list:
            print(f'{student.name}\t{student.gender}\t{student.tel}')

    def save_student_info(self):
        with open('student.txt', 'w+', encoding='utf-8') as f:
            # for student in self.student_list:
            #     f.write(student.name + ',' + student.gender + ',' + student.tel + '\n')

            new_list = [student.__dict__ for student in self.student_list]
            f.write(str(new_list))
        print('保存成功')
        print('*' * 30)

    def load_student(self):
        try:
            f = open('student.txt', 'r+', encoding='utf-8')
        except FileNotFoundError:
            pass
        else:
            # lines = f.readlines()
            # for line in lines:
            #     line = line.strip()
            #     line = line.split(',')
            #     student = Student(line[0], line[1], line[2])
            #     self.student_list.append(student)
            # print('载入成功')
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(student['name'], student['gender'], student['tel']) for student in new_list]
            f.close()

    @staticmethod
    def show_menu():
        print('欢迎进入xxx学员管理系统 v1.0')
        print('*' * 30)
        print('1. 增加学员信息')
        print('2. 删除学员信息')
        print('3. 更新学员信息')
        print('4. 获取指定学员信息')
        print('5. 展示所有学员信息')
        print('6. 保存学员信息')
        print('7. 打印帮助信息')
        print('8. 退出系统')
        print('*' * 30)

    def run(self):
        self.load_student()
        self.show_menu()
        while True:
            menu_num = int(input('请输入您需要的功能序号：'))

            if menu_num == 1:
                self.add_student()

            elif menu_num == 2:
                self.del_student()

            elif menu_num == 3:
                self.update_student()

            elif menu_num == 4:
                self.get_student_info()

            elif menu_num == 5:
                self.list_student_info()

            elif menu_num == 6:
                self.save_student_info()

            elif menu_num == 7:
                self.show_menu()

            elif menu_num == 8:
                break


if __name__ == '__main__':
    sm = StudentManager()
    sm.run()
