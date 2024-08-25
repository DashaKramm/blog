from django.urls import path

from api_v2.views import ArticleView, CommentView

app_name = 'api_v2'

urlpatterns = [
    path('articles/', ArticleView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleView.as_view(), name='article'),
    path('articles/<int:article_id>/comments/', CommentView.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentView.as_view(), name='comment'),
]
