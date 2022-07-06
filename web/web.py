from flask import Flask, render_template, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Base(Resource):
    def get(self):
        return {"data": "urmum"}


api.add_resource(Base, "/api/")


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])  # Home and / route to the same place
def HomePage():
    return render_template("home.html")


@app.route("/signin", methods=["GET", "POST"])
def SignIn():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
    return render_template("signin.html")


@app.route("/signup", methods=["GET", "POST"])
def SignUp():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
    return render_template("signup.html")


navigation = ["u", "r", "m", "u", "m"]


@app.route("/printvariables", methods=["GET"])
def PrintVariables():
    return render_template("printvariables.html", navigation=navigation)


if __name__ == "__main__":
    app.run(debug=True)
