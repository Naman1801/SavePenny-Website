from django.contrib import admin
from . models import product,Contact,Order,OrderUpdate
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','phone','email')
    # list_editable=('phone',)
    list_per_page=5
    search_fields=('name',)
    #list_filter=('name',)

class OrderUpdateAdmin(admin.ModelAdmin):
    list_display=('order_id','update_desc')
    list_editable=('update_desc',)
    list_per_page=5
    search_fields=('name',)
    #list_filter=('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display=('order_id','name','city','amount')
    #list_editable=('update_desc',)
    list_per_page=5
    search_fields=('name',)
    list_filter=('city','state')

class productAdmin(admin.ModelAdmin):
    list_display=('product_name','desc','category','price','pub_date','image')
    list_editable=('desc',)
    list_per_page=5
    search_fields=('name','category')
    list_filter=('category','subcategory')


admin.site.register(product,productAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderUpdate,OrderUpdateAdmin)