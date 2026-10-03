from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "utsav.db"

EVENTS = [
    "Dance Battle",
    "Battle of Bands",
    "Code Quest",
    "Art Attack",
    "Photography Challenge",
    "Fun Games"
]


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            event TEXT NOT NULL,
            registered_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/registration")
def registration():
    return render_template("registration.html", events=EVENTS)


@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    event = request.form.get("event", "").strip()

    if not name or not email or not phone or not event:
        return render_template(
            "registration.html",
            events=EVENTS,
            error="Please fill all fields."
        )

    if event not in EVENTS:
        return render_template(
            "registration.html",
            events=EVENTS,
            error="Please select a valid event."
        )

    conn = get_db()

    cursor = conn.execute("""
        INSERT INTO registrations
        (name, email, phone, event, registered_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        email,
        phone,
        event,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    registration_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return render_template(
        "registration.html",
        events=EVENTS,
        success=f"Registration successful! Your Registration ID is #{registration_id}"
    )


@app.route("/registrations")
def registrations():

    conn = get_db()

    data = conn.execute("""
        SELECT * FROM registrations
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    return render_template(
        "registrations.html",
        registrations=data
    )


@app.route("/delete/<int:id>", methods=["POST"])
def delete_registration(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM registrations WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("registrations"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)