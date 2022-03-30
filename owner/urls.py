from django.urls import path
from owner import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("home",views.OwnerView.as_view(),name="addmobile"),
    path("list",views.MobileListView.as_view(),name="allmobiles"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)