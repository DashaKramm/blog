from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer, CommentSerializer
from webapp.models import Article, Comment


# Create your views here.
@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET'])


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            article = get_object_or_404(Article, pk=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            articles = Article.objects.order_by('-created_at')
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_data = ArticleSerializer(article).data
        return Response(article_data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_data = ArticleSerializer(article).data
        return Response(article_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({'pk': pk}, status=status.HTTP_204_NO_CONTENT)


class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        article_id = kwargs.get('article_id')
        if pk:
            comment = get_object_or_404(Comment, pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif article_id:
            article = get_object_or_404(Article, pk=article_id)
            comments = Comment.objects.filter(article=article)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, article_id, **kwargs):
        article = get_object_or_404(Article, pk=article_id)
        data = request.data.copy()
        data['article'] = article.id
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        comment_data = CommentSerializer(comment).data
        return Response(comment_data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, pk, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(data=request.data, instance=comment)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        comment_data = CommentSerializer(comment).data
        return Response(comment_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, pk, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({'pk': pk}, status=status.HTTP_204_NO_CONTENT)
