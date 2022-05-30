from django.urls import path, register_converter
from . import views
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

urlpatterns = [
    path('new/', views.post_list, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('', views.post_list, name='post_list'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_year'),

]