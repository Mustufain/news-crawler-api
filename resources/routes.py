from resources.news import NewsApi, SearchNewsPostedDate


def initialize_resource(api):
    api.add_resource(NewsApi, '/news')
    api.add_resource(SearchNewsPostedDate, '/news/<posted_date>')
