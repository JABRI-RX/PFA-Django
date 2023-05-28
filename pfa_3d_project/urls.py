 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include("Core.urls")),
    path('product/',include("Product.urls")),
    path('dashboard/',include("dashboard.urls")),
    path('conversation/',include("converstaion.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
