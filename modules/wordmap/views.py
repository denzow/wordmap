from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, generics

from .models import Word
from .serializer import WordSerializer


def index(request):
    return render(request, 'wordmap/index.html', {})


def show_word(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    return render(request, 'wordmap/show_word.html', {
        'word_name': word.word
    })


class WordViewSet(viewsets.ModelViewSet):

    serializer_class = WordSerializer
    queryset = Word.get_all_words()


class WordFilterViewSet(generics.ListAPIView):

    serializer_class = WordSerializer

    def get_queryset(self):
        query_word = self.kwargs.get('query_word')
        if query_word:
            return Word.get_word_by_like(query_word)
        else:
            return []
