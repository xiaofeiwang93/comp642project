from flask import render_template

def home():
    try:
        return render_template('home.html')
    except Exception as e:
        print(e)
        return raise_error(e)

def  raise_error(e):
    print(e)
    return render_template("/commonview/error.html", error = str(e))