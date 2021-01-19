from flask import Flask, render_template, request  # never name your document flask because it will refer to the document instead of the library and the import fails

app = Flask(__name__)

opt = []
cri = []
scr = []


@app.route("/", methods=['POST', 'GET'])
def option():
    if request.method == 'POST':
        new_option = request.form['option']
        opt.append(new_option)
        return render_template("index.html", cri=cri, opt=opt)
    else:
        return render_template("test.html")


@app.route("/criteria", methods=['POST', 'GET'])
def criteria():
    if request.method == 'POST':
        new_criteria = request.form['criteria']
        cri.append(new_criteria)
        return render_template("index.html", cri=cri, opt=opt)
    else:
        return render_template("test.html")


@app.route("/score", methods=['POST', 'GET'])
def score():
    if request.method == 'POST':
        new_score = request.form['score']
        cell_cri = request.form['cell_cri']
        cell_opt = request.form['cell_opt']
        print(new_score)
        print(cell_cri)
        print(cell_opt)
        scr.append([cell_cri, cell_opt, new_score])
        print(scr)
        return render_template("index.html", scr_element=new_score, cri=cri, opt=opt, scr=scr)
    else:
        return render_template("test.html")


@app.route("/final_score", methods=['POST', 'GET'])
def final_score():
    if request.method == 'POST':
        cell_opt = request.form['cell_opt']
        opt_scr_lst = []
        for i, j in list(enumerate(scr)):
            if cell_opt in j:
                opt_scr = scr[i][2]
                opt_scr_lst.append(opt_scr)

        return render_template('index.html', final_score=str(sum((int(i) for i in opt_scr_lst))), cri=cri, opt=opt,
                               cell_opt=cell_opt)
    else:
        return render_template("test.html")


if __name__ == "__main__":
    app.run(port=3000, debug=True)  # debug=True so that the page can be updated without having to refresh the server
