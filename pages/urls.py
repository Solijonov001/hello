from django.urls import path
from .views import HomePagesView,AboutPagesView,NewsPagesView,OutherPagesView


urlpatterns = [
    path('About/',AboutPagesView.as_view(),name= 'about'),
    path('',HomePagesView.as_view(),name='home'),
    path('About/News/',NewsPagesView.as_view(),name= 'news' ),
    path('Outher/',OutherPagesView.as_view(),name = 'author'),


]