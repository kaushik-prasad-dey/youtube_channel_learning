#first we have to import Flask
from flask import Flask
#second we have created the instance of Flask class
app=Flask(__name__)

@app.route('/contact')
def contact_us():
    return "<h2>This is contact us page</h2>"
@app.route('/about')
def about_us():
    return "<h1>This is about us page!!!</h1>"
#third stage is that creating one UDF and mapped it to the index route
@app.route('/')
def hello_kaushik():
    return "welcome to the Flask world and new changes detection and we added debug=True!!"

#dynamic url add variable name with myusername
#@app.route('/myuser/<myusername>')
def show_your_user(myusername):
    return f'<h2>welcome {myusername} to my channel</h2>'
#add url rule
app.add_url_rule('/myuser/<myusername>','show_your_user',show_your_user)
#data converter
@app.route('/post1/<string:id>')
def showing_number_of_post_as_string(id):
    return f'<h3>The id of the post1 is {id}</h3>'

@app.route('/post1/<int:id>')
def showing_number_of_post(id):
    return f'<h3>The id of the post1 is {id}</h3>'




if __name__=="__main__":
    app.run(debug=True, port=8900)

#1. localhost:8900/ =>welcome to the Flask world and new changes detection and we added debug
#2. localhost:8900/about => This is about us page
#3. localhost:8900/contact=>This is contact us page
#4. localhost:8900/myuser/rahul
#5. localhost:8900/post1/10
#we can also build dynamic url by using variables in that url.
#how we can add the variable to the URLs. use <variable_name>.
#The function then recives the <variable_name> as a keyword argument.
#we can also use a data converter to convert the variable to a specific data type.
#<converter:variable_name> 
#string || int || float || uuid
#add_url_rule() ->the url mapping can also be done using this 
    #add_url_rule()
    