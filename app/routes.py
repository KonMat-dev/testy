from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/index2')
def index2():
    return "Hello, World! 2 "
