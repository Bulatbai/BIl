from flask import Flask, render_template, request
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
 return render_template("index.html")



@app.route('/database/')
def rou():
    f = open('good.txt', 'r+', encoding='utf-8')
    text = f.readlines()
    f.close()
    return render_template("database.html", text=text)

@app.route('/add/')
def method_name():
    return render_template("Gro.html")



@app.route('/add/', methods=["POST"])
def add():
    key = request.form["text"]
    f = open('good.txt', 'a+', encoding='utf-8')
    f.write(key + "\n")
    f.close()
    return  "Зарегистрировано"



if __name__ == "__main__":
    app.run(debug=True)


