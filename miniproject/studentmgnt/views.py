from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_control
from django.views.generic import CreateView, ListView, TemplateView, UpdateView ,DeleteView
from django.views.generic.base import TemplateView
from .models import Student,Course
from django.http import JsonResponse

# Create your views here.



@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class SignInView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if 'username' in request.session:
            return redirect('admin_home')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user is not None and user.is_superuser:
            request.session['email'] = email
            login(request, user)
            return redirect('admin_home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('signin')



class HomeView(TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     if 'username' in request.session:
    #         return render(request, self.template_name)
    #     else:
    #         return redirect('signin')
    

# class StudentView(TemplateView):
#     template_name = 'student/student.html'    


class StudentListView(ListView):
    model = Student
    template_name = 'student/liststudent.html'
    context_object_name = 'students'
    ordering = ['-created_at']

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student/student.html'
    fields = ['Studentname', 'studentemail', 'phone', 'address','created_at']
    success_url = reverse_lazy('StudentListView')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['Studentname', 'studentemail', 'phone', 'address']
    success_url = reverse_lazy('StudentListView')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

# -----------------course-------------------------


class CourseListView(ListView):
    model = Course
    template_name = 'course/listcourse.html'
    context_object_name = 'courses'
    ordering = ['-created_at']


class CourseCreateView(CreateView):
    model = Course
    template_name = 'course/course.html'
    fields = ['coursename', 'code', 'description', 'created_at']
    success_url = reverse_lazy('CourseListView')


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_form.html'
    fields = ['coursename', 'code', 'description', 'created_at']
    success_url = reverse_lazy('CourseListView')