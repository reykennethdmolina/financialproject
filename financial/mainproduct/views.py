from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from mainproduct.models import Mainproduct
import datetime

#import pprint

# Create your views here.
@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Mainproduct
    template_name = 'mainproduct/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Mainproduct.objects.all().filter(isdeleted=0).order_by('-pk')

@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Mainproduct
    template_name = 'mainproduct/detail.html'

@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Mainproduct
    template_name = 'mainproduct/create.html'
    fields = ['code', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/mainproduct')

@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = Mainproduct
    template_name = 'mainproduct/edit.html'
    fields = ['code', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.save()
        return HttpResponseRedirect('/mainproduct')

@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Mainproduct
    template_name = 'mainproduct/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.isdeleted = 1
        self.object.status = 'I'
        self.object.save()
        return HttpResponseRedirect('/mainproduct')