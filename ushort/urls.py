from django.urls import path

from .views import UrlShortListCreateApiView, UrlShortRedirectView


urlpatterns = [
    path("", UrlShortListCreateApiView.as_view(), name="create_short_url"),
    path("<hash>", UrlShortRedirectView.as_view(), name="redirect_url"),
]
