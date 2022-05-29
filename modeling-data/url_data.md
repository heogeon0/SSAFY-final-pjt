## App movies   : ‘movies/’

#### serve to client

### Home : home/(GET)

movies data

movies : [    {
      "adult": bool,
      "backdrop_path": char,
      "original_language": "char",
      "overview": "text",
      "popularity": float,
      "poster_path": "char",
      "release_date": "date-time",
      "title": "char",
      "vote_average": float,

​		"genres" : array

​		"is_active" : bool

}]

#### client to server

token



### 영화 추천 : recommendation/ (GET )

#### client to server

세개 이상의 movie_id 전달, token

#### serve to client

movies data

movies : [    {
      "adult": bool,
      "backdrop_path": char,
      "original_language": "char",
      "overview": "text",
      "popularity": float,
      "poster_path": "char",
      "release_date": "date-time",
      "title": "char",
      "vote_average": float,

​		"genres" : array

​		"is_active" : bool

}]

### about : about/

none(front 내에서 구현)



## App  account   :  ‘account/’



### login : login/ (POST)

#### client to server

accounts: [{

password: char,

username: char,

}]

### serve to client

token





### signup : signup/ (POST)

#### client to server

accounts: [{

username: char,

password: char,

}]

### serve to client

token



### logout : logout/ (POST)

#### client to server

token

### serve to client

none





### signup : signup/ (POST)

#### client to server

accounts: [{

username: char,

password1: char,

password2: char,

}]

### serve to client

token





### currentUserInfo : user/ (GET)

#### client to server

token

### serve to client

user





## App community   :  ‘communitys/’

### review : review/	(GET)

#### client to server

token

### serve to client

{review_id : integer,
   user_id : integer,

​	title : char,

​	movie_title : char

​	score : Interger

​    created_at : datetime,

 }



### review-create :review/(POST)

#### client to server

token

{  
    title : char,

​	content : text,

​	movie_title : char

​	score : Interger

}

### serve to client

{review_id : integer,
   user_id : integer,

​	title : char,

​	content : text,

​	movie_title : char

​	score : Interger

​    created_at : datetime,

​	updated_at : datetime

 }



### review-detail : review/<int: article_pk>/	(GET)

#### client to server

token, article_pk



### serve to client

{review_id : integer,
   user_id : integer,

​	title : char,

​	content : text,

​	movie_title : char

​	score : Interger

​    created_at : datetime,

​	updated_at : datetime

 }

 review_like : {
       review_like_id : integer,
       user_id : integer
    }

  comment : {
       comment_id : integer,
       review_id : integer,
       content : text,
   },



### review-delete: review/<int: article_pk>/	(DELETE)

#### client to server

token, article_pk



### serve to client

none



### review-update: review/<int: article_pk>/	(PUT)

#### client to server

token, article_pk

{	title : char,

​	content : text,

​	movie_title : char

​	score : Interger

 }

### serve to client

{review_id : integer,
   user_id : integer,
    created_at : date_time,

​	updated_at : date_time

​    title : char

​	content : text

  }





### comment-create: review/<int: article_pk>/comment/	(POST)

#### client to server

token, article_pk

{  
	content : text

}

### serve to client

{  

​	user_id : int

​	content : text

​	article_id : int

​	created_at : datetime

​	update_at : datetime

}



### comment-update: review/<int: article_pk>/comment/<int: comment_pk>/	(PUT)

#### client to server

token, article_pk, comment_pk

{  
	content : text

}



### serve to client

{  

​	user_id : int

​	content : text

​	article_id : int

​	created_at : datetime

​	update_at : datetime

}



### comment-delete: review/<int: article_pk>/comments/<int: comment_pk>/	(DELETE)

#### client to server

token, article_pk, comment_pk

### serve to client

none