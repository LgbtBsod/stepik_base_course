from sqlalchemy import create_engine,select,Table,Column, Integer,String,MetaData,ForeignKey,Date

meta = MetaData()

staff = Table('Staff', meta, Column('first_name', String(250), nullable=False), Column('last_name', String(250), nullable=False), Column('id', Integer, primary_key=True))

student = Table('Student', meta, Column('group_id', Integer, ForeignKey('Fgroup.id')), Column('first_name', String(250), nullable=False), Column('last_name', String(250), nullable=False), Column('id', Integer, primary_key=True))
  
fgroup = Table('Fgroup', meta, Column('faculty_id', Integer, ForeignKey('Faculty.id')),Column('number', Integer, primary_key=True), Column('id', Integer, primary_key=True))
    
faculty = Table('Faculty', meta, Column('name', String(250), nullable=False), Column('id', Integer, primary_key=True))
    
exam = Table('Exam', meta, Column('staff_id', Integer, ForeignKey('Staff.id')), Column('discipline',String(250), nullable=False),Column('id', Integer, primary_key=True))
    
exam_record = Table('Exam_record', meta, Column('student_id',Integer, ForeignKey('Student.id')), Column('exam_id', Integer, ForeignKey('Exam.id')), Column('grade', String(250), nullable=False), Column('date', Date, nullable=False), Column('id', Integer, primary_key=True))
    
hr_record = Table('HR_record', meta, Column('staff_id', Integer, ForeignKey('Staff.id')),Column('faculty_id', Integer, ForeignKey('Faculty.id')), Column('position',String(250), nullable=False), Column('id', Integer, primary_key=True))


engine = create_engine('sqlite:///univer.db',echo = True)
meta.create_all(engine)


