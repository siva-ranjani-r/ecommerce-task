from flask import Flask,render_template,request


app=Flask(__name__)


lis=[]
@app.route("/create")
def ecommerce():
    lis.append(stu)
    return render_template("index.html",data=lis)


class buyer:
    def __init__(self, name, age,purchased,amount,url):
        self.name=name
        self.age=age
        self.purchased=purchased
        self.amount=amount
        self.url=url

    def product(self):
        return self.name,self.age,self.purchased,self.amount,self.url


@app.route("/",methods=['get','post'])
def create_object():
    if request.method == "POST":
        name=request.form.get("name")
        age=request.form.get("age")
        purchased=request.form.get("purchased")
        amount=request.form.get("amount")
        url=request.form.get("url")
        obj=buyer(name,age,purchased,amount,url)
        lis.append(obj)
    return render_template("create.html",data=lis)
        
    
stu=buyer("sivaranjani",23,"ipad",45000,"/static/images/ipad.png")




if __name__=="__main__":
    app.run(debug=True)