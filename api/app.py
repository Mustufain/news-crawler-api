import urllib
from flask import Flask
from flask_restful import Api
from api.database.db import initialize_db
from api.resources.routes import initialize_resource
from api.common.utils import get_pwd, get_username

app = Flask(__name__)
api = Api(app)

MONGODB_USERNAME = urllib.parse.quote_plus(get_username())
MONGODB_PWD = urllib.parse.quote_plus(get_pwd())
MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PWD}" \
              f"@news-scraper.a2rmv.mongodb.net/" \
              f"ary_news?retryWrites=true&w=majority"

app.config['MONGODB_SETTINGS'] = {
    'host': MONGODB_URI
}
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


initialize_db(app)
initialize_resource(api)

if __name__ == '__main__':
    app.run()
