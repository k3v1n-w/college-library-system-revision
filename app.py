from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/books")
def books():

    book_list=[
        {"id":1,"title":"An Inspector Calls","author":"Priestley","availability":True},
        {"id":2,"title":"Macbeth","author":"Shakespeare","availability":True},
        {"id":3,"title":"Othello","author":"Shakespeare","availability":False},
        {"id":4,"title":"A Christmas Carol","author":"Priestley","availability":False}
        ]

    search = request.args.get("search","")

    if search:
        book_list = [
            book for book in book_list
            if search.lower() in book["title"].lower()
        ]

    return render_template("book.html", books=book_list)

if __name__ == "__main__":
    app.run(debug=True)