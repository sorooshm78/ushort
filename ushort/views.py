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
        ushort_object = get_object_or_404(UrlShort, hash=hash)
        ushort_object.add_visitor()
        return ushort_object.url
