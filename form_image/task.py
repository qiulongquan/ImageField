from celery import task

@task(name='form_image.tasks.func_name')   #appname为当前app注册的名字
def func_name():
    print ("测试成功")