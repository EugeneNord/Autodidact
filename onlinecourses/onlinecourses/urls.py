from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include("autodidact.urls")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Панель администрирования онлайнкурсов "Самоучка"'
admin.site.index_title = 'Онлайнкурсы'
