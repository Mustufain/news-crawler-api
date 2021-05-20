import urllib
from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_resource

app = Flask(__name__)
api = Api(app)

MONGODB_USERNAME = urllib.parse.quote_plus("mustufain")
MONGODB_PWD = urllib.parse.quote_plus("mongo@!123")
MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PWD}" \
              f"@news-scraper.a2rmv.mongodb.net/" \
              f"ary_news?retryWrites=true&w=majority"

app.config['MONGODB_SETTINGS'] = {
    'host': MONGODB_URI
}
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


initialize_db(app)
initialize_resource(api)

app.run()
