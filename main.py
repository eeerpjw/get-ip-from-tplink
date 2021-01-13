import os
import argparse
import time
from threading import Timer
from datetime import datetime
from restart_notification import send_noti
def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--freq", type=float, default=0.5, help="frequency of checking IP")
    opt = parser.parse_args()
    return opt

def doit():
    # 开机启动的话这里需要将python的地址改为绝对路径，
    # 指定python环境位置，否则会默认系统自带的python，导致出错
    os.system("python check_send.py") 
    intertime = opt.freq*60*60
    t = Timer(intertime, doit)#每86400秒（1天），发送1次，实际要86420-6240，因为每次发送大概持续2小时，不用linux的定时任务是因为每次登陆都需要扫描二维码登陆，很麻烦的一件事，就让他一直挂着吧
    t.start()

if __name__ == '__main__':
    opt = get_opt()
    print('check IP every %s hour(s)'%opt.freq)
    s = datetime.now()
    # 不能开机后立即执行程序，会导致找找不到requests等packages问题
    print('NOW:%s，Send will start in %s minutes'%(s,6))
    time.sleep(60*6)
    # 发送机器重启的提醒
    send_noti("9xxxxxxx0@qq.com")# 发送启动的消息
    # 定期检查ip变化并发送邮件
    doit()
