import module2 as m2
import module3 as m3
import module4 as m4
monthname=[
        'JAN',
        'FEB',
        'MAR',
        'APR',
        'MAY',
        'JUN',
        'JUY',
        'AUG',
        'SEP',
        'OCT',
        'NOV',
        'DEC',
        ]
dic={
        "JAN":"'%-01-%'",
        "FEB":"'%-02-%'",
        "MAR":"'%-03-%'",
        "APR":"'%-04-%'",
        "MAY":"'%-05-%'",
        "JUN":"'%-06-%'",
        "JUY":"'%-07-%'",
        "AUG":"'%-08-%'",
        "SEP":"'%-09-%'",
        "OCT":"'%-10-%'",
        "NOV":"'%-11-%'",
        "DEC":"'%-12-%'",
        }
if __name__ == '__main__':
    output=[]
    obj2=m2.dbconnection()
    obj4=m4.htmlpage()
    obj3=m3.tableformation()
    for i in monthname:
         output.append(obj2.connection(i))

    html_code=''
    count=-1
    for j in output:
        count=count+1
        html_code+=obj3.tables_html(j,monthname,count)
    
    obj4.htmlconnection(html_code)
        
         
