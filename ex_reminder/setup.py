from setuptools import setup

setup(
    name='ex_reminder',
    version='v1.0',
    description='I can remind you of experiments!', # 简要描述
    py_modules=['ex_reminder'],
    author='Jones',
    author_email='jlin398@wisc.edu',   # 作者邮件
    url='https://github.com/JonnesLin/ex_reminder', # 项目地址,一般是代码托管的网站
    requires=['yagmail','urllib3'],
    license='MIT'
)