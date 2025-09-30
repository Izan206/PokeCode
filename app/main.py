from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome_page():
    return "Hello!, we are Izan and Axel and this is PokeCode"

if __name__=='__main__':
    app.run('0.0.0.0', 8080)