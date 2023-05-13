from flask import Flask, render_template, request

app = Flask(__name__)

tasks = {
    "majorTask": "",
    "shortTasks": [],
    "maintenanceTasks": []
}


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/tasks", methods=["GET", "POST"])
def set_tasks():
    if request.method == "POST":
        task_type = request.form.get("taskType")
        task = request.form.get("task")

        if task_type == "majorTask":
            tasks["majorTask"] = task
        elif task_type == "shortTask":
            tasks["shortTasks"].append(task)
        elif task_type == "maintenanceTask":
            tasks["maintenanceTasks"].append(task)

    return render_template("tasks.html", tasks=tasks)




if __name__ == "__main__":
    app.run(debug=True)