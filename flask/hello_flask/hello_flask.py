import flask

APP = flask.Flask(__name__)

@APP.route("/")
def index():
    """show with "/" index page
    """
    return
flask.render_template("index.html")

if __name__ == "__main__":
    APP.debug = True
    APP.run()
