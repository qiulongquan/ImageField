from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 使用validators.FileExtensionValidator来进行限制：
    # myfile = models.FileField(upload_to="%Y/%m/%d/", validators=[validators.FileExtensionValidator(['txt', 'pdf'],
 	#         message='myfile必须为txt,pdf格式的文件')])
    # 直接使用ImageField，就可以限制上传的文件，必须是图片，不用再使用验证器validators了，效果都是一样的
    # 如果想要使用ImageField，必须要安装Pillow库，如果没安装运行pip install Pillow安装
    myfile = models.ImageField(upload_to="%Y/%m/%d/")
