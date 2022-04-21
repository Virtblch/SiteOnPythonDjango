"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
#from django.conf.urls import url
from django.views.static import serve
from linuxbash.views import index_page, category_page, post_page

# Проверка URL на соответствие формату, при совпадении переход в соответствующую функцию views.py
urlpatterns = [
    # Загруженные через админку файлы.
    # В более древних версиях Django при ошибке заменить "re_path" на "url"
    re_path(r'^static/files/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # Стили
    re_path(r'^static/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    # Админка
    path('admin/', admin.site.urls),
    # Главная страница
    path('', index_page),
    # Подкатегория. Если url подходит по маске, с помощью переменной subCateg передаем часть url в view.
    # В данном случае там подкатегория.
    # Пример: /mtext/
    path('<slug:subCateg>/', category_page),
    # Пост
    # Пример: /mtext/101-cuneiform.html
    path('<slug:subCateg>/<int:urlInt>-<slug:urlSlug>.html', post_page),
    # re_path(r'^(?P<slug>[^\.]+)/$', index_page),
]
# Доступ к загруженным файлам(static/files)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
