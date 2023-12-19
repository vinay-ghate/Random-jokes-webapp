from flask import Flask,render_template,url_for
import pyjokes

app = Flask(__name__)

@app.route('/')
def index():
    joke = joke=pyjokes.get_joke()
    return render_template('index.html',joke=joke)

if __name__=="__main__":
    app.run(debug=True)




