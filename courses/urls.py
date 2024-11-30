from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("create/", views.create_course, name="create_course"),
    path("<int:course_id>/enroll/", views.enroll_course, name="enroll_course"),
]
