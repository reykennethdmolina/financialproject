from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from chartofaccount.models import Chartofaccount
import datetime


@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Chartofaccount
    template_name = 'chartofaccount/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Chartofaccount.objects.all().filter(isdeleted=0).order_by('-pk')


# @method_decorator(login_required, name='dispatch')
# class DetailView(DetailView):
#     model = Bankbranch
#     template_name = 'bankbranch/detail.html'
#
#
@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Chartofaccount
    template_name = 'chartofaccount/create.html'
    fields = ['main', 'clas', 'item', 'cont']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.enterby = self.request.user
        self.object.modifyby = self.request.user
        self.object.save()
        return HttpResponseRedirect('/chartofaccount')
#
#
# @method_decorator(login_required, name='dispatch')
# class UpdateView(UpdateView):
#     model = Bankbranch
#     template_name = 'bankbranch/edit.html'
#     fields = ['code', 'description',
#               'bank', 'description',
#               'address', 'contact_person',
#               'contact_position', 'telephone1',
#               'telephone2', 'remarks']
#
#     def get_context_data(self, **kwargs):
#         context = super(UpdateView, self).get_context_data(**kwargs)
#         context['bank'] = Bank.objects.filter(isdeleted=0).order_by('description')
#         return context
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.modifyby = self.request.user
#         self.object.modifydate = datetime.datetime.now()
#         self.object.save()
#         return HttpResponseRedirect('/bankbranch')
#
#
# @method_decorator(login_required, name='dispatch')
# class DeleteView(DeleteView):
#     model = Bankbranch
#     template_name = 'bankbranch/delete.html'
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.modifyby = self.request.user
#         self.object.modifydate = datetime.datetime.now()
#         self.object.isdeleted = 1
#         self.object.status = 'I'
#         self.object.save()
#         return HttpResponseRedirect('/bankbranch')
