import sqlite3
import json


conn = None

curs = None
all_tables = ['History_marks','Algebra_marks','Biology_marks','Chemestry_marks','students_log','schedule','marks']
all_subjects= ['History','Algebra','Biology','Chemestry']
working_days = ['Понеділок','Вівторок','Середа','Четвер',"П'ятниця"]

monday_schedule = ['Українська література', 'Алгебра', 'Зарубіжна література', 'Хімія', 'Мистецтво', 'Географія', 'Історія']
tuesday_schedule= ['Українська мова', 'Зарубіжна література', 'Трудове навчання', 'Англійська мова', 'Фізкультура', 'Правознавство',None]
wednesday_schedule = ['Інформатика', 'Інформатика', 'Геометрія', 'Хімія', 'Історія', 'Фізика', 'Виховна година']
thursday_schedule = ['Українська література', 'Алгебра', 'Біологія', 'Англійська мова', 'Фізкультура', 'Фізика', 'Історія']
friday_schedule = ['Фізика', 'Українська мова', 'Геометрія', 'Англійська', 'Біологія', 'Фізкультура', 'Основи здоров’я']

schedule = [monday_schedule,tuesday_schedule,wednesday_schedule,thursday_schedule,friday_schedule]



def open_db():
    global conn,curs
    conn = sqlite3.connect('info.db')
    curs = conn.cursor()

def close():
    curs.close()
    conn.close()

def do(request):
    open_db()   
    curs.execute(request)
    conn.commit()

def clear():
    global all_tables
    open_db()
    for i in all_tables:
        do(f'DROP TABLE IF EXISTS {i}')


    close()


def structure_create():
    do("""CREATE TABLE IF NOT EXISTS students_log(
        id INTEGER PRIMARY KEY,
        name TEXT,
        second_name TEXT,
        login TEXT,
        password TEXT)""")
    
    do("""CREATE TABLE IF NOT EXISTS marks(
       student_id INTEGER,
       subject TEXT,
       mark INTEGER,
       reason TEXT,
       date DATE,
       time TEXT

    )""")
        
    

    do('''CREATE TABLE IF NOT EXISTS schedule(
       id INTEGER PRIMARY KEY,
       day TEXT,
       lesson_1 TEXT,
       lesson_2 TEXT,
       lesson_3 TEXT,
       lesson_4 TEXT,
       lesson_5 TEXT,
       lesson_6 TEXT,
       lesson_7 TEXT
    )''')
    


    

    

def add_log_pass(name,second_name,login,password):
    open_db()
    
    curs.execute("""INSERT INTO students_log(
                name,second_name,login,password) VALUES (?,?,?,?)""",[name,second_name,login,password])
    conn.commit()
    close()

def correcting_id_order():
    open_db()
    do("""SELECT name,second_name,login,password FROM students_log ORDER BY second_name""")

    info_by = curs.fetchall()
    
    do('DROP TABLE IF EXISTS students_log')
    conn.commit()
    
    do("""CREATE TABLE IF NOT EXISTS students_log(
        id INTEGER PRIMARY KEY,
        name TEXT,
        second_name TEXT,
        login TEXT,
        password TEXT)""")
    

    curs.executemany("""INSERT INTO students_log(name,second_name,login,password) VALUES(?,?,?,?)""",info_by)


    conn.commit()

def add_mark(id,subj,mark,reason,date,time):
    open_db()
    curs.execute('INSERT INTO marks(student_id,subject,mark,reason,date,time) VALUES(?,?,?,?,?,?)',[id,subj,mark,reason,date,time])
    conn.commit()
    close()
    
def get_marks(user_id):
    open_db()

    curs.execute(f'SELECT subject,mark FROM marks WHERE student_id == {user_id}')

    return curs.fetchall()

def get_markndate(user_id):
    open_db()

    # current_time = str(datetime.now()).split(' ')[0].split('-')[-1]
    # for i in time_marks:
       
    #     if int(i[0].split('-')[-1])- int(current_time) == 0:
    #         time_marks[time_marks.index(i)] = 'Сьогодні'
    #     if int(i[0].split('-')[-1])- int(current_time) == 1:
    #         time_marks[time_marks.index(i)] = 'Вчора'
    #     elif int(i[0].split('-')[-1])- int(current_time) > 1:
    #         time_marks[time_marks.index(i)] = str(int(i[0].split('-')[-1])- int(current_time)) + 'д'
        
    

    curs.execute(f'SELECT subject,mark,reason,date,time FROM marks WHERE student_id == {user_id}')
    
    

    return curs.fetchall()



            

    


def schedule_fill():
    global working_days

    
    for i in schedule:  
        curs.executemany('INSERT INTO schedule(lesson_1,lesson_2,lesson_3,lesson_4,lesson_5,lesson_6,lesson_7) VALUES(?,?,?,?,?,?,?)',[i])
    id = curs.execute('SELECT id FROM schedule')
    id = curs.fetchall()
    for i in id:
        i = i[0]
        day = working_days[int(i)-1]
        curs.execute(f'UPDATE schedule SET day = ? WHERE id = ?',[day,i])
    conn.commit()
    

def get_schedule():
    open_db()
    info = curs.execute("SELECT day,lesson_1,lesson_2,lesson_3,lesson_4,lesson_5,lesson_6,lesson_7 FROM schedule")
    
    return info.fetchall()
    
    


    

def get_log_pass():
    open_db()
    curs.execute('SELECT id,login,password FROM students_log')

    return curs.fetchall()    

def prepare_student_info():
    do('SELECT id,name,second_name FROM students_log')
    res = curs.fetchall()

    return res




def main():
    clear()

    structure_create()
    
    add_log_pass('Дарина','Матвієнко','matviy69','666jesus')
    add_log_pass('Альона','Гринчук','alona','roblox123')
    add_log_pass('Даня','Брожин','danya3','445566s')
    add_log_pass('Софія','Вдовцова','sofavdov','ez12')
    add_log_pass('Ростислав','Білецький','bileckij_123','654321re')
    add_log_pass('Давід','Адамян','david','123456xd')
    add_log_pass('Влад','Витюк','messi','ronaldo')
    add_log_pass('Софія','Дуднік','kick','kickmeplease')
    
    
    
   

    correcting_id_order()
    schedule_fill()
    
    

if __name__ == "__main__":
    main()
    