import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")
@app.route("/submit", methods=["POST"])
def tasks():
    if request.method == "POST":
        majorTask = request.form.getlist["majorTask"]
        shortTasks = request.form.getlist["shortTask"]
        maintence = request.form.getlist["maintence"]

        return render_template("index.html", majorTasks=majorTasks, shortTasks=shortTasks, maintence=maintence)


if __name__ == "__main__":
    app.run(debug = True)