# 使用说明
定时获取tplink路由器IP，并在ip变更后发送到制定邮箱列表
## 环境
- python 3.6
- requests

## 使用
1. **必要的设置和修改**，check_send.py中修改：
   - 收件人字典列表
   - 发件邮箱和授权码
   - 如果使用的不是163邮箱，需要更改host和port
> 如何申请163邮箱的授权码
> [教程](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2cda80145a1742516)

2. 使用
```bash
python main.py  # 默认每0.5小时查看一次ip变更
```
```bash
python main.py --freq 1 # 每一小时查看一次IP是否变更
```
