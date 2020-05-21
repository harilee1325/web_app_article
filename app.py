from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def album():
   return render_template("album.html")


@app.route("/magazine")
def magazine():
   return render_template("magazine.html")
    

@app.route("/blog")
def blog():
   return render_template("blog.html")    


if __name__ == "__main__":
    app.run(debug=True)