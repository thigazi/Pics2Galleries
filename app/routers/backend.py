from start import app


@app.route('/admin/<task>')
def hello_admin():
    return "Hello World"
