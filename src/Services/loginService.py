from functools import wraps
import os
from flask import Flask, flash, redirect, request, session, url_for
from flask import render_template

from Services.commonService import raise_error

# Login page endpoint
def login():
    return render_template('Common/login_view.html')
    # try:
    #     return render_template('Common/login_view.html')
    # except Exception as e:
    #     return raise_error(e)    