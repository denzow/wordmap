# coding: utf-8

from rest_framework import serializers

from .models import Word, Category


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        exclude = []
