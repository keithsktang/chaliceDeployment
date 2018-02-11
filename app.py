# Code Challenge -- using Chalice framework to create a serverless app that can deploy from github to Heroku
# Challenge Accpted!


# import chalice and dependencies
from chalice import Chalice
import http.client
import json
import os


app = Chalice(app_name='chaliceDeploy')

# a simple https post request for heroku build api
# passing commit hash as version identifier
@app.route('/{version}', cors=True)
def index(version):
    data = {"source_blob": {"url": "https://github.com/keithsktang/herokuDeployment/archive/master.tar.gz", "version": version}}
    headers = {"Accept": "application/vnd.heroku+json; version=3",
              "Content-Type": "application/json",
              # get auth token from environment_variables
              "Authorization": os.environ['HEROKU_KEY']}
    conn = http.client.HTTPSConnection("api.heroku.com")
    conn.request("POST", '/apps/pure-beach-57030/builds', json.dumps(data), headers)
    response = conn.getresponse()
    return json.loads(response.read())
    conn.close()
