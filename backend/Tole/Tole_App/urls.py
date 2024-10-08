from django.urls import path
from .views import (
    DataFillPlaces,
    PaymentInitiateView,
    PaymentSuccessView,
    PlaceCreateView,
    PlaceDescriptionView,
    PlaceDetailView,
    RegisterView,
    LoginView,
    UserView,
    LogoutView,
    google_callback,
    google_login
)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('places/create', PlaceCreateView.as_view()),
    path('places', PlaceDetailView.as_view()),
    path('payment/initiate', PaymentInitiateView.as_view(), name='initiate_payment'),  # Payment initiation
    path('payment/success', PaymentSuccessView.as_view(), name='payment_success'),    # Payment success
    path('places/<int:place_id>', PlaceDescriptionView.as_view()),
    path('dumdata', DataFillPlaces.as_view()),
    path('auth/login', google_login, name='google_login'),
    path('auth/callback', google_callback, name='google_callback'),
]
