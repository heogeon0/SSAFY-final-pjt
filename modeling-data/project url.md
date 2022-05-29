project url



movies :  ‘movies/’

community :  ‘communitys/’

account :  ‘accounts/’



name | router  |  url



NotFound404 | '/404' | 없음

about | '/about' | 없음



accounts/

login  |  '/login'  | 'login/'

logout  |  '/logout  '  | 'logout  /'

signup|  '/signup'  | 'signup/'

currentUserInfo  |  없음  | 'user/'



movies/

home  |  '/'  | '/'  	=> 	movie_list와 movie 디테일이 들어갈 곳

movieRecommend | '/recommend' | 'recommend/'



communitys/



reviews| '/reviews' | 'review/'    GET

reviewNew| '/reviews/new' | 'review/'   POST

review| '/reviews/:articlePk' | 'review/<<int:review_pk>>/'  GET

reviewEdit| '/reviews/:articlePk/edit' | 'review/<<int:review_pk>>/'   PUT

reviewDelete | '' | 'review/<<int:review_pk>>/  DELETE'

likeReview| '' | 'review/<<int:review_pk>>/like/'



---

django 위주

create_comment | '' | 'review/<<int:review_pk>>/comment/'

comment_update_or_delete | '' | 'review/<<int:review_pk>>/comment/<<int:comment_pk>>'

---

front 위주

front에서 comments를 불러 올 때는 역참조 하기!!

createComment |'' | 'review/<<int:review_pk>>/comment/'	POST

updateComment | '' | 'review/<<int:review_pk>>/comment/<<int:comment_pk>>'	PUT

deleteComment |  '' | 'review/<<int:review_pk>>/comment/<<int:comment_pk>>'	DELETE

 



