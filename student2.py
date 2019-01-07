# 练习
# １，用来描述一个学生信息student类
# 学生信息有　姓名　年龄　成绩　将存入列表中　可以任意添加和删除学生信息
# １，打印学生个数２，打印平均成绩，３打印平均年龄（建议用列表的长度计算学生个数）

class Student:
    infos = []
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.score=s


    @classmethod
    def input_student(cls):
        while True:
            n=input("姓名：")
            if not n:
                break
            a=int(input("年龄："))
            s=int(input("成绩："))
            cls.infos.append(Student(n,a,s))
    @classmethod   
    def del_student(cls):
        n = input("输入要删除学生的姓名：")
        for index,s in enumerate(cls.infos):
            if s.name == n:
                del cls.infos[index]
                return
    @classmethod
    def print_student_count(cls):
        '打印学生的个数'
        print(len(cls.infos))
    
    @classmethod
    def print_avg_score(cls):
        '打印平均成绩'
        # total_score=0
        # for s in cls.infos:
        #     total_score+=s.score
        total_score = sum((s.score for s in cls.infos))
        print("平均成绩是",total_score/len(cls.infos))
    @classmethod
    def output_student(cls):
        for s in cls.infos:
            print(s.name,s.age,s.score)

Student.input_student()
Student.output_student()
Student.del_student()
Student.output_student()
Student.print_student_count()
Student.print_avg_score()
