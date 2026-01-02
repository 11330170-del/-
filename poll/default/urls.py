from django.urls import path
from .views import poll_list,PollList,PollView,pollvote,PollEdit,optioncreate,optiondelete
urlpatterns=[
    path("","poll/",poll_list),
    path("list", PollList.as_view(),name="poll_list"),
    path("<int.pk>/",PollView.as_view(),name="poll_view"),
    path("<int:oid>/vote/",pollvote.as_view(),name="poll_vote"),
    path("<int.pk>/edit",PollEdit.as_view(),name="poll_edit"),
    path("<int:pid>/add",optioncreate.as_view(),name="option_create"),
    path("<int:oid/modify",optionedit.as_view(),name="option_edit"),
    path("<int.pk/delete",optiondelete.as_view())
]