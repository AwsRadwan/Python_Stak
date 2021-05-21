from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def level1():
    return render_template('Playground1.html', num = 3, bcolor="blue")

@app.route('/play/<x>')
def level2(x):
    return render_template('Playground1.html', num = int(x), bcolor="blue")

@app.route('/play/<x>/<color>')
def level3(x,color):
    return render_template('Playground1.html', num = int(x), bcolor = color)

if __name__=="__main__":
    app.run(debug=True)