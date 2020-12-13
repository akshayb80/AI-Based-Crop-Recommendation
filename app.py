from flask import Flask,request,render_template,redirect,jsonify,url_for
from model import result
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        n=request.form['n']
        p=request.form['p']
        k=request.form['k']
        temp=request.form['temp']
        hum=request.form['hum']
        ph=request.form['ph']
        rain=request.form['rain']

        res = result(n,p,k,temp,hum,ph,rain)
        return redirect(url_for('predict', res=[n,p,k,temp,hum,ph,rain,res[0]]))
        
    return render_template('index.html')

@app.route('/predict')
def predict():
    res = request.args.getlist('res')
    return render_template('predict.html',res=res)

if __name__ == "__main__":
    app.run(debug=True)