import json
import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, render_template, session, g, request, redirect , jsonify
from database import init_db
from auth import auth_routes
from order import order_routes   # <-- FIXED
from flask_session import Session
from flask import session
from functools import wraps




app = Flask(__name__)
app.secret_key = "abc123"
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

init_db(app)
auth_routes(app)
order_routes(app)

@app.route("/")
def home():
    return render_template("index.html")

# Categories Page
@app.route('/categories')
def categories():
    return render_template("categories.html")

# Category Foods Page
@app.route('/category-foods')
def category_foods():
    return render_template("category-foods.html")

# Contact Page
@app.route("/contact")
def contact():
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("contact.html")


# Food Search Page
@app.route('/food-search')
def food_search():
    return render_template("food-search.html")
# Foods Page
@app.route('/foods')
def foods():
    return render_template("foods.html")


# Order Page
@app.route('/order')
def order():
    return render_template("order.html")
@app.route("/account")
def account():
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("account.html")


@app.route("/order-history")
def order_history():
    if not session.get("user_id"):
        return redirect("/login")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM orders WHERE user_id=%s ORDER BY id DESC",
                   (session["user_id"],))
    orders = cursor.fetchall()

    return render_template("order_history.html", orders=orders)


@app.route("/report-problem", methods=["POST"])
def report_problem():
    if not session.get("user_id"):
        return redirect("/login")

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    subject = request.form["subject"]
    message = request.form["message"]

    cur = g.db.cursor()
    cur.execute("""
        INSERT INTO problems (user_id, name, email, phone, subject, message)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (session["user_id"], name, email, phone, subject, message))
    g.db.commit()
    cur.close()

    return render_template("problem_success.html")



app.run(debug=True)
