from django.shortcuts import HttpResponseRedirect
from django.http import Http404
from .models import URL
from django.conf import settings
from .serializer import URLSerializer

from rest_framework.response import Response
from rest_framework import viewsets, pagination, permissions, status
from rest_framework.views import APIView
# Create your views here.


def capture_request(request, short_url):
    try:
        url_obj = URL.objects.get(short_url= '%s/%s'%(settings.DOMAIN_NAME,short_url))
        url_obj.total_clicks +=1
        url_obj.save()
        return HttpResponseRedirect(url_obj.long_url)
    except URL.DoesNotExist:
        raise Http404("No URL exist for it.")


class URLView(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = URLSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)


    def create(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        if not serializer_data.is_valid():
            return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_data.save()
            return Response(data=serializer_data.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)
    
        