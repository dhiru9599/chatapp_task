from django.urls import path
from chatapi.views import (
    UserCreateView,
    UserUpdateView,
    GroupCreateView,
    GroupDeleteView,
    GroupListView,
    GroupMemberAddView,
    MessageCreateView,
    MessageListView,
)

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/delete/<int:pk>/', GroupDeleteView.as_view(), name='group-delete'),
    path('groups/list/', GroupListView.as_view(), name='group-list'),
    path('groups/add-member/<int:pk>/', GroupMemberAddView.as_view(), name='group-add-member'),
    path('messages/create/', MessageCreateView.as_view(), name='message-create'),
    path('messages/list/', MessageListView.as_view(), name='message-list'),
]
