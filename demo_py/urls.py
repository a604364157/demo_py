"""demo_py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from web.views import say_hello, show_students, show_real_students, run_two_color_ball, run_big_lotto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayHello/', say_hello),
    path('showStudents/', show_students),
    path('showRealStudents/', show_real_students),
    path('runBall', run_two_color_ball),
    path('runLotto', run_big_lotto),
]
