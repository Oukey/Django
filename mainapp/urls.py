from django.urls import path

import mainapp.views as mainapp

app_neme = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='cetegory'),
]