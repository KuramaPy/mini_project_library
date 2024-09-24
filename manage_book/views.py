from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import book
from .forms import TaskForm


class TaskListView(ListView):
    model = book
    template_name = 'task_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        price = self.request.GET.get('price')
        publication_date = self.request.GET.get('publication_date')
        
        if price:
            queryset = queryset.filter(price__lte=price)  
        if publication_date:
            queryset = queryset.filter(year_publication=publication_date)  
        
        return queryset
    
def delete_filtered_books(request):
    if request.method == "POST":
        price = request.POST.get('price')
        publication_date = request.POST.get('publication_date')

        # Fetch filtered books
        filtered_books = book.objects.all()
        if price:
            filtered_books = filtered_books.filter(price__lte=price)
        if publication_date:
            filtered_books = filtered_books.filter(year_publication=publication_date)

        # Delete the filtered books
        filtered_books.delete()

        # Redirect to the task list page after deletion
        return redirect('manage_book:task_list')

class TaskDetailView(DetailView):
    model = book
    template_name = 'task_detail.html'

class TaskCreateView(CreateView):
    model = book
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('manage_book:task_list')

class TaskUpdateView(UpdateView):
    model = book
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('manage_book:task_list')

class TaskDeleteView(DeleteView):
    model = book
    template_name = 'task_confirm_delete.html'
    
    def get_success_url(self):
        # Redirect to the list view after deletion
        return self.request.META.get('HTTP_REFERER', reverse_lazy('manage_book:task_list'))
"""
class manage_book_veiw:
    def create():
        pass
    def update():
        pass
    def delete():
        pass
    def list_books():
        pass
    def get():
        pass
# Create your views here.
"""