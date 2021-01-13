# 使用说明
定时获取tplink路由器IP，并在ip变更后发送到制定邮箱列表
## 环境
- python 3.6
- requests

## 使用
1. **必要的设置和修改**，[check_send.py](https://github.com/eeerpjw/get-ip-from-tplink/blob/main/check_send.py)中修改：
   - 收件人字典列表
   - 发件邮箱和授权码
   - 如果使用的不是163邮箱，需要更改host和port
   - log、存放最新ip文件的地址、doit函数中python的环境地址都要改为绝对地址
   
> 如何申请163邮箱的授权码
> [教程](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2cda80145a1742516)

2. RUN
```bash
python main.py  # 默认每0.5小时查看一次ip变更
```
```bash
python main.py --freq 1 # 每一小时查看一次IP是否变更
```
> 建议开[screen](https://www.cnblogs.com/mchina/archive/2013/01/30/2880680.html)后运行

> 也可以使用nohub COMMAND & 运行，具体参考[run_silently.py](./run_silently.py)

3. 设置开机启动（需要sudo权限）
```bash
sudo vim /etc/rc.local
```
在exit 0 前面加入：
```bash
sudo -H -u pjw nohup $PATH_PYTHON -u $PATH_TO_MAIN_FILE --freq=0.5 > $HOME/rebootip.log 2>&1 &
```
参考：
- [开机启动python脚本](https://blog.csdn.net/adcadc123456789/article/details/107201140)
- [Linux 开机启动配置 rc.local 文件运行 python 脚本的 ImportError:No module named xxx](http://deanlib.com/index.php/archives/26/)
