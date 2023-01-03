import os
from flask import Flask, render_template, request, redirect, url_for, session
import crawler

from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(24)

pic_url_ls = []

@app.route('/')
def hello_world():  # put application's code here
    return render_template('test_bootstrap.html')


@app.route('/crawler/<int:page>', methods=['GET', 'POST'])
def flask_crawler(page=None):
    global pic_url_ls
    if request.method == 'POST':
        word = request.form.get("word")
        session["word"] = word
        pic_url_ls = crawler.crawler_more(key=word)
    else:
        word = session.get("word")

    pic_ls, pic_num = crawler.crawler_page(key=word, pages=page)
    return render_template('crawler.html', name=word, pic_ls=pic_ls, page=page, pic_num=pic_num, pic_url_ls=pic_url_ls)


if __name__ == '__main__':
    app.run()
