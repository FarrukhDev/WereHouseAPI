from django.contrib import admin
from django.urls import path
from product.views import *
from user.views import *
from ombor.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Werehouse API",
      default_version='v1',
      description="Useful application for sellers and werehouse owners",
       terms_of_service="https://www.google.com/policies/terms/",
       contact=openapi.Contact(email="farruxbekergashaliev@gmail.com"),
   ),
   public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/clients/',UserListCreateAPIView.as_view(),name = 'all_clients'),
    path('create/user/',UserListCreateAPIView.as_view(),name = 'create_user'),
    path('get/client/<int:pk>',UserRetrieveUpdateDestroyAPIView.as_view(),name='get_client'),
    path('del/client/<int:pk>',UserRetrieveUpdateDestroyAPIView.as_view(),name='delete_client'),
    path('update/client/<int:pk>',UserRetrieveUpdateDestroyAPIView.as_view(),name='update_client'),
    path('get/products',ProductListCreateAPIView.as_view(),name = 'all_products'),
    path('create/product',ProductListCreateAPIView.as_view(),name = 'create_product'),
    path('get/product/<int:pk>',ProductRetrieveUpdateDestroyAPIView.as_view(),name = 'get_product'),
    path('del/product/<int:pk>',ProductRetrieveUpdateDestroyAPIView.as_view(),name = 'delete_product'),
    path('update/product/<int:pk>',ProductRetrieveUpdateDestroyAPIView.as_view(),name = 'update_product'),
    path('get/ombor',OmborListCreateAPIView.as_view(),name = 'all_ombors'),
    path('create/ombor',OmborListCreateAPIView.as_view(),name = 'create_ombors'),
    path('get/ombor/<int:pk>',OmborRetrieveUpdateDestroyAPIView.as_view(),name = 'get_ombor'),
    path('del/ombor/<int:pk>',OmborRetrieveUpdateDestroyAPIView.as_view(),name = 'delete_ombor'),
    path('update/ombor/<int:pk>',OmborRetrieveUpdateDestroyAPIView.as_view(),name = 'update_ombor'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger_doc"),
]
