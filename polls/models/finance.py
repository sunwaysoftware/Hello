from django.db import models
from django.utils.html import format_html
import datetime


# 卖方（乙方）
class Sellers(models.Model):
    class Meta:
        verbose_name = '卖方'
        verbose_name_plural = '卖方信息'

    full_name = models.CharField('卖方名称', max_length=100)
    tax_no = models.CharField('企业税号', max_length=50)
    address = models.CharField('经营地址', max_length=100)
    tel = models.CharField('联系电话', max_length=100)
    account_bank = models.CharField('开户银行', max_length=100)
    account_no = models.CharField('银行账号', max_length=100)

    def __str__(self):
        return self.full_name


# 买方（甲方）
class Buyers(models.Model):
    class Meta:
        verbose_name = '买方'
        verbose_name_plural = '买方信息'

    full_name = models.CharField('买方名称', max_length=100)
    tax_no = models.CharField('企业税号', max_length=50)
    address = models.CharField('联系地址', max_length=100)
    contact_name = models.CharField('联 系 人', max_length=100)
    contact_tel = models.CharField('联系电话', max_length=100, blank=True)

    def __str__(self):
        return self.full_name


# 合同
class Contracts(models.Model):
    class Meta:
        verbose_name = '合同'
        verbose_name_plural = '合同档案'

    contract_no = models.CharField('合同编号', max_length=50)
    contract_name = models.CharField('合同名称', max_length=100)
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE, verbose_name='买方名称')
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE, verbose_name='卖方名称')
    total_value = models.DecimalField('合同总额', max_digits=10, decimal_places=2)
    award_date = models.DateField('签定日期', )
    expiry_date = models.DateField('有效日期')

    def expiry_state(self):
        rtn_state = '<span style="color:%s;">%s</span>'
        if self.expiry_date < datetime.date.today():
            rtn_state = rtn_state % ('red', '已过期')
        elif self.expiry_date - datetime.date.today() < datetime.timedelta(days=60):
            rtn_state = rtn_state % ('blue', '即将到期')
        else:
            rtn_state = rtn_state % ('green', '合同期内')
        return format_html(rtn_state)

    expiry_state.short_description = '合同状态'  # 设置方法字段在admin中显示的标题

    def __str__(self):
        return self.contract_name
