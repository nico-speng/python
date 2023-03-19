import os
import json

filename = 'student.txt'

# 定义菜单栏提示
def menm():
    print('====================学生信息管理系统========================')
    print('-----------------------功能菜单----------------------------')
    print('\t\t1.录入学生信息')
    print('\t\t2.查找学生信息')
    print('\t\t3.删除学生信息')
    print('\t\t4.修改学生信息')
    print('\t\t5.排序')
    print('\t\t6.统计学生总人数')
    print('\t\t7.显示所有学生信息')
    print('\t\t0.退出')

def main():
    while True:
        menm()
        choice = int(input('请选择'))
        if choice in {0, 1, 2, 3, 4, 5, 6, 7}:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer in ['y','Y']:
                    print('谢谢您的使用！！！')
                    break
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                update()
            elif choice == 5:
                student_sorted()
            elif choice == 6:
                total()
            elif choice == 7:
                all_show()

def show():
    if not os.path.exists(filename):
        print('文件不存在！')
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]    

def insert():
    student_list = []
    while True:
        id = input('请输入学生ID(如1001):')
        if not id:
            break

        name = input('请输入姓名')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩'))
            python = int(input('请输入python成绩'))
            java = int(input('请输入java成绩'))

        except Exception:
            print('输入无效，不是整数类型，请重新输入')
            continue

        # 将录入的学生信息保存到字典内
        student = {'id':id,'name':name,'english':english,'python':python,'java':java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加?y/n\n')
        if answer in ['y','Y']:
            continue
        else:
            break
    
    # 调用save()类方法
    save(student_list)
    print('学生信息录入完毕!!!')

def save(list):
    try:
        # 如果文件存在就追加写入
        stu_txt = open(filename,'a',encoding='utf-8')
    except Exception:
        # 如果没有就写入
        stu_txt = open(filename,'w',encoding='utf-8')
    for item in list:
        stu_txt.write(json.dumps(item)+'\n')
    # 关闭缓存
    stu_txt.close()

def search():
    # 获取所有学员的数据
    student_list = show()
    if not student_list:
        print("学员列表为空，无法搜索！")
        return
    # 输入学员的ID
    student_id = input('请输入查找的学员ID：')
    found = False
    for student in student_list:        
        if student_id == student['id']:
            print(student)
            found = True
            break        

    if not found:
        print('没有该学员存在！！！')

def delete():
    while True:
        if student_id := input('请输入要删除的学生的ID:'):
            student_old = []

            if os.path.exists(filename):
                with open(filename, 'r+', encoding='utf-8') as file:
                    student_old = file.readlines()
                    file.seek(0)  # 将文件指针移动到文件开头
                    for item in student_old:
                        if student_id not in item:
                            file.write(item)
                    file.truncate()  # 截断文件，删除多余的内容
            if not student_old:
                print('无学生信息')
                break
            else:
                print(f'id为{student_id}的学生信息已被删除')
        else:
            print('无学生信息')
            break
        show()
        answer = input('是否继续删除？y/n\n')
        if answer.lower() != 'y':
            break
            
def update():
    if not os.path.exists(filename):
        print('文件不存在！')
        return

    student_id = input('请输入修改的学员ID：')

    with open(filename, 'r', encoding='utf-8') as f:
        student_list = [json.loads(line) for line in f]

    for i, student in enumerate(student_list):
        if student['id'] == student_id:
            print(student)
            print('找到学生信息，可以修改他的相关信息了！')
            while True:
                try:
                    student['name'] = input('请输入姓名：')
                    student['english'] = int(input('请输入英语成绩：'))
                    student['python'] = int(input('请输入python成绩：'))
                    student['java'] = int(input('请输入java成绩：'))
                except ValueError:
                    print('您的输入有误，请重新输入！')
                else:
                    break

            student_list[i] = student
            with open(filename, 'w', encoding='utf-8') as f:
                for s in student_list:
                    f.write(json.dumps(s) + '\n')

            print('修改成功！')
            break
    else:
        print('未找到该学员信息！')

    answer = input('是否继续修改学生信息？(y/n)\n')
    if answer.lower() == 'y':
        update()

# 定义排序规则函数
def student_sorted():
    
    key = input('请输入排序字段：')

    student_list = show()
    # 定义排序规则函数
    key_func = lambda student_list: student_list[key]

    # 对学生列表按照Java成绩进行排序
    sorted_students = sorted(student_list, key=key_func, reverse=True)

    # 输出排序结果
    for student in sorted_students:
        print(f"学号：{student['id']}，姓名：{student['name']}，java成绩：{student['java']}，python成绩：{student['python']}，英语成绩：{student['english']}")

def total():
    student_list = show()
    print(f'学生的总人数为：{len(student_list)}人')

def all_show():
    student_list = show()
    print(student_list)
    

if __name__=='__main__':
    main()