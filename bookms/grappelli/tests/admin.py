# coding: utf-8

# DJANGO IMPORTS
from django.db import models
from django.contrib import admin

# PROJECT IMPORTS
from grappelli.tests.models import Category, Entry

site = admin.AdminSite(name="Admin Site")


class CategoryOptions(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)


class EntryOptions(admin.ModelAdmin):
    list_display = ("id", "title", "category", "user",)
    list_display_links = ("title",)


site.register(Category, CategoryOptions)
site.register(Entry, EntryOptions)


