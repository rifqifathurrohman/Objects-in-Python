
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    html="""
    <style type="text/css">
    h1 {
	color: grey;
    }
    h3{
       color: Blue;
       }
    p{
      color: Red;
      }
    </style>
    <center><h1><b>LATIHAN PYTHON</b></h1></center> 
    <center><h3><b>Hallo semua ! Ini adalah latihan dasar Python pada Flask <br>
    Saya Rifqi Fathurrohman NPM 1204076 Kelas 2C D4 Teknik Informatika <br>
    POLITEKNIK POS INDONESIA.</b></h3></center>
    <p align="center"><b>Sekian Terima kasih
    </b></p>
    """
    return html





