from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('admin',views.Admininfo)
router.register('category',views.Categoryview)
router.register('batch',views.Batchview)
router.register('center',views.Centerview)
router.register('subcategory',views.Subcategoryview)
urlpatterns = [
    path('',include(router.urls))
]
