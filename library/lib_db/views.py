from django.shortcuts import render
from .models import Book, Order, Reader, Genre, BooktableLogs, ReadertableLogs
from django.db.models import Q
from django.views.generic import ListView, DetailView, UpdateView
from django.http import Http404, HttpResponse
from .forms import OrderForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    # Доступные книги (статус = 'a')
    books = Book.objects.all()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        {'num_books':num_books,'book_list': books,},
    )

class Search(ListView):
    """Поиск читателя"""
    model = Reader
    template_name = 'reader_list.html'
    
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Reader.objects.filter(
            Q(fio__contains=query)
        )
        order_list = Order.objects.filter(
            Q(order_id__iexact=query)
        )

        
        if order_list:
            return order_list

        elif object_list:
            return object_list

class BookListView( ListView):
    model = Book
    context_object_name = 'book_list'  
    queryset = Book.objects.all()
    template_name = 'books.html' 


class BookDetailView(DetailView):
    model = Book
    def book_detail_view(request,pk):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
       
        return render(
        request,
        'book_detail.html',
        {'book':book_id, },
    )

class BookDetectiveView(ListView):
    model = Book
    context_object_name = 'book_list'  
    queryset = Book.objects.filter(genre = 1)
    template_name = 'books_genres.html' 

class BookRomanView(ListView):
    model = Book
    context_object_name = 'book_list'  
    queryset = Book.objects.filter(genre = 2)
    template_name = 'books_genres.html' 

class BookDramaView(ListView):
    model = Book
    context_object_name = 'book_list'  
    queryset = Book.objects.filter(genre = 3)
    template_name = 'books_genres.html'

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            new_order = Order()
            new_order = order
            numfromhere = Order.objects.last()
            num = int(numfromhere.order_id)
            num = num+1
            new_order.order_id = str(num)
            new_order.return_mark = False
            new_order.save()
        return redirect('index')
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'form': form}) 

class ReaderListView( ListView):
    model = Reader
    context_object_name = 'reader_list'  
    queryset = Reader.objects.all()
    template_name = 'readers.html' 


class ReaderDetailView(DetailView):
    model = Reader
    def reader_detail_view(request,pk):
        try:
            id=Reader.objects.get(pk=pk)
        except Reader.DoesNotExist:
            raise Http404("Reader does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
       
        return render(
        request,
        'reader_detail.html',
        {'reader': id, },
    )

#def reader_edit(request, id):
#    try:
#        person = Reader.objects.get(id=id)
# 
#        if request.method == "POST":
#            person.name = request.POST.get("fio")
#            person.age = request.POST.get("phone")
#            person.save()
#            return redirect('index')
#        else:
#            return render(request, "reader_edit.html", {"person": person})
#    except Reader.DoesNotExist:
#        raise Http404("Reader does not exist")


class ReaderUpdateView(UpdateView):
    model = Reader
    template_name = 'reader_edit.html'
    fields = ['fio', 'phone']


def reader_delete(request, pk):
    try:
        person = Reader.objects.get(pk=pk)
 
        if request.method == "POST":
            person.delete()
            return redirect('readers')
        else:
            return redirect('index')
    except Reader.DoesNotExist:
        raise Http404("Reader does not exist")


class OrderListView( ListView):
    model = Order
    context_object_name = 'order_list'  
    queryset = Order.objects.all()
    template_name = 'orders.html' 


class OrderDetailView(DetailView):
    model = Reader
    def order_detail_view(request,pk):
        try:
            id=Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404("Order does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
       
        return render(
        request,
        'order_detail.html',
        {'order': id, },
    )

class OrderDoneView(ListView):
    model = Order
    context_object_name = 'order_list'  
    queryset = Order.objects.filter(return_mark = True)
    template_name = 'orders.html' 
    
class OrderUndoneView(ListView):
    model = Order
    context_object_name = 'order_list'  
    queryset = Order.objects.filter(return_mark = False)
    template_name = 'orders.html' 


class LogsListView(ListView):
    model = ReadertableLogs
    context_object_name = 'logs_list'  
    queryset = ReadertableLogs.objects.all()
    template_name = 'logs.html' 