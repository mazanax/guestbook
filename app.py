from os import getenv

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Update the DATABASE_URI to use PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL', 'postgresql://guestbook_user:yourpassword@localhost/guestbook_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)


# Create tables if they don’t exist
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        content = request.form.get("content")
        if name and content:
            new_message = Message(name=name, content=content)
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for("index"))
    messages = Message.query.all()
    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    app.run(debug=True)
