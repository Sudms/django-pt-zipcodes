from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins, viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from zip_codes.models import PostalCode
from zip_codes.api.serializers import PostalCodeSerializer

class PostalCodesViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    '''
    Endpoint for zip codes management.
    '''
    queryset = PostalCode.objects.all()
    filter_backends = (DjangoFilterBackend,)
    
    @action(detail=False, methods=['get'], permission_classes=(IsAuthenticated,), serializer_class=PostalCodeSerializer,  url_path='address')
    def get_address(self, request):
        '''
        Get items from zip code and return the full address
        '''
        serializer = self.get_serializer(data=request.data.GET)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
