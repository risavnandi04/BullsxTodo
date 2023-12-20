from django.urls import path
from .views import (
    TaskCreateView,
    TaskRetrieveView,
    TaskListView,
    TaskDeleteView,
    TaskUpdateView,
    MyTokenObtainPairView,
    MyTokenRefreshView,
)


urlpatterns = [
    path("algxtodo/create", TaskCreateView.as_view(), name="task_create"),
    path(
        "algxtodo/<int:pk>/", TaskRetrieveView.as_view(), name="task_retrieve"
    ),
    path("algxtodo/", TaskListView.as_view(), name="task_list"),
    path(
        "algxtodo/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update",
    ),
    path(
        "algxtodo/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete",
    ),
    path(
        "algxtodo/token/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "algxtodo/token/refresh/",
        MyTokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
