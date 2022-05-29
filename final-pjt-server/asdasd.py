# import pandas as pd
# import numpy as np
# import warnings; warnings.filterwarnings('ignore')
# import json


# movies = pd.read_csv('test4.csv')
# print(movies.shape)
# print(movies.head(2))



### 데이터 csv로 바꾸기 
import pandas as pd
import json
import csv
info = ["pk", "adult", "backdrop_path", "original_language", "overview", "popularity", "poster_path",
    "released_date", "title", "vote_count","vote_average", "genres", "is_active", "director", "actors"]

with open('movies/fixtures/movies_practice.json', encoding='UTF8' , mode='r') as f:
    array = json.load(f)

with open('test4.csv', 'w', encoding='UTF8' ,) as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = info)
    writer.writeheader()
    writer.writerows(array)
