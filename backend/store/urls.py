from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('accessories', views.AccessoriesViewSet, basename='accessories')
router.register('caftans', views.CaftanViewSet, basename='caftans')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.ShoppingCardViewSet)
router.register('orders', views.OrderViewSet)
router.register('customers', views.CustomerViewSet)

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-item')

urlpatterns = router.urls + carts_router.urls + [
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.login_user, name='logout'),
    path('send_email/', views.send_email)
]
