from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from inputvattype.models import Inputvattype
import datetime


@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
<<<<<<< HEAD:financial/bank/views.py
    model = Bank
    template_name = 'bank/index.html'
=======
    model = Inputvattype
    template_name = 'inputvattype/index.html'
>>>>>>> refs/remotes/origin/xtrap029-patch-1:financial/inputvattype/views.py
    context_object_name = 'data_list'

    def get_queryset(self):
        return Inputvattype.objects.all().filter(isdeleted=0).order_by('-pk')


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
<<<<<<< HEAD:financial/bank/views.py
    model = Bank
    template_name = 'bank/detail.html'

@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Bank
    template_name = 'bank/create.html'
=======
    model = Inputvattype
    template_name = 'inputvattype/detail.html'


@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Inputvattype
    template_name = 'inputvattype/create.html'
>>>>>>> refs/remotes/origin/xtrap029-patch-1:financial/inputvattype/views.py
    fields = ['code', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/inputvattype')


@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
<<<<<<< HEAD:financial/bank/views.py
    model = Bank
    template_name = 'bank/edit.html'
=======
    model = Inputvattype
    template_name = 'inputvattype/edit.html'
>>>>>>> refs/remotes/origin/xtrap029-patch-1:financial/inputvattype/views.py
    fields = ['code', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.save()
<<<<<<< HEAD:financial/bank/views.py
        return HttpResponseRedirect('/bank')

@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Bank
    template_name = 'bank/delete.html'
=======
        return HttpResponseRedirect('/inputvattype')


@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Inputvattype
    template_name = 'inputvattype/delete.html'
>>>>>>> refs/remotes/origin/xtrap029-patch-1:financial/inputvattype/views.py

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.isdeleted = 1
        self.object.status = 'I'
        self.object.save()
        return HttpResponseRedirect('/inputvattype')
