News Crawler Api
--
Rest Api to access news articles. Currently there are two end points: 

1. ```/news/YYYY-MM-dd``` will get all the news articles posted on ```YYYY-MM-dd```


basic usage of the end point running locally: 
```
 curl "http://127.0.0.1:5000/news/2021-06-01"
 
{
 
    "_id": {
            "$oid": "60a2b9e5b1fb0d2cd69db912"
        },
        "url": "https://arysports.tv/test-cricket-limited-make-many-changes-azhar-ali/",
        "text": "HARARE: Azhar Ali believes that too many changes in Test cricket are not ideal due to the limited window for the longer format in the year. Speaking to reporters via online presser, Azhar said players need some time to adjust in Test cricket and regular changes wouldn’t favor building a team. “See, Test cricket is played very limited in a year so it is impossible to make regular changes,” he said. “I have played 87 Tests in 11 years and only 91 Test were played during that time. Average 8 Tests are played everywhere so how can we make so many changes. It will cause hurdles in building a team with making regular changes,” he stressed. Talking about Day 1 of the second Test against Zimbabwe, Azhar said the last few overs were not good for them otherwise they dominated the whole day. “If you look at our performance, we were well set on the track. Unfortunately, in the last eight overs, we lost quick wickets as the ball was coming slowly during that time. We will try to post a big total tomorrow and restrict them earlier,” he concluded. Comments comments",
        "author": "ARY Sports",
        "posted_date": {
            "$date": 1620345600000
        },
        "headline": "'Test cricket is very limited to make so many changes' Azhar Ali",
        "places_mentioned": [
            "Zimbabwe",
            "HARARE",
            "Test"
        ]
 }
```

2. ```/news``` will get first 20 records. ```/news?start=begin&limit=end``` will 
   get records from ```begin``` uptil ```end``` 
   eg: ```/news?start=40&limit=100``` will get 40th record uptil 100th record from the database. 

basic usage of the end point: 

```
curl "http://127.0.0.1:5000/news?start=1&limit=2"

{
    "_links": {
        "next": "/news?start=3&limit=2",
        "start": 1,
        "limit": 2,
        "count": 21404,
        "base": "http://127.0.0.1:5000/news"
    },
    "results": [
        {
            "url": "https://arynews.tv/en/instagram-removes-kangana-ranaut/",
            "text": "Instagram removes Kangana Ranaut’s COVID-19 post Instagram is the latest social media platform to shut out Bollywood actor Kangana Ranaut for her incriminatory posts, deleting a post in which she called COVID-19 a “small-time flu.” Ranaut, who was permanently banned from Twitter earlier this month for violating its community guidelines following her tweets inciting post-poll violence, took to Instagram earlier this week to share that she had tested positive for COVID. Following the deletion of the said post, Ranaut took to her stories to slam the photo-sharing app, saying, “Instagram has deleted my post where I threatened to demolish Covid because some were hurt.” “ _Matlab terrorists and communists sympathisers suna tha Twitter pe_ but Covid fan club (I had heard taunts of terrorist and communist sympathisers on Twitter, but Covid fan club).. awesome,” remarked the _Tanu Weds Manu_ actor. > She went on to add that it’s been two days since the post but she doesn’t think she “will last here more than a week.” Self-awareness is a virtue, are we right? Comments comments",
            "author": "Web Desk",
            "posted_date": {
                "$date": 1620604800000
            },
            "headline": "Instagram removes Kangana Ranaut's COVID-19 post - ARY NEWS",
            "places_mentioned": [
                "Instagram"
            ]
        }
    ]
}
```

TBA:
1. Add endpoint to do keyword search
2. Deploy to EC2

# Usage
1. Create virtualenv ```pyenv virtualenv 3.7.1 <your-virtuale-env>```
2. Set PYTHONPATH ```export PYTHONPATH=/path/to/news-crawler-api```
3. Start flask server ```python api/app.py```