from django.urls import path
from . import views


urlpatterns = [
    path('review/', views.review_list_or_create),
    path('review/<int:review_pk>/', views.review_detail_or_update_delete),
    path('review/<int:review_pk>/like/', views.review_like),
    path('review/<int:review_pk>/comment/', views.create_comment),
    path('review/<int:review_pk>/comment/<int:comment_pk>/', views.comment_update_delete),
    path('review/<int:review_pk>/comment/<int:comment_pk>/like/', views.comment_like),
]