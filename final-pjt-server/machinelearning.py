import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
import csv




movies = pd.read_csv('test4.csv')
movies_df = movies[['pk', 'popularity', 'title','vote_count', 'vote_average', 'genres', 'director']]
# 문자열로 된 데이터를 literal_evalw로 변경
movies_df['genres'] = movies_df['genres'].apply(literal_eval)
# genres의 각 단어들을 하나의 문장으로 변환
movies_df['genres_literal'] = movies_df['genres'].apply(lambda x : (' ').join(x))

# machinelearning을 하기위해서 단어들의 카운트로 여러문서들을 벡터화, 카운트행렬, 단어 문서 행렬
count_vect = CountVectorizer(min_df=0, ngram_range=(1, 2))
# traindataset에 mean과 variance 학습을 위해서 fit_transform()을 한다.
genre_mat = count_vect.fit_transform(movies_df['genres_literal'])

# 코사인 유사도를 사용
genre_sim = cosine_similarity(genre_mat, genre_mat)

# 내림차순 정렬
genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1]
np.save('test.npy',genre_sim_sorted_ind)


# 영화 선정을 위한 가중치 선정
C = movies_df['vote_average'].mean()
m = movies_df['vote_count'].quantile(0.6)

def weighted_vote_average(record):
    v = record['vote_count']
    R = record['vote_average']

    return ((v/(v+m)) * R) + ((m / (v + m)) * C)

movies_df['weighted_vote'] = movies_df.apply(weighted_vote_average, axis=1)
# movies_df.to_csv("filename.csv", mode='w')


def find_sim_movie(df, sorted_ind, title_name, top_n=10):
    title_movie = df[df['title'] == title_name]
    title_index = title_movie.index.values

    similar_indexes = sorted_ind[title_index, : (top_n * 2)]
    similar_indexes = similar_indexes.reshape(-1)

    similar_indexes = similar_indexes[similar_indexes != title_index]

    return df.iloc[similar_indexes].sort_values('weighted_vote', ascending=False)[:top_n]

similar_movies = find_sim_movie(movies_df, genre_sim_sorted_ind, 'The Godfather', 10)
similar_movies[['title', 'vote_average', 'weighted_vote']]
