import pymysql
from flask import g

def init_db(app):
    app.config['DB_HOST'] = 'localhost'
    app.config['DB_USER'] = 'root'
    app.config['DB_PASSWORD'] = 'raeva1511'
    app.config['DB_NAME'] = 'food_delivery'

    @app.before_request
    def connect_db():
        if 'db' not in g:
            g.db = pymysql.connect(
                host=app.config['DB_HOST'],
                user=app.config['DB_USER'],
                password=app.config['DB_PASSWORD'],
                database=app.config['DB_NAME'],
                cursorclass=pymysql.cursors.DictCursor
            )

    @app.teardown_request
    def close_db(error=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    return app
