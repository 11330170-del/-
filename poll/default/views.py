from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView,DetailView,RedirectView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def poll_list(req):
    polls=Poll.objects.all()
    return render(req,"default/list.html",{'poll.list':polls,'msg':'hello!'})

class PollList(ListView):
    model=Poll

    #應用程式名稱/資料模型_list.html
    #default/poll_list.html

class PollView(DetailView):
        model=Poll

        def get_context_data(self,**kwargs):
             ctx=super().get_context_data(**kwargs)
             option_list=Option.object.filter(poll_id=self.object.id)
             return ctx

class pollvote(RedirectView):
    # redirectview_url="https://www.google.com"

    def get_redirect_url(self, *args, **kwargs):
         option=Option.objects.get(id=self.kwargs['oid'])
         option.votes+=1
         option.save()
         return reverse("poll_view",args=[option.poll_id])
    
class pollcreate(CreateView):
     model=Poll
     fields='__all__'


class PollEdit(UpdateView):
    model=Poll
    fields='__all__'
    def get_success_url(self):
          return reverse_lazy('poll_list') 

class optioncreate(CreateView):
     model=Option
     fields=['title']

     def form_valid(self, form):
          form.instance.poll_id=self.kwargs['pid']
          return super().form_valid(form)
     def get_success_url(self):
          return reverse_lazy('poll_view',kwargs={'pk':self.kwargs['pid']})

class optionedit():
     pass

class polldelete(DeleteView):
          model=Poll
          success_url=reverse_lazy('poll_list')

class optiondelete(DeleteView):
     model=Option

     def get_success_url(self):
          return reverse_lazy('poll_view',kwargs={'pk'})