from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'
# @app.route('/')
# def cc()
# def ccc(x):
#     x+=1

@app.route('/')
def counter():
    if 'count' in session:
        session["count"]+=1
        count=session['count']
        return render_template('counter.html', count=count)
    
    else:
        session['count'] =0
    
        return render_template('counter.html', count=session['count'])

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect("/")

@app.route('/addtwo')
def addtwo():
    session['count'] += 1
    return redirect('/')

@app.route('/inp', methods=['post'])
def aadd():
    session['count'] += int(request.form['inp'])-1
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)