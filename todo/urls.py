from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.index, name='index'),
    path('add',views.addtodo, name='add'),
    path('completed/<todo_id>',views.completedtodo,name='completed'),
    path('deletecompleted',views.deletecompleted,name='deletecompleted'),
    path('deleteall',views.deleteall,name='deleteall'),
]
