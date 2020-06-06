from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    name = models.CharField(max_length=50, verbose_name=u"权利人名称", default="")
    ID = models.CharField(max_length=100, verbose_name=u"证件号码")
    locate = models.CharField(max_length=100, verbose_name=u"不动产坐落")
    estate_num=models.CharField(max_length=100, verbose_name=u"不动产单元号")
    estate_card = models.CharField(max_length=100, verbose_name=u"不动产权证号")
    type = models.CharField(max_length=100, verbose_name=u"共有方式")
    area = models.CharField(max_length=50, verbose_name=u"面积")
    use = models.CharField(max_length=100, verbose_name=u"用途", null=True, blank=True)
    status = models.CharField(max_length=100, verbose_name=u"登记状态", null=True, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
