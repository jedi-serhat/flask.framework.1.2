from flask import Flask 
app = Flask(__name__)

@app.route("/")
def head():
    return "Hello  Serhat. Ne yapacaz bu Kodlari"

@app.route("/second")
def head2():
    return "Yalan, baskasi yalan, olumden baskasi yalan"

@app.route("/third")
def head3():
    return "Yeter artik"

@app.route("/forth/<string:id>")
def forth(id):
    return f"Ne istersen onu basarim {id}"

if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)