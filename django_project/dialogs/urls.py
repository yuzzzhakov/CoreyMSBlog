from django.urls import path
from .views import (
    Dialogs,
    DialogView,
    MessageCreate,
    DialogCreateView,
    DialogCreate,
    DialogCheck,
)
from . import views

urlpatterns = [
    path('dialogs/', Dialogs.as_view(), name='dialogs'),
    path('dialogs/<int:id>/', DialogView.as_view(), name='dialog-view'),
    path('dialogs/message_create_<int:id>/', MessageCreate.as_view(), name='message-create'),
    path('dialog/dialog_create_view_<int:id>/', DialogCreateView.as_view(), name='dialog-create-view'),
    path('dialogs/dialog_create_<int:id>/', DialogCreate.as_view(), name='dialog-create'),
    path('dialogs/dialog_check_<int:id>/', DialogCheck.as_view(), name='dialog-check'),
]

