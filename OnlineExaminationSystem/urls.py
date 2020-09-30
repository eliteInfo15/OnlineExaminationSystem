"""OnlineExaminationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from OnlineExamApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('OnlineExamApp.urls')),
    path('Adminbyname/<int:id>',views.Adminbyname.as_view()),
    path('center/<str:center_name>',views.Centername.as_view()),
    path('batch/<str:batch_time>',views.Batchtime.as_view()),
    path('subcategory/<str:subcategory_name>',views.Subcategoryname.as_view()),
    path('category/<str:category_name>',views.Categorybyname.as_view())
]
