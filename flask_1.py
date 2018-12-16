
from flask import Flask, render_template, request
import requests
import csv

app = Flask(__name__)



def geocode(news)->str:
    with open('records_a.csv') as data:
        for x in data:
            b = str(news)
            c = str(x[0:9])
            if b == c:
                return str(x) 

def geocode1(names):
    with open('records_a.csv') as data:
        for x in data:
            c = str(x[12:15].strip(','))
            b = str(names)
            if b == c:
                return str(x)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    news = request.form['news']
    if news != "":
        news = request.form['news']
        title = '这是查询结果:'
        results = geocode(news)
        return render_template('results.html',
                               the_title=title,
                               the_news=news,
                               the_results=results,)
    else:
        names = request.form['names']
        title = '这是查询结果:'
        results = geocode1(names)
        return render_template('results.html',
                               the_title=title,
                               the_news=names,
                               the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎使用上午班python查询网站')


if __name__ == '__main__':
    app.run(debug=True)
