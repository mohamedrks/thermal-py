from pythermalcomfort.models import pmv_ppd 
from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'page' : 'Home' , 'Time' : time.time()} 
    result = pmv_ppd(tdb=27, tr=27 , vr=0.1, rh=50, met=1.1, clo=0.5, standard="ASHRAE")

    json_dump = json.dumps(result)

    return json_dump

if __name__ == '__main__':
    app.run(port=8080)