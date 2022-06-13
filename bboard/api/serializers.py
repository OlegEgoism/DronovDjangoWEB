from rest_framework import serializers
from main.models import Bb, Comment

"""Формирование списка объявлений"""
class BbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ('id', 'title', 'content', 'price', 'created_at')


"""Сведения о выбранном объявлении"""
class BbDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ('id', 'title', 'content', 'price', 'created_at', 'contacts', 'image')


"""Вывод и добавление комментариев"""
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('bb', 'author', 'content', 'created_at')