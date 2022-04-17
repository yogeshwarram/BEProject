from django.contrib import admin
from .models import UserDetail, Slider, Contact, Cart
from saler.models import Results, MainCat, MainProduct, Results, StudentData, Product, ProductSize, SalerDetail, category, dow, SellerSlider, MyCart, WholeSaleProduct, Orders, trend,WholeSaleProductOrders
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class StudentResource(resources.ModelResource):
   class Meta:
      model = StudentData
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource
admin.site.register(StudentData,StudentAdmin)

class MainProductResource(resources.ModelResource):
   class Meta:
      model = MainProduct
class MainProductAdmin(ImportExportModelAdmin):
   resource_class = MainProductResource
admin.site.register(MainProduct,MainProductAdmin)

class MainCatResource(resources.ModelResource):
       class Meta:
          model = MainCat
class MainCatAdmin(ImportExportModelAdmin):
   resource_class = MainCatResource
admin.site.register(MainCat,MainCatAdmin)

admin.site.site_header = 'Wrappers'

admin.site.register(Results)
admin.site.register(UserDetail)
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(SalerDetail)
admin.site.register(Slider)
admin.site.register(category)
admin.site.register(dow)
admin.site.register(Contact)
admin.site.register(SellerSlider)
admin.site.register(MyCart)
admin.site.register(WholeSaleProduct)
admin.site.register(WholeSaleProductOrders)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(trend)