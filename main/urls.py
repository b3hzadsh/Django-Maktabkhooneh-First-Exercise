from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main import views

app_name = "main"
urlpatterns = [
    path("", views.langing),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
