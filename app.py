
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/user/<string:name>/<int:id>')
def tst(name, id):
    return "User_page:" + name + "-" + str(id)


@app.route('/post/')
def test():
    return render_template("boot.html")

@app.route('/')
@app.route('/Home')
def index():
    f = open('good.txt', 'r+', encoding='utf-8')
    text = f.readlines()
    return render_template("index.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)




 # app.run(host='0.0.0.0')
