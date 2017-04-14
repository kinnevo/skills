from django.core.urlresolvers import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Genre(MPTTModel):

    SKILL_TYPE = (
        ('F', 'Functional'),
        ('B', 'Behavioral'),
    )

    name = models.CharField(max_length=50, unique=True)
    skill_type = models.CharField(max_length=1, choices=SKILL_TYPE, default='F')
    description = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'pk': self.pk, })

    class MPTTMeta:
        order_insertion_by = ['name']

        def __init__(self):
            pass
