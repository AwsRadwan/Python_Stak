from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Checkerboard2.html', vertical = 8, horizontal = 8)

@app.route('/<num>')
def callDown(num):
    return render_template('Checkerboard2.html', vertical = 8, horizontal = int(num))

@app.route('/<num1>/<num2>')
def acrossDown(num1,num2):
    return render_template('Checkerboard2.html', vertical = int(num1), horizontal = int(num2) )

@app.route('/<num1>/<num2>/<color1>/<color2>')
def hellaColors(num1, num2, color1, color2):
    return render_template('Checkerboard2.html', vertical = int(num1), horizontal = int(num2), color1= color1, color2 = color2)
if __name__ == "__main__":
    app.run(debug=True)