from flask import Flask,render_template
app = Flask(__name__)
@app.route('/<name>',methods=['GET'])
def index(name):
    return render_template('index.html',name=name)
@app.errorhandler(404)
def not_found(e):
    print(e)
    return render_template('404.html'),404
if __name__ == '__main__':
    app.run(debug=True)
