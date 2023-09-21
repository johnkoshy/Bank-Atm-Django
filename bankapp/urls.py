from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('customer_details', views.customer_details, name='customer_details'),
    path('deposit/<int:id>', views.deposit, name='deposit'),
    path('deposit/deposit_amount/<int:id>', views.deposit_amount, name='deposit_amount'),
    path('withdraw/<int:id>', views.withdraw, name='withdraw'),
    path('withdraw/withdraw_amount/<int:id>', views.withdraw_amount, name='withdraw_amount'),
    path('card/add/', views.card_selection, name='add'),
    path('card/<int:pk>/', views.update_view, name='change'),
    path('card/ajax/load-types/', views.load_types, name='ajax_load_types'),
    path('card/success', views.success, name='success'),
    path('phone/activate/', views.phone_activation, name='phone_activation'),
]