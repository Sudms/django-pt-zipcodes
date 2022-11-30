from rest_framework import routers
from zip_codes.api.views import PostalCodesViewSet

zip_router = routers.DefaultRouter()
zip_router.register(r'zip-code', PostalCodesViewSet)