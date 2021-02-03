from flask import Flask, render_template, redirect, url_for, request  # never name your document flask because it will refer to the document instead of the library and the import fails

app = Flask(__name__)

opt_list = ['Get a dog', 'Get a cat']
cri_list = ['Time', 'Cost']
prio_dict = {}
s_dict = {}
fs_dict = {}

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", opt_list=opt_list, cri_list=cri_list, prio_dict=prio_dict, s_dict=s_dict, fs_dict=fs_dict)

@app.route("/option", methods=['POST'])
def option():
    if request.method == 'POST':
        new_option = request.form['option']
        opt_list.append(new_option)
        return redirect(url_for('home'))

@app.route("/criteria", methods=['POST'])
def criteria():
    if request.method == 'POST':
        new_criteria = request.form['criteria']
        cri_list.append(new_criteria)
        return redirect(url_for('home'))

@app.route("/priority", methods=['POST'])
def criteria_priority():
    if request.method == 'POST':
        cell_cri = request.form['cell_criteria']
        prio = request.form['priority']
        prio_dict[cell_cri] = int(prio)
    return redirect(url_for('home'))

@app.route("/score", methods=['POST'])
def score():
    if request.method == 'POST':
        new_score = request.form['score']
        cell_cri = request.form['cell_criteria']
        cell_opt = request.form['cell_option']

        for criteria, priority in prio_dict.items():
            if criteria == cell_cri:
                new_score = int(new_score) * priority

        if cell_opt not in s_dict:
            s_dict[cell_opt] = {}
        s_dict[cell_opt][cell_cri] = new_score
        rebuild_final_option_scores(cell_opt)
        return redirect(url_for('home'))

def rebuild_final_option_scores(cell_opt):
    for k, v in s_dict.items():
        if k == cell_opt:
            l = list(v.values())
            s = sum([int(i) for i in l])
            fs_dict[cell_opt] = s

if __name__ == "__main__":
    app.run(port=3000, debug=True)  # debug=True so that the page can be updated without having to refresh the server
