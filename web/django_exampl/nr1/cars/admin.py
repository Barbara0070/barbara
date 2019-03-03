from django.contrib import admin
from cars.models import Car
# Register your models here.
#admin.site.register(Car)
from cars.models import Engine

class CarAdmin(admin.ModelAdmin):
    list_display= ["brand", "model", "year"]
    list_filter = ["brand"]
 #   search
    pass
admin.site.register(Car, CarAdmin)


admin.site.register(Engine)


