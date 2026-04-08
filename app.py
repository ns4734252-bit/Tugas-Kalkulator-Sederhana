from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    keuntungan = None
    persentase = None

    if request.method == 'POST':
        modal = float(request.form['modal'])
        pendapatan = float(request.form['pendapatan'])
        biaya = float(request.form['biaya'])

        keuntungan = pendapatan - biaya - modal

        if modal > 0:
            persentase = round((keuntungan / modal) * 100, 2)
        else:
            persentase = 0

    return render_template_string(html, keuntungan=keuntungan, persentase=persentase)

if __name__ == '__main__':
    app.run(debug=True)
    



