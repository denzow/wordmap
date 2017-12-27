from django.shortcuts import render

from rest_framework import viewsets, generics

from .models import Word
from .serializer import WordSerializer


def index(request):
    return render(request, 'wordmap/index.html', {})


class WordViewSet(viewsets.ModelViewSet):

    serializer_class = WordSerializer
    queryset = Word.get_all_words()


class WordFilterViewSet(generics.ListAPIView):

    serializer_class = WordSerializer

    def get_queryset(self):
        query_word = self.kwargs['query_word']
        return Word.get_word_by_like(query_word)
