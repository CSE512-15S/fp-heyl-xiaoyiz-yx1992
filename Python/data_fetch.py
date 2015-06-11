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
            [["39.73","-86.27"],"Indianapolis"],
            [["41.53","-93.65"],"Des Moines"],
            [["37.65","-97.43"],"Wichita"],
            [["38.18","-85.73"],"Louisville"],
            [["30.03","-90.03"],"New Orleans"],
            [["43.65","-70.32"],"Portland_Maine"],
            [["39.33","-76.42"],"Baltimore"],
            [["42.37","-71.03"],"Boston"],
            [["42.42","-83.02"],"Detroit"],
            [["44.88","-93.22"],"Minneapolis"],
            [["32.32","-90.08"],"Jackson"],
            [["39.12","-94.60"],"Kansas City"],
            [["45.80","-108.53"],"Billings"],
            [["41.30","-95.90"],"Omaha"],
            [["36.08","-115.17"],"Las Vegas"],
            [["42.93","-71.43"],"Manchester"],
            [["40.70","-74.17"],"Newark"],
            [["35.05","-106.60"],"Albuquerque"],
            [["40.77","-73.98"],"New York"],
            [["35.22","-80.93"],"Charlotte"],
            [["46.90","-96.80"],"Fargo"],
            [["40.00","-82.88"],"Columbus"],
            [["35.40","-97.60"],"Oklahoma City"],
            [["45.60","-122.60"],"Portland_Oregon"],
            [["39.88","-75.25"],"Philadelphia"],
            [["41.73","-71.43"],"Providence"],
            [["33.95","-81.12"],"Columbia"],
            [["43.58","-96.73"],"Sioux Falls"],
            [["35.05","-90.00"],"Memphis"],
            [["29.97","-95.35"],"Houston"],
            [["40.78","-111.97"],"Salt Lake City"],
            [["44.47","-73.15"],"Burlington"],
            [["36.85","-75.98"],"Virginia Beach"],
            [["47.45","-122.30"],"Seattle"],
            [["38.37","-81.60"],"Charleston"],
            [["42.95","-87.90"],"Milwaukee"],
            [["41.15","-104.82"],"Cheyenne"]
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