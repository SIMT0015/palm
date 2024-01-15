from flask import Flask, request, render_template
import google.generativeai as palm

palm.configure(api_key = "AIzaSyBqoLSiRQW_OzlwnkB1d8iPeqp0k9A08Lg")
defaults = {'model':"models/chat-bison-001"}

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        response = palm.chat(**defaults, messages = q) 
        return(render_template("index.html", result = response.last))
    else:
        return(render_template("index.html", result="waiting for prompt"))
if __name__ == "__main__":
    app.run(port = 1234) # i need this port number because 5000 is being used alr
