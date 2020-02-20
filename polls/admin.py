from django.contrib import admin
from .models.finance import Buyers, Sellers, Contracts
# Register your models here.

admin.site.site_title = "OA后台管理系统"
admin.site.site_header = "百隆商贸" + admin.site.site_title
admin.site.index_title = "欢迎登陆"


class BuyersAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ('full_name', 'tax_no', 'address', 'contact_name', 'contact_tel')


class SellersAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ('full_name', 'tax_no', 'address', 'tel', 'account_bank', 'account_no')


class ContractsAdmin(admin.ModelAdmin):
    list_per_page = 20
    # 列表页
    search_fields = ['contract_name', 'contract_no']
    list_display = ('contract_no', 'contract_name', 'award_date', 'total_value', 'expiry_date', 'expiry_state')


admin.site.register(Buyers, BuyersAdmin)
admin.site.register(Sellers, SellersAdmin)
admin.site.register(Contracts, ContractsAdmin)
