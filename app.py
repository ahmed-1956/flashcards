import sqlite3
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
def get_db_connection():
    connection = sqlite3.connect("flashcards.db")
    connection.row_factory = sqlite3.Row
    return connection
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/add", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        question = request.form.get("question", "").strip()
        answer = request.form.get("answer", "").strip()
        category = request.form.get("category", "").strip()
        if question and answer and category:
            connection = get_db_connection()
            connection.execute(
                """
                INSERT INTO cards (question, answer, category)
                VALUES (?, ?, ?)
                """,
                (question, answer, category)
            )
            connection.commit()
            connection.close()
            return redirect("/cards")
    return render_template("add.html")


@app.route("/edit/<int:card_id>", methods=["GET", "POST"])
def edit_card(card_id):
    connection = get_db_connection()

    card = connection.execute(
                        "SELECT * FROM cards WHERE id = ?",
                                (card_id,)
    ).fetchone()

    if card is None:
        connection.close()
        return "Card not found", 404

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        answer = request.form.get("answer", "").strip()
        category = request.form.get("category", "").strip()

        if question and answer and category:
            connection.execute(
                """
                UPDATE cards
                SET question = ?, answer = ?, category = ?
                WHERE id = ?
                """,
                (question, answer, category, card_id)
            )

            connection.commit()
            connection.close()

            return redirect("/cards")

    connection.close()

    return render_template("edit.html", card=card)


@app.route("/delete/<int:card_id>", methods=["POST"])
def delete_card(card_id):
    connection = get_db_connection()

    connection.execute(
        "DELETE FROM cards WHERE id = ?",
        (card_id,)
    )

    connection.commit()
    connection.close()

    return redirect("/cards")



@app.route("/cards")
def cards():
    connection = get_db_connection()

    cards = connection.execute(
        "SELECT * FROM cards"
    ).fetchall()

    connection.close()

    return render_template("cards.html", cards=cards)

@app.route("/study")
def study():
    card_id = request.args.get("id")

    connection = get_db_connection()

    if card_id:
        card = connection.execute(
            "SELECT * FROM cards WHERE id = ?",
            (card_id,)
        ).fetchone()

        connection.close()

        return render_template("study.html", card=card)

    cards = connection.execute(
        "SELECT * FROM cards"
    ).fetchall()

    connection.close()

    return render_template("study.html", cards=cards)
