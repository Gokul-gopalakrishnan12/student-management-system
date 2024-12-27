"""
URL configuration for student_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("student_register",views.register,name="register"),
    path("logins",views.logins,name="logins"),
    path("admin_",views.admin,name="admin"),
    path("studenthome",views.studenthome,name="studenthome"),
    path("teacherhome",views.teacherhome,name="teacherhome"),
    path("teacher_register",views.teacher_register,name="teacher_register"),
    path("a_add_teacher",views.teacher_register,name="teacher_register"),
    path("a_view_teacher",views.teacher_view,name="teacher_view"),
    path("a_view_student",views.view_student,name="view_student"),
    # path("a_logout",views.a_logout,name="a_logout"),
    # path("s_studentedit",views.studentedit,name="studentedit"),
    path("s_view_teacher",views.student_view_teacher,name="student_view_teacher"),
    path("view_student",views.view_student,name="view_student"),
    path("approve/<int:id>",views.approve,name="approve"),
    path("delete_student/<int:id>",views.delete_student,name="delete_student"),
    path("delete_teacher/<int:id>",views.delete_teacher,name="delete_teacher"),
    path("t_view_student",views.teacher_view_student,name="teacher_view_student"),
    path("t_edit_teacher",views.edit_teacher,name="edit_teacher"),
    path("update_teacher/<int:id>",views.update_teacher,name="update_teacher"),
    path("s_student_edit",views.edit_student,name="edit_student"),
    path("update_student/<int:id>",views.update_student,name="update_student"),
    path("logout",views.logouts,name="logouts"),
    path("new",views.new,name="new")



]

