from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from .models import Word
from .serializer import WordSerializer


def index(request):
    return render(request, 'wordmap/index.html', {})


class WordViewSet(viewsets.ModelViewSet):

    queryset = Word.objects.all()
    serializer_class = WordSerializer
