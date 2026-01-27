from flask import request, jsonify, session, g
import json

def order_routes(app):

    @app.route("/place-order", methods=["POST"])
    def place_order():
        if not session.get("user_id"):
            return jsonify({"status": "not_logged_in"})

        data = request.json

        customer_name = data.get("customer_name")
        phone = data.get("phone")
        email = data.get("email")
        address = data.get("address")
        items = data.get("items")
        total = data.get("total")

        cur = g.db.cursor()
        cur.execute("""
            INSERT INTO orders 
            (user_id, customer_name, email, phone, address, items, total)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            session["user_id"],
            customer_name,
            email,
            phone,
            address,
            json.dumps(items),
            total
        ))

        g.db.commit()
        cur.close()

        return jsonify({"status": "success"})


    @app.route("/cancel-order/<int:order_id>", methods=["POST"])
    def cancel_order(order_id):
        if not session.get("user_id"):
            return {"status": "not_logged_in"}

        cur = g.db.cursor()
        cur.execute(
            "DELETE FROM orders WHERE id=%s AND user_id=%s",
            (order_id, session["user_id"])
        )
        g.db.commit()
        cur.close()

        return {"status": "success"}


        