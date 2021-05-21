from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_worldd():
    return 'Hello World!'

@app.route('/dojo')
def hello_world():
    return 'Dojo!'

@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi " + name +"!"

@app.route('/repeat/<num>/<name>')
def hii(name,num):
    print(name)
    print(num)
    string = ""
    for i in range(int(num)):
        string +=f"{name}\n"
    return string

if __name__=="__main__":
    app.run(debug=True)
