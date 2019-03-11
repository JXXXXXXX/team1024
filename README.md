# team1024
1.使用ImageField提示需要安装Pillow  pip install Pillow

2.数据表不能同时有两个属性为一个表的外键

3.Cannot assign “A1”: “B1” must be a “C1” instance.告诉我们 必须使用 C1 模型类的 实例，而不是具体的参数值。例如
A = User.objects.get(id=1)
MM.objects.create(fid=A,........)
而不能直接
MM.objects.create(fid=1.....)

4.datetime时间与系统时间相差8小时,在网上找了一些办法也没啥用...

数据库创建流程:
app/models.py定义数据表
settings里设置installed_apps加入当前app
命令行 python mange.py makemigrations myapp(创建的app名字)
命令行 python mange.py migrate

在admin.py 中加入
from .models import user,item,user_item,category,item_category,record
admin.site.register(user)
admin.site.register(item)
admin.site.register(item_category)
admin.site.register(user_item)
admin.site.register(category)
admin.site.register(record)
后即可在/admin页面看见详细信息

测试语句
from myapp.models import user,item,user_item,category,item_category,record
a=user(id='160810206',pwd='123',name='涂彦伦',tel='17863110620',email='875103075@qq.com',tag=True)
a.save()
b=item(name='物品',time='2019-3-11',detail='我在xx丢的,样子是xx',place='大活',state='False',tag='False')
b.save()#暂未插入图片
aa=user.objects.get(id='160810206')
bb=item.objects.get(id=1)
cc=user_item(user_id=aa,item_id=bb)#这时候cc里面存的是对象,cc.item_id是一个item实例,cc.item_id.id才是item_id的值
cc.save()
d=category(name='一卡通')#id会从1自增可以不赋值
d.save()
ee=item_category(category_id=d,item_id=bb)
ee.save()
ff=record(id_1=aa,id_2='160810207',item_id=bb,tag=True)
ff.save()