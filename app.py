import dbhelpers as dbh
from flask import Flask, request, make_response
import apihelpers as apih
import json

app = Flask(__name__)

@app.get('/api/candy')
def get_candy():
    # no input to validate so straight to run statement
    results = dbh.run_statement('CALL get_candy()')
# if result of run_statement is a list tpye then return a success message else send a server error message
    if(type(results) == list):
      return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Error'), 500)


app.run(debug=True)        