from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def calculate():
    expression = ""
    if request.method == 'POST':
        number = request.form.get('number', '')
        operator = request.form.get('operator', '')
        calculate = request.form.get('calculate', '')
        clear = request.form.get('clear', '')

        expression = request.form.get('expression', '')

        if number:
            expression += number
        elif operator:
            expression += operator
        elif calculate:
            try:
                expression = str(eval(expression))
            except:
                expression = "Error"
        elif clear:
            expression = ""

    return render_template('index.html', expression=expression)


if __name__=="__main__":
    app.run(host="0.0.0.0")
