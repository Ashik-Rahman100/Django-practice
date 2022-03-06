from django.urls import path

from . import views

urlpatterns = [
    path('fessdj/', views.fees_django),
    path('feespy/', views.fees_python),
    
]
