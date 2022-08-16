from pythermalcomfort.models import pmv_ppd 
from flask import *
import json, time

app = Flask(__name__)

@app.route('/cal/', methods=['GET'])
def home_page():
    data_set = {'page' : 'Home' , 'Time' : time.time()} 
    user_query = str(request.args.get('temp'))
    temp = float(user_query)
    result = pmv_ppd(tdb=27, tr=temp , vr=0.1, rh=50, met=1.1, clo=0.5, standard="ASHRAE")

    json_dump = json.dumps(result)

    return json_dump

if __name__ == '__main__':
    app.run()