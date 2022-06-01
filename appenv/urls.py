
from.import views
from django.urls import path

urlpatterns = [
    path('new',views.test,name='my name'),
    path('second',views.test1, name="second"),
    
]