from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib import messages

from .models import Thread
from .forms import ReplyForm

# class ForumView(TemplateView):
#
#   template_name = 'forum/index.html'
class ForumView(ListView):

  model = Thread
  paginate_by = 5
  template_name = 'forum/index.html'

  def get_queryset(self):
    queryset = Thread.objects.all()
    order = self.request.GET.get('order', '')
    if order == 'views':
      queryset = queryset.order_by('-views')
    elif order == 'answers':
      queryset = queryset.order_by('-answers')
    tag = self.kwargs.get('tag', '')
    if tag:
      queryset = queryset.filter(tags__slug__icontains=tag)
    return queryset

  def get_context_data(self, **kwargs):
    context = super(ForumView, self).get_context_data(**kwargs)
    context['tags'] = Thread.tags.all()
    return context

class ThreadView(DetailView):

  model = Thread
  template_name = 'forum/thread.html'

  def get_context_data(self, **kwargs):
    context = super(ThreadView, self).get_context_data(**kwargs)
    context['tags'] = Thread.tags.all()
    context['form'] = ReplyForm(self.request.POST or None)
    return context

  def post(self, request, *args, **kwargs):
    if not self.request.user.is_authenticated():
      messages.error(
        self.request, 'Para responder ao tópico, é necessário estar logado.'
      )
      return redirect(self.request.path)
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)
    form = context['form']
    if form.is_valid():
      reply = form.save(commit=False)
      reply.thread = self.object
      reply.author = self.request.user
      reply.save()
      messages.success(
        self.request, 'Resposta enviada com sucesso!'
      )
      context['form'] = ReplyForm()
    return self.render_to_response(context)


index = ForumView.as_view()
thread = ThreadView.as_view()
