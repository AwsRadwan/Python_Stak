users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def users_table():
    return render_template('table.html', a= users[0]['first_name'], b= users[0]['last_name'], c= users[1]['first_name'], d= users[1]['last_name'], e= users[2]['first_name'], f= users[2]['last_name'], g= users[3]['first_name'], k= users[3]['last_name'])
    
if __name__ == "__main__":
    app.run(debug=True)