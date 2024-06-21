from backend import app


if __name__ == '__main__':
    app.run(debug=True)

# to create tables in database run these code:
# from backend import db
# from backend import app
# app.app_context().push()
# db.create_all()