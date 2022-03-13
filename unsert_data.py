import sqlite3
import sqlalchemy

try:
    conn = sqlite3.connect('univer.db')
    cursor = conn.cursor()
    print("База данных создана и успешно подключена к SQLite")
    
    cursor.execute("INSERT INTO Faculty(id,name) VALUES (1,'Faculty of Arts');")
    cursor.execute("INSERT INTO Faculty(id,name) VALUES (2,'Faculty of Applied Mathematics');")
    
    cursor.execute("INSERT INTO FGroup(id,faculty_id,number) VALUES (1,1,0);")
    cursor.execute("INSERT INTO FGroup(id,faculty_id,number) VALUES (2,1,0);")
    cursor.execute("INSERT INTO FGroup(id,faculty_id,number) VALUES (3,2,0);")

    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) VALUES (1,'Roman','Ivanov',1);")
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) VALUES (2,'Aleksey','Kuznetsov',1);")
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) VALUES (3,'Olga','Naumova',1);")
    
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) values (4,'Irina','Filippenko',2);")
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) values (5,'Alexandr','Galkin',2);")
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) values (6,'Petr','Kutepov',2);")
    
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) values (7,'Sergey','Ivaschenko',3);")
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) values (8,'Oleg','Alekseev',3);")
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) values (9,'Vladimir','Kupriyanov',3);")
    cursor.execute("INSERT INTO Student(id,first_name,last_name,group_id) values (10,'Evgeniya','Nesmelova',3);")
    
    cursor.execute("INSERT INTO Staff(id,first_name,last_name) values (1,'Semen','Vasilenko');")
    cursor.execute("INSERT INTO Staff(id,first_name,last_name) values (2,'Nadezhda','Gavrilova');")
    cursor.execute("INSERT INTO Staff(id,first_name,last_name) values (3,'Igor','Makarov');")
    
    cursor.execute("INSERT INTO HR_record(staff_id,faculty_id,position) values (1,1,'professor');")
    cursor.execute("INSERT INTO HR_record(staff_id,faculty_id,position) values (2,2,'professor');")
    cursor.execute("INSERT INTO HR_record(staff_id,faculty_id,position) values (3,2,'docent');")
    
    cursor.execute("INSERT INTO Exam(id,discipline,staff_id) values (1,'History of Arts',1);")
    cursor.execute("INSERT INTO Exam(id,discipline,staff_id) values (2,'Programming',2);")
    cursor.execute("INSERT INTO Exam(id,discipline,staff_id) values (3,'Math',3);")

    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(1,1,4,'2020-01-15');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(2,1,5,'2020-01-15');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(4,2,3,'2020-01-10');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(5,2,4,'2020-01-10');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(6,2,3,'2020-01-10');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(6,3,5,'2020-01-05');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(8,3,5,'2020-01-05');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(9,3,4,'2020-01-05');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(10,2,4,'2020-01-10');")
    cursor.execute("INSERT INTO Exam_record(student_id,exam_id,grade,date) values(10,3,5,'2020-01-05');")        
    conn.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")