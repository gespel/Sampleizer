from flask import Flask, render_template_string, jsonify
import matplotlib
matplotlib.use("Agg")  # non-GUI backend
import matplotlib.pyplot as plt
import io
import base64
import random
from sampleizer import Sampleizer
from modules import sine, randosine
import uuid
import randomname

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <title>Sampleizer</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body class="p-5">
    <div class="container d-flex flex-column align-items-center">
      <h1 class="mb-4">Sampleizer</h1>
      <button id="gen-btn" class="btn btn-primary mb-4">Graph generieren</button>
      <button id="download-btn" class="btn btn-secondary mb-4 ms-2">Samples downloaden</button>
      <div id="graph"></div>
    </div>
    <script>
      document.getElementById('gen-btn').onclick = function() {
        fetch('/generate')
          .then(response => response.json())
          .then(data => {
            document.getElementById('graph').innerHTML = '<img src="data:image/png;base64,' + data.img + '" class="img-fluid"/>';
          });
      }
      document.getElementById('download-btn').onclick = function() {
        window.location.href = '/download_samples';
      }
    </script>
  </body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/generate')
def generate():
    global last_samples
    s = Sampleizer("randosineOne")
    si = sine.Sine(10.0, 48000.0)
    rs = randosine.RandoSine(20, 48000.0, 1)
    for i in range(4800):
        s.add_sample(rs.get_sample())
    last_samples = s.get_samples()

    plt.figure()
    plt.plot(s.get_samples())
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')

    #print(s.get_definition())
    return jsonify({'img': img_base64})

@app.route('/download_samples')
def download_samples():
    global last_samples
    if 'last_samples' not in globals():
        return "Keine Samples generiert.", 400
    sample_data = "\n".join(str(x) for x in last_samples)
    return (
        sample_data,
        200,
        {
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Disposition': f'attachment; filename="{randomname.get_name()}.swave"'
        }
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)