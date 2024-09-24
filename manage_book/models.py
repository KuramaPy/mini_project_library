from enum import Enum
from django.db import models

class Category(Enum):
    Psychology = 'psy'
    Science = 'sci'
    Art = 'art'
    General = 'gen'
    Historical = 'his'
    Novel = 'nov'
    Poetry = 'poe'

    @classmethod
    def choices(cls):
        return [
            (cls.Psychology.value, 'Psychology'),
            (cls.Science.value, 'Science'),
            (cls.Art.value, 'Art'),
            (cls.General.value, 'General'),
            (cls.Historical.value, 'Historical'),
            (cls.Novel.value, 'Novel'),
            (cls.Poetry.value, 'Poetry'),
        ]

class book(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False,db_index=True)
    author=models.CharField(max_length=50,blank=False,null=False,db_index=True)
    year_publication=models.PositiveIntegerField(blank=False,null=False)
    category=models.CharField(max_length=3,blank=False,null=False,choices=Category.choices())
    pages=models.PositiveIntegerField()
    price=models.PositiveIntegerField(blank=False,null=False)
    release_date=models.DateField(auto_now_add=True,null=False)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    
'''
    class Meta:
        managed=True
        ordering=['name']
        indexes=[
            models.indexes(fields=['author','name']),
            models.indexes(fields=['name'],name='name_idx')
        ]
'''