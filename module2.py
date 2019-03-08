import sqlite3
from module1 import dic
class dbconnection:
    def connection(self,monthname):
        db = sqlite3.connect("htmltable.db") 
        cursor = db.cursor()
        q="select sid,sname,exam_date,tamil,english ,maths ,science ,social ,Total ,Result from(SELECT s.sid,s.sname,m.exam_date,m.maths ,m.english ,m.science  ,m.social ,m.tamil ,case when m.maths>=50 and m.english>=50 and m.science>=50 and m.tamil>=50 and m.social>=50 then 'PASS' else 'FAIL' end as Result,(m.maths + m.english + m.science +m.social +m.tamil) AS Total FROM student s join marks m on m.sid=s.sid where m.exam_date like "+str(dic[monthname])+") as Result_set where Result_set.Result='PASS';"
        cursor.execute(q)
        head=[i[0] for i in cursor.description]
        try:
            res=cursor.fetchall()
        except Exception as e:
            print(e)
        res.insert(0,head)
        return res
        db.close()

