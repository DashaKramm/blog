from rest_framework import serializers

from webapp.models import Tag
from webapp.models.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'status', 'tags', 'created_at', 'updated_at', 'author']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        article = Article.objects.create(**validated_data)
        article.tags.set(tags)
        return article

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', [])
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        instance.tags.set(tags)
        return instance
