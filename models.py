from django.db import models

# Create your models here.

class userData(models.Model):
  username = models.CharField('用户名', max_length=20)
  password = models.CharField('密码', max_length=100,default='')
  email = models.CharField('邮箱', max_length=30)
  ##👆necessary when sign up,and username&email unique
  ## uesrname or email was needed when sign in
  gender = models.CharField('性别', max_length=2, null=True)
  age = models.IntegerField('年龄', null=True)
  birthData = models.DateField('出生日期', null=True)

  def __str__(self):
    return self.username