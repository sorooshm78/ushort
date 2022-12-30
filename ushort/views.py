from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView

from .serializers import UrlShortModelSerializer
from .models import UrlShort


class UrlShortListCreateApiView(ListCreateAPIView):
    serializer_class = UrlShortModelSerializer
    queryset = UrlShort.objects.all()


class UrlShortRedirectView(RedirectView):
    def get_redirect_url(self, hash):
        url_short = get_object_or_404(UrlShort, hash=hash)
        return url_short.url
