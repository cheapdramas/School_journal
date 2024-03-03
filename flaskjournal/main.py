from datetime import datetime,date
from flask import Flask,session,request,redirect,url_for,render_template,request
from db_scripts import get_log_pass,get_schedule,prepare_student_info,add_mark,get_marks,get_markndate
import os

PATH = os.path.dirname(__file__) + os.sep
PATH_STATIC = PATH + 'static' + os.sep
app = Flask(__name__)

@app.route('/students_log')
def students_log():
    return get_log_pass()


@app.route('/schedule')
def schedule():
    return get_schedule()



def mark_fill_page():
    all_subjects = ['Алгебра','Англійська мова','Біологія','Географія','Геометрія','Зарубіжна література','Інформатика','Історія України','Мистецтво',"Основи здоров'я",'Правознавство','Трудове навчання','Українська література','Українська мова','Фізика','Фізична культура','Хімія']

    if request.method == 'GET':
        
        list_remake= []
        list_info= prepare_student_info()   
        for info in list_info:

            list_remake.append((info[0],info[1] + ' '+info[2]))

        marks_listt = [x+1 for x in range(12)]
        


        
        return render_template('add_mark.html',student_list = list_remake,subj_list = all_subjects,marks_list=marks_listt)
    if request.method == 'POST':
        student_id = request.form.get('student')
        subject = request.form.get('subject')
        mark = request.form.get('mark')
        reason = request.form.get('reason')
        date_ = date.today()
        time = str(datetime.now()).split(' ')[1].split('.')[0].split(':')[0]+':'+ str(datetime.now()).split(' ')[1].split('.')[0].split(':')[1]

        


        subject = all_subjects[int(subject)]
        
    
        add_mark(student_id,subject,mark,reason,date_,time)
            

        return redirect(url_for('add_mark'))
    



def get_marks_url():
    url = request.url

    a =url.split('/')
    id = int(a[-1])
    return get_marks(id)
    

def get_news_page():
    url = request.url

    a =url.split('/')
    id = int(a[-1])
    

    return get_markndate(id)
    
    


app.add_url_rule('/add_mark','add_mark',mark_fill_page,methods = ['post','get'])

for i in range(get_log_pass()[-1][0]):
    i = i+1
    app.add_url_rule(f'/get_marks/{i}',f'get_marks{i}',get_marks_url,methods = ['post','get'])

for i in range(get_log_pass()[-1][0]):
    i = i+1
    app.add_url_rule(f'/get_news/{i}',f'get_news{i}',get_news_page,methods = ['post','get'])


#pythonanywere запустити хост
if __name__ == '__main__':
    app.run()