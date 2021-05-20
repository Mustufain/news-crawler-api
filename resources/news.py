import json
from flask import Response, request
from database.models import News
from flask_restful import Resource
from common.utils import get_paginated_list


class NewsApi(Resource):

    def get(self):
        """HTTP GET METHOD"""
        # default behavior:
        # show 20 records
        # start with first record
        start = int(request.args.get('start', 1))
        limit = int(request.args.get('limit', 20))
        # get count of objects in db
        count = News.objects.count()
        url = request.base_url
        data = {}
        links_data = get_paginated_list(count, start, limit, url)
        start -= 1
        end = start - 1 + limit
        news = json.loads(News.objects().order_by('_id').exclude('id')[start:end].to_json())
        data['_links'] = links_data
        data['results'] = news
        json_data = json.dumps(data, ensure_ascii=False, indent=4)
        return Response(json_data, mimetype="application/json", status=200)

    def get(self, posted_date):
        """HTTP GET METHOD TO GET NEWS ARTICLES FOR A PARTICULAR DATE"""
        print(posted_date)
        return

    def get(self, keyword):
        """HTTP GET METHOD TO GET NEWS ARTICLES WHERE KEYWRODS AcleaRE PRESENT"""
        return


# Api Improvements
# implements http
# Add tests
#