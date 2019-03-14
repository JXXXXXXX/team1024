from django.contrib import admin

# Register your models here.
from .models import user,item,user_item,category,item_category,record

admin.site.register(user)
admin.site.register(item)
admin.site.register(item_category)
admin.site.register(category)
admin.site.register(record)
admin.site.register(user_item)