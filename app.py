from flask import Flask, render_template, redirect
from flask import Flask


# Dependencies

# -------Create an instance of Flask-------------
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Return template and data
    return render_template("index.html",)


if __name__ == "__main__":
    app.run(debug=True)


# -----------------------------------------------
# if __name__ == "__main__":
#     app.run(port=5001)
