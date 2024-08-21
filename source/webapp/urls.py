from django.urls import path

from webapp.views import UpdateArticleView, DeleteArticleView, ArticleListView, CreateArticleView, \
    ArticleDetailView, CreateCommentView, UpdateCommentView, DeleteCommentView, LikeArticleView, UnlikeArticleView, \
    LikeCommentView, UnlikeCommentView
from webapp.views.api import index

app_name = 'webapp'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('create/', CreateArticleView.as_view(), name='create_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/update/', UpdateArticleView.as_view(), name='update_article'),
    path('article/<int:pk>/delete/', DeleteArticleView.as_view(), name='delete_article'),
    path('article/<int:pk>/comment/create/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/update/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
    path('article/<int:pk>/like/', LikeArticleView.as_view(), name='like_article'),
    path('article/<int:pk>/unlike/', UnlikeArticleView.as_view(), name='unlike_article'),
    path('comment/<int:pk>/like/', LikeCommentView.as_view(), name='like_comment'),
    path('comment/<int:pk>/unlike/', UnlikeCommentView.as_view(), name='unlike_comment'),
    path('', index, name='index'),
]
