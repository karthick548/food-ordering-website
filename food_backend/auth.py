from flask import request, render_template, redirect, session, g, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def auth_routes(app):

    # SIGNUP
    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")
            phone = request.form.get("phone")
            password = request.form.get("password")

            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

            cur = g.db.cursor()

            cur.execute("SELECT * FROM users WHERE email=%s", (email,))
            existing = cur.fetchone()

            if existing:
                return "Email already registered. Please login."

            cur.execute(
                "INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s)",
                (name, email, phone, hashed_password)
            )
            g.db.commit()
            cur.close()

            return render_template("signup_success.html")

        return render_template("signup.html")

    # LOGIN
    

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            cur = g.db.cursor()
            cur.execute("SELECT * FROM users WHERE email=%s", (email,))
            user = cur.fetchone()
            cur.close()

            # WRONG EMAIL
            if not user:
                flash("Wrong email or password", "error")
                return redirect("/login")

            # WRONG PASSWORD
            if not bcrypt.check_password_hash(user["password"], password):
                flash("Wrong email or password", "error")
                return redirect("/login")

            # SUCCESS LOGIN
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["user_email"] = user["email"]
            session["user_phone"] = user["phone"]

            return redirect("/")

        return render_template("login.html")

    # CHECK LOGIN (only one)
    @app.route("/check-login")
    def check_login():
        return {"logged_in": bool(session.get("user_id"))}

    # LOGOUT
    @app.route("/logout")
    def logout():
        session.clear()
        return redirect("/")
