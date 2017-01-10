from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import datetime


class Bankaccount(models.Model):
    code = models.CharField(max_length=10, unique=True)
    bank = models.ForeignKey('bank.Bank', default=0, related_name='bank_id', validators=[MinValueValidator(1)])
    bankbranch_id = models.IntegerField(default=0)
    bankaccounttype = models.ForeignKey('bankaccounttype.Bankaccounttype', default=0, related_name='bankaccounttype_id',
                                        validators=[MinValueValidator(1)])
    currency = models.ForeignKey('currency.Currency', default=0, related_name='currency_id', validators=[MinValueValidator(1)])
    chartofaccount_id = models.IntegerField(null=True)
    accountnumber = models.CharField(max_length=30)
    remarks = models.CharField(max_length=250, null=True)
    beg_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    beg_code = models.CharField(max_length=1, null=True)
    beg_date = models.DateField(null=True)
    run_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    run_code = models.CharField(max_length=1, null=True)
    run_date = models.DateField(null=True)
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('C', 'Cancelled'),
        ('O', 'Posted'),
        ('P', 'Printed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    enterby = models.ForeignKey(User, default=1, related_name='bankaccount_enter')
    enterdate = models.DateTimeField(auto_now_add=True)
    modifyby = models.ForeignKey(User, default=1, related_name='bankaccount_modify')
    modifydate = models.DateTimeField(default=datetime.datetime.now())
    isdeleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'bankaccount'
        ordering = ['-pk']
        permissions = (("view_bankaccount", "Can view bankaccount"),)

    def get_absolute_url(self):
        return reverse('bankaccount:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    def status_verbose(self):
        return dict(Bankaccount.STATUS_CHOICES)[self.status]