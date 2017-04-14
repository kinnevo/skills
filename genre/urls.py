from django.conf.urls import url
from .views import SkillDetail, SkillUpdate, SkillDelete, SkillCreate, SkillList
from .models import Genre

urlpatterns = [
    url(r'detail/(?P<pk>\d+)', SkillDetail.as_view(model=Genre), name="genre_detail",),
    url(r'update/(?P<pk>\d+)', SkillUpdate.as_view(model=Genre), name="genre_update",),
    url(r'delete/(?P<pk>\d+)', SkillDelete.as_view(model=Genre, success_url='list'), name="genre_delete",),
    url(r'create', SkillCreate.as_view(model=Genre), name="genre_create",),
    url(r'list', SkillList.as_view(model=Genre), name="genre_list",),
]
