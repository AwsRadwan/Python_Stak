from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form1.html')

@app.route('/sub', methods=['post'])
def result_of_submition():
    print("Got Post Info")
    print(request.form)
    yname = request.form['your_name']
    loc = request.form['location']
    fav = request.form['fl']
    com = request.form['comment']
    return render_template("result.html", yname=yname, loc=loc, fav=fav, com=com)


if __name__=="__main__":
    app.run(debug=True)