from flask import Flask
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    return '<h1>charpter one demo.</h1>'
@app.route('/<name>')
def greet(name):
    return '<h1>Welcome,{}</h1>'.format(name)
if __name__ == '__main__':
    app.run(debug=True)
