from flask import Flask, render_template, request
import json
from Gertrudis.static.Claude import Claude

gertrudis = Claude()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/api/Gertrudis", methods=['GET', 'POST'])
    def get():
          r = request.json
        #   print('u.u', r)
        #   print('u.u', r['data'])
        #   message = r['data']
          r = gertrudis.message(r['data'])
          message = r.content[0].text
          return json.dumps(message)
    
    @app.route("/", methods=['GET', 'POST'])
    def home():
            return render_template("index.html")

    return app