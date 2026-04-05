from flask import Flask, render_template_string, request

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Kalkulator Ekonomi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 40px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            width: 400px;
            margin: auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
        }
        .hasil {
            margin-top: 20px;
            background: #e8f5e9;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Kalkulator Keuntungan Usaha</h2>
        <form method="POST">
            <label>Modal Awal (Rp)</label>
            <input type="number" name="modal" required>

            <label>Pendapatan (Rp)</label>
            <input type="number" name="pendapatan" required>

            <label>Biaya Operasional (Rp)</label>
            <input type="number" name="biaya" required>

            <button type="submit">Hitung</button>
        </form>

        {% if keuntungan is not none %}
        <div class="hasil">
            <p><strong>Keuntungan Bersih:</strong> Rp {{ keuntungan }}</p>
            <p><strong>Persentase Keuntungan:</strong> {{ persentase }}%</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

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
    


