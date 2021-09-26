from start import app


@app.route('/')
def hello_frontend():
    return "this is the frontend"
