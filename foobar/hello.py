from flask import Flask

app = Flask("foobar")
app.config.from_object(__name__)


@app.route('/hello')
def index():
    return "Hello this big awesome new World!"
