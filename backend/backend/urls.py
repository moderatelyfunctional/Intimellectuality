"""backend URL Configuration

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
from django.urls import path

import me_auth.views
import me_user.views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns.extend([
	path('signup', me_auth.views.signup),
	path('login', me_auth.views.login)
])

urlpatterns.extend([
    path('create_post', me_user.views.create_post),
    path('fetch_posts', me_user.views.fetch_posts),
    path('fetch_profile', me_user.views.fetch_profile),
    path('update_profile', me_user.views.update_profile)
])
