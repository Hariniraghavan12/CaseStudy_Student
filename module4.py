import HTML
import webbrowser
import sqlite3
class htmlpage:
    def htmlconnection(self,message):
        try:
            with open('hi.html','w') as f:
                f.write(message)
        except IOError:
            print("could not read file",f)
        try:
            with open('hi.html','r') as f:
                f.read()
                webbrowser.open_new_tab('hi.html')
        except IOError:
            print("Could not write into file",f)
        
