"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.views.generic import TemplateView

from root import settings

def auth_redirect_all(request):
    """Redirect any auth/* URLs to home page"""
    return redirect('/')

# Custom 404 handler
handler404 = lambda request, exception=None: TemplateView.as_view(template_name='notfound.html')(request)

urlpatterns = [
                  path('admin-page/', admin.site.urls),
                  # Catch auth URLs at root level too
                  re_path(r'^auth/.*', auth_redirect_all),
                  path('', include('main.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # + debug_toolbar_urls()
