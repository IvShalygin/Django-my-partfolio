"""personal_partfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView
from django.utils.translation import gettext_lazy as _

# Адміністрацыйная панэль за межамі i18n_patterns (без прэфікса мовы)
urlpatterns = [
    path('admin/', admin.site.urls),  # Адміністрацыйная панэль без моўнага прэфікса

    # Дадаем шлях для змены мовы
    path('i18n/', include('django.conf.urls.i18n')),  # Правильный путь для смены языка
]

# Іншыя шляхі з падтрымкай лакалізацыі
urlpatterns += i18n_patterns(
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('vba/', views.home_vba, name='home_vba'),
    path('my_django/', views.my_django, name='my_django'),
    path('syst/', views.syst, name='syst'),
)

# Даданне статычных файлаў
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)