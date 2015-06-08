from instagram.client import InstagramAPI
import csv
import time

api = InstagramAPI(client_id='18ee6a03eec44280bf88fbe63dcce92d', client_secret='02cc8d7afecb448d87a7cd28ffe9432b')

locations = [
            [["33.653333", "-86.808889"],"Birmingham"],
            [["61.216667", "-149.900000"],"Anchorage"],
            [["33.450000", "-112.066667"],"Phoenix"],
            [["34.736111", "-92.331111"],"Little Rock"],
            [["34.05", "-118.25"],"Los Angeles"],
            [["39.761850", "-104.881105"],"Denver"],
            [["41.186389", "-73.195556"],"Bridgeport"],
            [["39.745833", "-75.546667"],"Wilmington"],
            [["30.336944", "-81.661389"],"Jacksonville"],
            [["33.755", "-84.39"],"Atlanta"],
            [["21.3", "-157.816667"],"Honolulu"],
            [["43.616667", "-116.2"],"Boise"],
            [["41.836944", "-87.684722"],"Chicago"],
            [["33.653333", "-86.808889"],"Indianapolis"],
            [["61.216667", "-149.900000"],"Des Moines"],
            [["33.450000", "-112.066667"],"Wichita"],
            [["34.736111", "-92.331111"],"Louisville"],
            [["39.761850", "-104.881105"],"New Orleans"],
            [["43.666667", "-70.266667"],"Portland"],
            [["41.186389", "-73.195556"],"Baltimore"],
            [["42.358056", "-71.063611"],"Boston"],
            [["39.745833", "-75.546667"],"Detroit"],
            [["30.336944", "-81.661389"],"Minneapolis"],
            [["33.755", "-84.39"],"Jackson"],
            [["21.3", "-157.816667"],"Kansas City"],
            [["43.616667", "-116.2"],"Billings"]
            [["33.755", "-84.39"],"Omaha"],
            [["33.755", "-84.39"],"Las Vegas"],
            [["33.755", "-84.39"],"Manchester"],
            [["33.755", "-84.39"],"Newark"],
            [["33.755", "-84.39"],"Albuquerque"],
            [["33.755", "-84.39"],"New York"],
            [["33.755", "-84.39"],"Charlotte"],
            [["33.755", "-84.39"],"Fargo"],
            [["33.755", "-84.39"],"Columbus"],
            [["33.755", "-84.39"],"Oklahoma City"],
            [["33.755", "-84.39"],"Portland"],
            [["33.755", "-84.39"],"Philadelphia"],
            [["33.755", "-84.39"],"Providence"],
            [["33.755", "-84.39"],"Columbia"],
            [["33.755", "-84.39"],"Sioux Falls"],
            [["33.755", "-84.39"],"Memphis"],
            [["33.755", "-84.39"],"Houston"],
            [["33.755", "-84.39"],"Salt Lake City"],
            [["33.755", "-84.39"],"Burlington"],
            [["33.755", "-84.39"],"Virginia Beach"],
            [["33.755", "-84.39"],"Seattle"],
            [["33.755", "-84.39"],"Charleston"],
            [["33.755", "-84.39"],"Milwaukee"],
            [["33.755", "-84.39"],"Cheyenne"],
            ]

for location in locations:
    with open(location[1]+".csv", 'wb') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(["ID", "Created At", "Filter", "Number of Likes", "HashTags", "url"])
        for i in range(0, 5):
            recent_media = api.media_search(lat=location[0][0],lng=location[0][1],distance=5000,count=500,min_timestamp=time.time()-(i+1)*24*60*60, max_timestamp = time.time()-i*24*60*60)
            for media in recent_media:
                tags = []
                if hasattr(media, 'tags'):
                    tags = media.tags
                    writer.writerow([media.id, media.created_time, media.filter, media.like_count, tags, media.images['standard_resolution'].url])