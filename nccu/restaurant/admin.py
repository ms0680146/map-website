from django.contrib import admin
from restaurant.models import Restaurant,Comment,Photo
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name','phone_number','address','opentime','longitude','latitude','fb_link','menu_link')
	
class CommentAdmin(admin.ModelAdmin):
	list_display = ('content','user','date_time','restaurant')

		
admin.site.register(Restaurant,RestaurantAdmin)	
admin.site.register(Comment,CommentAdmin)	
admin.site.register(Photo)
