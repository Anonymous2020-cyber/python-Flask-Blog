from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
   return render_template('index.html.txt')

@app.route("/harry")
def harry():
   return "hello harry bhai!"
if __name__ == '__main__':
   app.run(debug=True)

#if __name__ == '__main__':
