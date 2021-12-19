from django.urls import path
from . import views
#from .views import Search, OrderSearch, OrderDetailView, OrdersList, reader_new, reader_toblacklist, order_create, export_excel_all, export_excel_last_month, user_login, logout_view, BookListView, PerfOrdersList
from .views import Search, BookListView, BookDetailView, BookDetectiveView
from django.conf import settings
#from django.conf.urls import url

from django.shortcuts import redirect
from library.yasg import urlpatterns as docs 
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Lib API')


urlpatterns = [
    path('', views.index, name='index'),
    path('reader-search/', Search.as_view(), name='reader-search'),

    path(r'^books/$', views.BookListView.as_view(), name='books'),
    path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('books/detectives/', views.BookDetectiveView.as_view(), name='detective'),
    path('books/romances/', views.BookRomanView.as_view(), name='romance'),
    path('books/drama/', views.BookDramaView.as_view(), name='drama'),
    path('order/create/', views.order_create, name='order_create'),
    path('readers/', views.ReaderListView.as_view(), name='readers'),
    path('reader/(?P<pk>\d+)$', views.ReaderDetailView.as_view(), name='reader-detail'),
    path('reader/(?P<pk>\d+)$/upd/', views.ReaderUpdateView.as_view(), name='reader-update'),
    path('reader/(?P<pk>\d+)$/delete/', views.reader_delete, name='reader-delete'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/done', views.OrderDoneView.as_view(), name='orders-done'),
    path('orders/in-process', views.OrderUndoneView.as_view(), name='orders-process'),
    path('logs/', views.LogsListView.as_view(), name='logs'),
]

#urlpatterns += docs


