from django.contrib import admin
from authorization.models import authorizationModel
# Register your models here.
class authorizationAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','account','password','name','line_id','enable')
	list_filter=('account','enable')
	search_fields=('account',)
	ordering=('id',)
	
admin.site.register(authorizationModel, authorizationAdmin)

	
# 第一種方式，未加入 ModelAdmin 類別 
#admin.site.register(authorizationModel)	

# 第二種方式，加入 ModelAdmin 類別，定義顯示欄位
#class authorizationAdmin(admin.ModelAdmin):
#	list_display=('id','account','password','name','line_id','enable')
#admin.site.register(authorizationModel, authorizationAdmin)