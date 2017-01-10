from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, Http404
from . models import Wtax
import datetime


@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Wtax
    template_name = 'wtax/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Wtax.objects.all().filter(isdeleted=0).order_by('-pk')


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Wtax
    template_name = 'wtax/detail.html'


@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Wtax
    template_name = 'wtax/create.html'
    fields = ['code', 'description', 'rate', 'wtaxtype_id', 'wtaxchartofaccount_id']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('wtax.add_wtax'):
            raise Http404
        return super(CreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/wtax')


@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = Wtax
    template_name = 'wtax/edit.html'
    fields = ['code', 'description', 'rate', 'wtaxtype_id', 'wtaxchartofaccount_id']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('wtax.change_wtax'):
            raise Http404
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.save()
        return HttpResponseRedirect('/wtax')


@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Wtax
    template_name = 'wtax/delete.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('wtax.delete_wtax'):
            raise Http404
        return super(DeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.isdeleted = 1
        self.object.status = 'I'
        self.object.save()
        return HttpResponseRedirect('/wtax')
