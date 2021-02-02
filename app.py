from flask import Flask, render_template, redirect, url_for, request  # never name your document flask because it will refer to the document instead of the library and the import fails

app = Flask(__name__)

opt = ['Get a dog','Get a cat']
cri = ['Time','Cost']
f_score = {}
scr = {}

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", cri=cri, opt=opt, scr=scr, f_score=f_score)

@app.route("/option", methods=['POST'])
def option():
    if request.method == 'POST':
        new_option = request.form['option']
        opt.append(new_option)
        return redirect(url_for('home'))

@app.route("/criteria", methods=['POST'])
def criteria():
    if request.method == 'POST':
        new_criteria = request.form['criteria']
        cri.append(new_criteria)
        return redirect(url_for('home'))


@app.route("/score", methods=['POST'])
def score():
    if request.method == 'POST':
        new_score = request.form['score']
        cell_cri = request.form['cell_cri']
        cell_opt = request.form['cell_opt']
        if cell_opt not in scr:
            scr[cell_opt] = {}
        scr[cell_opt][cell_cri] = new_score
        print(scr)

    for k, v in scr.items():
        if k == cell_opt:
            l = list(v.values())
            s = sum([int(i) for i in l])
            f_score[cell_opt] = s

        return redirect(url_for('home'))


@app.route("/final_score", methods=['POST'])
def final_score():
    if request.method == 'POST':
        cell_opt = request.form['cell_opt']
        for k, v in scr.items():
            if k == cell_opt:
                l = list(v.values())
                s = sum([int(i) for i in l])
                f_score[cell_opt] = s
        print(f_score)

        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(port=3000, debug=True)  # debug=True so that the page can be updated without having to refresh the server
