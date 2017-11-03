from django.db import models
from django.conf import settings

from taggit.managers import TaggableManager


class Thread(model.Model):

  title = models.CharField('Título', max_length=100)
  body = models.TextField('Mensagem')
  author = models.ForeignKey(
    #AUTH_USER_MODEL because a custom user model is being used
    settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='threads'
  )
  views = models.IntegerField('Visualizações', blank=True, default=0)
  answers = models.IntegerField('Respostas', blank=True, default=0)

  tags = TaggableManager()

  created_at = models.DateTimeField('Criado em ', auto_now_add = True)
  updated_at = models.DateTimeField('Atualizado em ', auto_now = True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name='Tópico'
    verbose_name_plural='Tópicos'
    ordering = ['-modified']

class Reply(models.Model):

  reply = models.TextField('Resposta')
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='threads'
  )
  correct = models.BooleanField('Correta?', blank=True, default=False)

  created_at = models.DateTimeField('Criado em ', auto_now_add = True)
  updated_at = models.DateTimeField('Atualizado em ', auto_now = True)

  def __str__(self):
    return self.reply[:100]

  def Meta:
    verbose_name: 'Resposta'
    verbose_name_plural: 'Respostas'
    ordering: ['-correct', 'created_at']
