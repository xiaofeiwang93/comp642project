from flask import render_template

class CommonService:
    
    def  raise_error(e):
        print(e)
        return render_template("/commonview/error.html", error = str(e))