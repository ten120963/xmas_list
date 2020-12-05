from django.urls import path
from . import views
from .views import SearchHomePageView, SearchResultsView

urlpatterns = [
    path('', views.home, name="home"),
    path('add_address', views.add_address, name="add_address"), 
    path('edit_address/<list_id>', views.edit_address, name="edit_address"),    
    path('delete_address/<list_id>', views.delete_address, name="delete_address"), 
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('uncross/<list_id>', views.uncross, name='uncross'),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('search_home', SearchHomePageView.as_view(), name='search_home'),
]
