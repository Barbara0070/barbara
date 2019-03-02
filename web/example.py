from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html.j2', name="nieznajomy")
@app.route("/add_user", methods=["POST"])
def add_user():

    return f"smth {request.form['username ']}"

@app.route("/<name>")
def hello(name):
    return render_template('main.html.j2', name=name)

if __name__ == "__main__":
    app.run()