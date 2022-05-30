# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/poul/')
# def rou():
#     f = open('good.txt', 'r+', encoding='utf-8')
#     text = f.readlines()
#     f.close()
#     return render_template("database.html", text=text)


# @app.route('/add/', methods=["POST"])
# def add():
#     key = request.form["text"]
#     f = open('good.txt', 'a+', encoding='utf-8')
#     f.write(key + "\n")
#     f.close()
#     return  render_template("database.html")


# # {% block body %}
# # {% for tex in text %}
# # <li>{{ tex }}</li>
# # {% endfor %}

# # {% block body %}
# # {% for tet in text %}
# # <li>{{ tet }}</li>
# # {% endfor %}