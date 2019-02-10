from flask import Flask, render_template, redirect, url_for, request,jsonify
import pandas as pd
app = Flask(__name__)

from io import StringIO
import json


import cx_Oracle

@app.route('/data')
def data():
    dsn_tns = cx_Oracle.makedsn('localhost', 49161, 'xe')
    db = cx_Oracle.connect('system', 'oracle', dsn_tns)
    df = pd.read_sql('select * from dwh_module_summary order by 1,2', db)
    df1={}
    df1['records']=json.loads(df.to_json(orient='records'))
    df1['length']=len(df.index)
    return json.dumps(df1)

    # df=data.groupby(['REGION','COUNTRY','SLA'])['ABEND','RECOVERD','DWH','ORP','GENISIS','CARDS','BANK'].sum()
    #return json.load(data.to_json(orient='records'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('Dashboard'))
    return render_template('login.html', error=error)


@app.route('/Dashboard')
def Dashboard():
    return render_template('layout.html')

@app.route('/<page>')
def childPages(page):
    print('pagename is :',page)
    return render_template(page)


@app.route('/data1')
def data1():
    import cx_Oracle
    from flask import request, jsonify
    import pandas as pd

    dsn_tns = cx_Oracle.makedsn('localhost', 49161, 'xe')
    db = cx_Oracle.connect('system', 'oracle', dsn_tns)
    data = pd.read_sql('select * from dwh_module_summary', db)
    df = data.groupby(['REGION', 'COUNTRY', 'SLA'])['ABEND', 'RECOVERD', 'DWH', 'ORP', 'GENISIS', 'CARDS', 'BANK'].sum()

    def color_negative_red(val):
        """
        Takes a scalar and returns a string with
        the css property `'color: red'` for negative
        strings, black otherwise.
        """
        color = 'red' if val > 100 else 'black'
        return 'color: %s' % color

    s = df.style.applymap(color_negative_red)
    return s.render().replace('\n', '')

if __name__ == '__main__':
   app.run(debug = True)
