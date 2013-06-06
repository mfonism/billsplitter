from django.conf.urls import patterns, url

from expenses.views import *

urlpatterns = patterns('',
	url(r'^groups/$', GroupList.as_view(), name='group_list'),
	url(r'^groups/add/$', GroupCreate.as_view(), name='group_create'),
	url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdate.as_view(), name='group_update'),
	url(r'^groups/(?P<pk>\d+)/delete/$', GroupDelete.as_view(), name='group_delete'),

	url(r'^(?P<group>\d+)/expenses/$', ExpenseList.as_view(), name='expense_list'),
	url(r'^(?P<group>\d+)/expenses/add/$', ExpenseCreate.as_view(), name='expense_create'),
	url(r'^(?P<group>\d+)/expenses/(?P<pk>\d+)/edit/$', ExpenseUpdate.as_view(), name='expense_update'),
	url(r'^(?P<group>\d+)/expenses/(?P<pk>\d+)/delete/$', ExpenseDelete.as_view(), name='expense_delete'),

	url(r'^(?P<group>\d+)/refund/add/$', RefundCreate.as_view(), name='refund_create'),
	url(r'^(?P<group>\d+)/refund/add/(?P<pk>\d+)/delete/$', RefundDelete.as_view(), name='refund_delete'),
)