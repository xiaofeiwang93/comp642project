from flask import render_template

class CommonService:

    def home():
        try:
            return True
        except Exception as e:
            print(e)
            return raise_error(e)
        
    def movieList():
        try:
            return True
        except Exception as e:
            print(e)
            return raise_error(e)

    def movieDetail():
        try:
            return True
        except Exception as e:
            print(e)
            return raise_error(e)

    def  raise_error(e):
        print(e)
        return render_template("/commonview/error.html", error = str(e))