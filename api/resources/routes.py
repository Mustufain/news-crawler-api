from api.resources.news import NewsApi, SearchNewsPostedDateApi


def initialize_resource(api):
    api.add_resource(NewsApi, '/news')
    api.add_resource(SearchNewsPostedDateApi, '/news/<posted_date>')
