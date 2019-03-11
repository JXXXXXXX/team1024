from django.db import models

# Create your models here.
class user(models.Model):
    id = models.CharField(max_length=10,primary_key=True)#学号
    pwd = models.CharField(max_length=30)#密码
    name = models.CharField(max_length=12)#姓名
    tel = models.CharField(max_length=11)#电话
    email = models.CharField(max_length=30)#邮箱
    tag = models.BooleanField()#用户标识,True 代表管理员,False 代表普通用户

class item(models.Model):
    id = models.AutoField(primary_key=True)#物品序号(整型,自增)
    name = models.CharField(max_length=30)#物品名称
    time = models.DateField()#丢失时间/捡到失物时间
    place = models.CharField(max_length=30)#物品丢失/拾获地点
    detail = models.CharField(max_length=1000)#详细描述
    image = models.ImageField()#物品图片
    state = models.BooleanField()#False 代表未找到失物/未被领取 True 代表找到失物/被领取
    tag = models.BooleanField()#False 代表失物表 True 代表招领表

class user_item(models.Model):
    #item_id = models.IntegerField(primary_key=True)
    item_id = models.ForeignKey('item',on_delete=models.CASCADE)
    user_id = models.ForeignKey('user',on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)#提交信息时间,自动生成当时时间
    class Meta:
    	unique_together=("item_id",)
class category(models.Model):
    id = models.AutoField(primary_key=True)#类别号(整型,自增)
    name = models.CharField(max_length=30)#类别名称

class item_category(models.Model):
    category_id = models.ForeignKey('category',on_delete=models.CASCADE)
    item_id =  models.ForeignKey('item',on_delete=models.CASCADE)
    class Meta:
    	unique_together=("category_id","item_id")#联合主键

class record(models.Model):
	id_1 = models.ForeignKey('user',on_delete=models.CASCADE)
	id_2 = models.CharField(max_length=10)
	item_id = models.ForeignKey('item',on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)#完成失物招领的时间,自动生成当时时间
	tag = models.BooleanField()
	#id_1 代表发布消息的人 False 代表id_2是提供失物的人 True 代表id_2是进行认领的人
	#数据表不能同时有两个属性为一个表的外键,否则报错
	class Meta:
		unique_together=("id_1","id_2","item_id")#
			