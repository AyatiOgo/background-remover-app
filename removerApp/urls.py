from django.urls import path
from .views import upload_image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', upload_image, name='home'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)