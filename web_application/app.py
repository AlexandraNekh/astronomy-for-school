from flask import Flask, render_template, url_for, request, send_from_directory

app = Flask(__name__, template_folder='frontend')

app.static_folder = 'frontend/static'


@app.route("/")
def main():
    return render_template("base.html")


@app.route("/astronauts")
def astronauts():
    return render_template("astronauts.html")


@app.route("/satellites")
def satellites():
    return render_template("satellites.html")


@app.route("/discoveries")
def discoveries():
    return render_template("discoveries.html")


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0')
