from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
# Route for the welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Add your other routes here

if __name__ == '__main__':
    app.run(debug=True)