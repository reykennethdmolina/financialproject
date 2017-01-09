from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from adtype.models import Adtype
import datetime


@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Adtype
    template_name = 'Adtype/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Adtype.objects.all().filter(isdeleted=0).order_by('-pk')


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Adtype
    template_name = 'adtype/detail.html'


@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Adtype
    template_name = 'adtype/create.html'
    fields = ['code', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/adtype')


@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = Adtype
    template_name = 'adtype/edit.html'
    fields = ['code', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.save()
        return HttpResponseRedirect('/adtype')


@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Adtype
    template_name = 'adtype/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.isdeleted = 1
        self.object.status = 'I'
        self.object.save()
        return HttpResponseRedirect('/adtype')
