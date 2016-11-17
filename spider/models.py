#coding:utf-8
"""
@file:      models.py
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2016-11-17 15:54
@description:
            存放数据库orm对象
"""
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

class Article(models.Model):
    class Meta:
        db_table = 'articles'

    title = models.TextField()
    link = models.TextField()
    bibtex = models.TextField()
    resource_type = models.TextField()
    resource_link = models.TextField()
    google_id = models.TextField()
    citations_link = models.TextField()
    id_by_journal = models.TextField()
    year = models.IntegerField()
    citations_count = models.IntegerField()
    create_time = models.TimeField()
    pdf_temp_url = models.CharField(max_length=200)


class CitationRecord(models.Model):
    citation_number = models.IntegerField()
    record_time = models.DateTimeField()


class Paper(models.Model):
    google_id = models.TextField()
    id_by_journal = models.TextField()
    title = models.TextField()
    citation_records = ListField(EmbeddedModelField('CitationRecord'))