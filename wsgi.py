from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blockip", methods = ['GET','POST'])
def blockip():
    if request.method == 'POST':
        ipaddress = request.form['ipaddress']
        if request.form.get('asa'):
            block_on_asa = request.form['asa']
            #call block_on_asa
        if request.form.get('checkpoint'):
            block_on_checkpoint = request.form['checkpoint']
            #call block_on_checkpoint
        if request.form.get('ips'):
            block_on_ips = request.form['ips']
            #all block_on_ips#
        result = f"Blocked on ..."
        return render_template('opresult.html',result=result)
    else:
        return render_template('index.html')
if __name__== "__main__":
    app.run()


