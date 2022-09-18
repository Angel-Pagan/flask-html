""" Import Packages """
from flask import Flask, render_template

""" App Flask Code """
app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('homepage.html')

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)