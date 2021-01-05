# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   SkosConcept,
)


@admin.register(SkosConcept)
class SkosConceptAdmin(admin.ModelAdmin):
    pass



