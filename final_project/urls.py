"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from final_app.views import homepage, login_page, register_page, login_view, register_view, suggest_course, preferences # TODO
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView # TODO


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', homepage, name='home'), # TODO
    path('login/', login_view, name='login'), # TODO
    path('register/', register_view, name='register'), # TODO
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), # TODO
    path('suggest_course/', suggest_course, name='suggest_course'), # TODO
    path('preferences/', preferences, name='preferences'), # TODO
    # path('items/', item_view, name='item_view')
]\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
