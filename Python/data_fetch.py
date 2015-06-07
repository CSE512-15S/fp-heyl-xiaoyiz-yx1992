from instagram.client import InstagramAPI
import csv
import time

api = InstagramAPI(client_id='18ee6a03eec44280bf88fbe63dcce92d', client_secret='02cc8d7afecb448d87a7cd28ffe9432b')

locations = [
            [["37.782158", "-122.434356"]],
            [["34.069570", "-118.444698"]],
            [["47.656028", "-122.309985"]],
            [["45.546765", "-122.621463"]],
            [["29.726584", "-95.380692"]],
            [["40.687695", "-73.945349"]],
            [["41.854194", "-87.681344"]],
            [["42.362860", "-71.095266"]],
            [["36.216460", "-115.269070"]],
            [["25.779232", "-80.194345"]],
            [["43.676043", "-79.401404"]],
            [["49.277355", "-123.121510"]],
            [["48.861344", "2.346717"]],
            [["51.510697", "-0.135244"]],
            [["41.897295", "12.491366"]],
            [["43.775000", "11.253328"]],
            [["55.755975", "37.625628"]],
            [["40.417442", "-3.700136"]],
            [["41.014648", "28.895450"]],
            [["48.141625", "11.578915"]]
            ]

names = ["SanFrancisco", "LosAngeles", "Seattle", "Portland","Houston", "NYC", "Chicago", "Boston", "LasVegas", "Miami",
            "Toronto", "Vancouver", "Paris", "London", "Rome", "Florence", "Moscow", "Madrid", "Istanbul", "Munich"]
count = 0

for location in locations:
    with open(names[count]+".csv", 'wb') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(["ID", "Created At", "Filter", "Number of Likes", "HashTags", "url"])
        for i in range(0, 5):
            recent_media = api.media_search(lat=location[0][0],lng=location[0][1],distance=5000,count=500,min_timestamp=time.time()-(i+1)*24*60*60, max_timestamp = time.time()-i*24*60*60)
            for media in recent_media:
                tags = []
                if hasattr(media, 'tags'):
                    tags = media.tags
                    writer.writerow([media.id, media.created_time, media.filter, media.like_count, tags, media.images['standard_resolution'].url])
    count = count + 1