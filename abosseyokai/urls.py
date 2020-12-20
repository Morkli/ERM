from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Abossey Okai Spare Parts Dealers Association'
admin.site.site_title = 'ASD Admin'
admin.site.index_title = 'Membership Database Administration'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', include("admin_honeypot.urls", namespace='admin_honeypot')),
    path('asdadmin/', admin.site.urls),
    path('', include("main.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)