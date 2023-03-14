
from django.contrib import admin
from django.urls import path
from api.views import get_student,get_contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',get_student),
    path('contact/',get_contact)
]
