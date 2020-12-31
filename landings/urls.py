from django.urls import path
from . import views  # , include

urlpatterns = [
    # path('', views.index, name='index'),
    path('about/<str:user_name>', views.about, name='about'),
    # path('portal', views.portal, name='portal'),
    path('essay_list/<str:user_name>', views.essay_list, name='essay_list'),
]
