from django.urls import path, include
from .views import BookMListView, BookMCreateView, BookmDetailView, BookmUpdateView, BookmDeleteView

urlpatterns = [
    path('', BookMListView.as_view(), name='list'),
    path('create/', BookMCreateView.as_view(), name='create'),
    path('detail/<int:pk>', BookmDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmDeleteView.as_view(), name='delete'),

]
