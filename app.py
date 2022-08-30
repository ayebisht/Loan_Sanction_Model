
from flask import *
import pickle
import sklearn

app=Flask(__name__)


def make_pred(inps):
    model = pickle.load(open('loan_santion.pkl','rb')) #unpickle
    res=model.predict([inps])[0]
    return res


@app.route("/")
def home_func():
    return render_template('home.html')


@app.route("/predlink",methods=['POST'])
def predict_func():
    Gender=int(request.form["Gender"])
    Married=int(request.form["Married"])
    Dependents=int(request.form["Dependents"])
    Education=int(request.form["Education"])
    Self_Employed=int(request.form["Self_Employed"])
    Applicant_Income=int(request.form["Applicant_Income"])
    Coapplicant_Income=int(request.form["Coapplicant_Income"])
    Loan_Amount=int(request.form["Loan_Amount"])
    Loan_Amount_Term=int(request.form["Loan_Amount_Term"])
    Credit_History=int(request.form["Credit_History"])
    Property_Area=int(request.form["Property_Area"])

    ip_params=[Gender,Married,Dependents,Education,Self_Employed,Applicant_Income,Coapplicant_Income,Loan_Amount,Loan_Amount_Term,Credit_History,Property_Area]

    result=make_pred(ip_params)
    return render_template("display.html",res=result)


if __name__=='__main__':
     app.run(debug=True)
