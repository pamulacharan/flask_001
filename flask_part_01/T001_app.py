
from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)


@app.route('/about')
def fun():
    return 'Charan'


@app.route('/contact')
def contact():
    return 'Hello charan this is Contact page'


@app.route('/switch/<pamula>')
def switch(pamula):
    if pamula == 'about':
        return redirect(url_for('fun'))
    if pamula == 'contact':
        return redirect(url_for('contact'))  # type: ignore


@app.route('/hello/<name>')
def raj(name):
    return 'Hello ' + name + ' this is Contact page'


@app.route('/hello/<int:name_01>')
def ramu(name_01):
    return 'THis page has %d subscribers' % name_01


def sonu():
    return 'hello venkat'


app.add_url_rule('/venkat', 'venkat', sonu)


def chandu():
    return 'hello chandu mahesh jithu raj'


app.add_url_rule('/harish', 'endpoint', chandu)


@app.route('/<rama>')
def seethe(rama):
    return render_template('about.html', name=rama)  # type: ignore


if  __name__ == '__main__':
    app.run(debug=True)
