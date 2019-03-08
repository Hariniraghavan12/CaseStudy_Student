import HTML
class tableformation:
    def tables_html(self,r,monthname,i):
        htmlcode="<b>"+monthname[i]+"</b>"
        htmlcode+= HTML.table(r)
        return htmlcode
