from flask import Flask, request
import os
from flask import jsonify
from main_handler.read_redirect import *
from main_handler.write_redirect import *
#from validation import *
app = Flask(__name__)

@app.route("/")
def hello():
    print('Hello World')
    return "Hello World!"


@app.route("/readevents",methods=['GET'])
def readEvents():
    print("GETEVENTS")
    #print(a)
    #validate_Function()
    #reObj = read_sql()
    
    #pod = request.args['pod']
    #sTime = request.args['sTime']
    #sDate = request.args['sDate']
    #eTime = request.args['eTime']
    #eDate = request.args['eDate']
    #db_result = read_event(pod,sTime,sDate,eTime,eDate)
    db_result = read_event(request.args['sDateTime'],request.args['eDateTime'])
    ret_obj = db_result
    return jsonify(ret_obj)



@app.route("/writeevents",methods=['POST'])
def writeEvents():
    print("POSTEVENTS")
    #print(a)
    #validate_Function()
    req_data=request.get_json(force=True)
    pod_id = req_data['pod_id']
    msg = req_data['msg']
    db_result = write_event(pod_id,msg)
    ret_obj = {'db_result':db_result}
    return jsonify(ret_obj)