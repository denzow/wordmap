from django.contrib.auth.models import User
from django.db import models


class Word(models.Model):

    word = models.CharField(verbose_name='単語名', max_length=255, unique=True, blank=False, null=False)
    description = models.TextField(verbose_name='説明')
    category = models.ManyToManyField('Category', verbose_name='カテゴリ')
    updated_at = models.DateTimeField(verbose_name='最終更新日', null=False, blank=False, auto_now=True)
    creator = models.ForeignKey(User, verbose_name='作成者', related_name='created_words')
    last_editor = models.ForeignKey(User, verbose_name='最終更新者', related_name='last_edited_words')

    def __str__(self):
        return '{}: {}'.format(self.id, self.word)


class Category(models.Model):

    category_name = models.CharField(verbose_name='カテゴリ名', max_length=255, primary_key=True)
    parent_category = models.ForeignKey('self', verbose_name='親カテゴリ', blank=True, null=True)

    def __str__(self):
        if self.parent_category:
            return '{}/{}'.format(self.parent_category, self.category_name)
        else:
            return '/{}'.format(self.category_name)

