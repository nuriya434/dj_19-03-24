from django.urls import path
from .views import MovieFilterView, movie_manage, movie_detail, create_movie, delete_movie, update_movie, session_list, session_detail, movie_list
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('', movie_manage, name='home'),
    path('movies/', movie_manage, name='movie_manage'),  
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movie/create/', create_movie, name='create_movie'),
    path('movie/<int:movie_id>/delete/', delete_movie, name='delete_movie'),
    path('movie/<int:movie_id>/update/', update_movie, name='update_movie'),
    path('sessions/', session_list, name='session_list'),
    path('session/<int:session_id>/', session_detail, name='session_detail'),
    path('movies/', movie_list, name='movie_list'),
    path('movies/filter/', MovieFilterView.as_view(), name='movie_filter'), 
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),

    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
