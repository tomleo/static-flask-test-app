import sys

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
app.config.update(
    FREEZER_RELATIVE_URLS=True,
    FREEZER_IGNORE_MIMETYPE_WARNINGS=True
)
freezer = Freezer(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/test/')
def test():
    return render_template('test.html')

@app.route('/wwf/')
def wwf():
    return render_template('wwf.html')
 
if __name__ == '__main__':
    try:
        sys.argv[1]
    except IndexError:
        app.run(debug=True)
    else:
        freezer.freeze()
