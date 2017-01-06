from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from bank.models import Bank
import datetime

#import pprint

# Create your views here.
@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Bank
    template_name = 'bank/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Bank.objects.all().filter(isdeleted=0).order_by('-pk')

    #def get_context_data(self, **kwargs):
    #    context = super(IndexView, self).get_context_data(**kwargs)
    #    context['test'] = "testlang"
    #    return context

    #pprint(get_queryset)
    #pprint.pprint(Bank.objects.all())
    #exit()

@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Bank
    template_name = 'bank/detail.html'

@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Bank
    template_name = 'bank/create.html'
    fields = ['code', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/bank')

@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = Bank
    template_name = 'bank/edit.html'
    fields = ['code', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.save()
        return HttpResponseRedirect('/bank')

@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Bank
    template_name = 'bank/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.isdeleted = 1
        self.object.status = 'I'
        self.object.save()
        return HttpResponseRedirect('/bank')