from django.urls import path
from .views import *



urlpatterns = [
    path('', SignInView.as_view(), name='signin'),
    path('index', HomeView.as_view(), name='index'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
 

]
