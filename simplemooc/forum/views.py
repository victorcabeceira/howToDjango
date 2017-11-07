from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Thread
# class ForumView(TemplateView):
#
#   template_name = 'forum/index.html'
class ForumView(ListView):

  model = Thread
  paginate_by = 10
  template_name = 'forum/index.html'

index = ForumView.as_view()
