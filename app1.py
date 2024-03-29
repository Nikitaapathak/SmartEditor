from gingerit.gingerit import GingerIt

from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/")
def sent():
    if request.method == "GET":
        return render_template("index2.html")
    else:

        if not request.form["SENT"]:
            return redirect("/")


@app.route("/sent_correct", methods=["GET", "POST"])
def sent_correct():
    if request.method == 'POST':
        text = request.form["SENT"]
        parser = GingerIt()
        print(parser.parse(text)['corrections'])
        result = parser.parse(text)['result']
        return render_template('index2.html', output1=result)



# if __name__ == "__main__":
#     app.run(host='0.0.0.0')

app.run()
