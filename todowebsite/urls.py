
from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id>/',views.update,name='update'),
    path('',views.index,name='index'),
]
# The above code defines the URL patterns for a Django web application. It includes paths for the admin interface, deleting tasks, updating tasks, and the main index page where tasks are displayed. Each path is associated with a specific view function in the `views` module of the `todoapp` application.