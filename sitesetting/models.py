from django.db import models

# Create your models here.

class sitesetting(models.Model):
    address=models.TextField(verbose_name="ادرس شرکت")
    email=models.EmailField(verbose_name="ایمیل شرکت")
    phone=models.CharField(max_length=90,verbose_name="تلفن شرکت")
    about_office=models.TextField(default='',verbose_name="درباره شرکت")
    logo_image=models.ImageField(upload_to="logo",null=True,blank=True,default='logo.jpg',verbose_name="عکس لوگو")
    instagrame_address = models.URLField(blank=True,null=True,verbose_name="ادرس اینستاگرام")
    telegrame_address = models.URLField(blank=True,null=True,verbose_name="ادرس تلگرام ")
    twitter_address = models.URLField(blank=True,null=True,verbose_name="ادرس تویتر")
    write_ruls=models.TextField(default='',verbose_name='قوانین کپی رایت')


    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'


class contact_us(models.Model):
    fullname=models.CharField(max_length=90,verbose_name="نام و نام خانوادگی")
    email=models.EmailField(verbose_name="ایمیل ")
    subject=models.CharField(max_length=90,verbose_name="موضوع")
    massege=models.TextField(verbose_name="پیغام")
    is_read=models.BooleanField(default=False,verbose_name='خوانده شده / نشده')


    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = 'تماس  ها'

class privacy(models.Model):
    privacy_text=models.TextField(verbose_name="توضیح حریم خصوصی ")

    class Meta:
        verbose_name = 'حریم خصوصی'
        verbose_name_plural = 'حریم خصوصی'




class rules(models.Model):
    privacy_text = models.TextField(verbose_name="توضیح شرایط و قوانین ")

    class Meta:
        verbose_name = 'شرایط و قوانین'
        verbose_name_plural = 'شرایط و قوانین'

