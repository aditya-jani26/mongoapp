from app import app


def hello_world():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run(debug=True)