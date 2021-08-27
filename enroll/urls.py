from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_show, name = "add_show" ),    
    path('delete/<int:id>/',views.Delete_data, name = "deletedata" ),    
    path('update/<int:id>/',views.Update_data, name = "updatedata" ),    
]