from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/autor')
def autor():
    return render_template('avtor.html')


@app.route('/lessons')
def lessons():
    return render_template('lessons.html')


@app.route('/instrument')
def instrument():
    return render_template('instr.html')

@app.route('/lessons1')
def lessons1():
    return render_template('lessons1.html')

@app.route('/lessons2')
def lessons2():
    return render_template('lessons2.html')

@app.route('/lessons3')
def lessons3():
    return render_template('lessons3.html')

@app.route('/lessons4')
def lessons4():
    return render_template('lessons4.html')

@app.route('/lessons5')
def lessons5():
    return render_template('lessons5.html')

@app.route('/lessons6')
def lessons6():
    return render_template('lessons6.html')

@app.route('/lessons7')
def lessons7():
    return render_template('lessons7.html')

@app.route('/lessons8')
def lessons8():
    return render_template('lessons8.html')

@app.route('/lessons9')
def lessons9():
    return render_template('lessons9.html')

@app.route('/lessons10')
def lessons10():
    return render_template('lessons10.html')


if __name__ == "__main__":
    app.run(threaded=True)
