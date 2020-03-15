from django.urls import path,include
from todo import views
urlpatterns = [
    path('',views.home, name='home'),
    path('addtodo',views.add_todo),
    path('delete_todo/<int:todo_id>',views.delete_todo)
]
