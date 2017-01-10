from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, Http404
from module.models import Module
from mainmodule.models import Mainmodule
import datetime


@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Module
    template_name = 'module/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Module.objects.all().filter(isdeleted=0).order_by('-pk')


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Module
    template_name = 'module/detail.html'


@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Module
    template_name = 'module/create.html'
    fields = ['code', 'description', 'mainmodule', 'name', 'segment']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('module.add_module'):
            raise Http404
        return super(CreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['mainmodule'] = Mainmodule.objects.filter(isdeleted=0).order_by('description')
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/module')


@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = Module
    template_name = 'module/edit.html'
    fields = ['code', 'description', 'mainmodule', 'name', 'segment']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('module.change_module'):
            raise Http404
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['mainmodule'] = Mainmodule.objects.filter(isdeleted=0).order_by('description')
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.save()
        return HttpResponseRedirect('/module')


@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Module
    template_name = 'module/delete.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('module.delete_module'):
            raise Http404
        return super(DeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.modifyby = self.request.user
        self.object.modifydate = datetime.datetime.now()
        self.object.isdeleted = 1
        self.object.status = 'I'
        self.object.save()
        return HttpResponseRedirect('/module')
