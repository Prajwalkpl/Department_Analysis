from flask import Flask, render_template, request

app = Flask(__name__)

# Define a dictionary to map problems to departments (you can expand this as needed).
problem_to_department = {
    "Road Issue": "Transport Department",
    "House waste Issue": "BBMP",
    "Electricity Issue": "KSEB",
    # Add more mappings as needed
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        problem = request.form.get("problem")
        department = get_department_for_problem(problem)
        return render_template("result.html", problem=problem, department=department)
    return render_template("base.html")

def get_department_for_problem(problem):
    return problem_to_department.get(problem, "Unknown Department")

if __name__ == "__main__":
    app.run(debug=True)
