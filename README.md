# zjut-selfreport
浙江工业大学每日一报挂机自动打卡



## 配置环境

1. 安装selenium+apscheduler

```shell
pip3 install selenium
pip3 install apscheduler
pip3 install pyvirtualdisplay
```

## 参数设置

1. 设置每日打卡时间

```python
#打卡时间 小时、分钟
c_minute = "00" 
c_hour = "8"
```

2. 输入网址、学号、密码

```python
#网址、学号、密码
url = 学生战役页面的网址
username = 学号
password = 密码
```

## 运行

后台运行

```shell
nohup python3 daka.py &
```

![p1](https://i.loli.net/2021/02/07/w1Q4An2Pa8uSRVH.png)

![p2](https://i.loli.net/2021/02/07/A5z2NWJQ7gKDlLZ.png)



