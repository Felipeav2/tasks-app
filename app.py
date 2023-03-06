import flask
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'f'


class TaskForm(FlaskForm):
    majorTask = StringField("Major Task", validators=[DataRequired()])

    shortTask1 = StringField("Short Task 1", validators=[DataRequired()])
    shortTask2 = StringField("Short Task 2", validators=[DataRequired()])
    shortTask3 = StringField("Short Task 3", validators=[DataRequired()])

    maintenance1 = StringField("Maintenece task 1", validators=[DataRequired()])
    maintenance2 = StringField("Maintenece task 2", validators=[DataRequired()])
    maintenance3 = StringField("Maintenece task 3", validators=[DataRequired()])

    submit = SubmitField("Add tasks")

tasks = []

'''
majorTasks = []
shortTask1 = []
shortTask2 = []
shortTask3 = []
maintenanceTask1 = []
maintenanceTask2 = []
maintenanceTask3 = []
'''



@app.route("/")
def index():
    return flask.render_template("index.html")
    
@app.route("/tasks", methods=['GET', 'POST'])
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        majorTask = form.majorTask.data

        shortTask1 = form.shortTask1.data
        shortTask2 = form.shortTask2.data
        shortTask3 = form.shortTask3.data

        maintenanceTask1 = form.maintenance1.data
        maintenanceTask2 = form.maintenance2.data
        maintenanceTask3 = form.maintenance3.data

        tasks.append({
            "majorTask": majorTask,
            "shortTask1": shortTask1,
            "shortTask2": shortTask2,
            "shortTask3": shortTask3,
            "maintenance1": maintenanceTask1,
            "maintenance2": maintenanceTask2,
            "maintenance3": maintenanceTask3,
        })
        return redirect(url_for("index"))
    return render_template("tasks.html", form=form, tasks=tasks)





if __name__ == "__main__":
    app.run(debug = True)