from django.contrib import admin
from .models import Policy, Customer, Trip, Term

@admin.register(Policy, Customer, Trip, Term)
class CustomerAdmin(admin.ModelAdmin):
    pass