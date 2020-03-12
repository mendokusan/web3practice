from flask import Flask, render_template,redirect,url_for
from mongoengine import *
app = Flask(__name__)
connect('web3')

@app.route('/') 
def index():
    myName = "Erika"
    return render_template('index.html', name=myName)
	

@app.route('/template')
def indextext():    
    return render_template ("index.html")
	
@app.route('/cat')
def dog():    
    return render_template("dog.html")

@app.route("/redirection")
def redirect_route():
    return redirect(url_for("redirect_route"))
	
class User(Document):
    email = StringField()
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
	
erika=User(first_name='Erika',last_name='Namba').save()

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)

postcontent=Post(title="somepost",author=erika).save()

@app.route('/listUsersTest')
def listUsersTest():
	return User.objects.to_json()

@app.route('/post')
def SomePost():
	p = Post.objects.get(id="5e67f7cee6583d77d7642b44")
	fn = p["author"]["last_name"]
	return fn

if __name__ =="__main__":
    app.run(debug=True, port=8080)
	
	