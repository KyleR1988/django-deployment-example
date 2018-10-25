from django.urls import path
from AppFour import views

# For TEMPLATE TAGGING
# Django will look for app_name
app_name = 'AppFour'

urlpatterns = [
    # Path take 3 arguments, your page name, which view to use, name of that view
    path('relative/', views.relative_url_templates, name = 'relative'),
    path('other/', views.other, name = 'other'),
]
