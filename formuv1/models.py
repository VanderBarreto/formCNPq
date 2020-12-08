#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:53:32 2020

@author: vanderneto
"""

from django.db import models


class Upload(models.Model):
    #file = models.FileField(widget=models.ClearableFileInput(attrs={'multiple': True}))
    docfile = models.FileField(upload_to='')
    
        
#class Document(models.Model):
#    description = models.CharField(max_length=255, blank=True)
#    document = models.FileField(upload_to='documents/')
#    uploaded_at = models.DateTimeField(auto_now_add=True)