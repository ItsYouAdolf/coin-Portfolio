from django.contrib import admin
from .models import country, denomination, age, metal, description

admin.site.register(country)
admin.site.register(description)
admin.site.register(denomination)
admin.site.register(age)
admin.site.register(metal)
