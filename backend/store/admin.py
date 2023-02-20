from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer


# Register your models here.
class CustomerInline(admin.StackedInline):
    model = Customer

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [CustomerInline]


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Customer)

