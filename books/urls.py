from django.urls import path,include
from books.views import *

urlpatterns = [
    path('', BooksList.as_view(), name='list'),
    path('add/', AddBook.as_view(), name='add'),
    path('detail/<int:pk>/', BookDetail.as_view(), name='detail'),
    path('edit/<int:pk>/', EditBook.as_view(), name='edit'),
    path('delete/<int:pk>/', DeleteBook.as_view(), name='delete'),
    path('api/', include('books.api.urls')), # API URLs
]
