from resources.news import NewsApi


def initialize_resource(api):
    api.add_resource(NewsApi, '/news')
    api.add_resource(NewsApi, '/news/<posted_date>')
