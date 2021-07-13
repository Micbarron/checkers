from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def defaultboard():
    return render_template('index.html', x=8, y=8, color0= 'red', color1= 'blue')

@app.route('/<x>/<y>/')
def scale_checkerboard(x, y):
    return render_template('index.html', x=int(x), y=int(y), color0= 'red', color1= 'blue' )


@app.route('/<x>/<y>/<color0>/<color1>')
def scale_checkerboard_color(x, y, color0, color1):
    return render_template('index.html', x=int(x), y=int(y), color0 = color0, color1 = color1  )








if __name__=="__main__":
    app.run(debug=True)