from django.urls import path

from ee393_project import views

urlpatterns = [path("", views.index, name="index"),path("basic", views.basic, name="basic"),path("trigonometry", views.trigonometry, name="trigonometry"),path("complex", views.complex, name="complex"),path('solve',views.solve,name="solve")
,path('setFunc',views.setFunc,name="setFunc"),]

