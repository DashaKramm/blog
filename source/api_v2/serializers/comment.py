from rest_framework import serializers

from webapp.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'article', 'text', 'created_at', 'updated_at', 'author']
        read_only_fields = ['id', 'article', 'created_at', 'updated_at', 'author']
