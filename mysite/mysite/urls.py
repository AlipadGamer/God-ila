"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from myapp.views import main
from myapp.views import pozdrav
from myapp.views import article_main
from myapp.views import article_uniq
from myapp.views import article
from myapp.views import mypage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main,name='main'),
    path('ahoj/',pozdrav,name='pozdrav'),
    path('article/',article_main),
    path('article/5',article_uniq),
    path('article/<int:article_id>/',article),
    path('article/<int:article_id>/<slug:name>',article),
    path('cau/',mypage,name='mypage'),
    path('',mypage,)

   

]

