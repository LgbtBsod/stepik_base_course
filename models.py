from sqlalchemy.orm import mapper,relationship,sessionmaker
from sqlalchemy import MetaData, create_engine, Table


# Открываем базу данных 
engine = create_engine('sqlite:///univer.db')
meta = MetaData(engine)

staff = Table('Staff', meta, autoload=True)

student = Table('Student', meta, autoload=True)
  
fgroup = Table('Fgroup', meta, autoload=True)
    
faculty = Table('Faculty', meta, autoload=True)
    
exam = Table('Exam', meta, autoload=True)
    
exam_record = Table('Exam_record', meta, autoload=True)
    
hr_record = Table('HR_record',meta,autoload=True)


class Staff():
    def __init__(self, first_name,last_name,id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
    def __repr__(self) -> str:
        return f"Staff('{self.first_name}','{self.last_name}','{self.id}')"
    
  
class Student():
    def __init__(self,group_id, first_name,last_name,id):
        self.group_id = group_id
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
    def __repr__(self) -> str:
        return f"Student('{self.group_id}','{self.first_name}','{self.last_name}','{self.id}')"
    
class FGroup():
    def __init__(self, faculty_id,number,id):
        self.faculty_id = faculty_id
        self.number = number
        self.id = id
    def __repr__(self) -> str:
        return f"FGroup('{self.faculty_id}','{self.number}','{self.id}')"
     
class Faculty():
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __repr__(self) -> str:
        return f"Faculty('{self.name}','{self.id}')"
    
class Exam():
    def __init__(self, staff_id,discipline,id):
        self.staff_id = staff_id
        self.discipline = discipline
        self.id = id
    def __repr__(self) -> str:
        return f"Exam('{self.staff_id}','{self.discipline}','{self.id}')"
    
class Exam_record():
    def __init__(self, student_id,exam_id,grade,date):
        self.student_id = student_id
        self.exam_id = exam_id
        self.grade = grade
        self.date = date
    def __repr__(self) -> str:
        return f"Exam_record('{self.student_id}','{self.exam_id}','{self.grade}','{self.date}')"
    
class Hr_record():
    def __init__(self, staff_id,faculty_id,position):
        self.staff_id = staff_id
        self.faculty_id = faculty_id
        self.position = position
    def __repr__(self) -> str:
        return f"HR_record('{self.staff_id}','{self.faculty_id}','{self.position}')"

mapper(Staff,staff)
mapper(Student,student)
mapper(FGroup,fgroup)
mapper(Faculty,faculty)
mapper(Exam,exam)
mapper(Exam_record,exam_record)
mapper(Hr_record,hr_record)
