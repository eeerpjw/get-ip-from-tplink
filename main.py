import os
import argparse
import time
from threading import Timer
from datetime import datetime

def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--freq", type=float, default=0.5, help="frequency of checking IP")
    opt = parser.parse_args()
    return opt

def doit():
    os.system("python check_send.py")
    intertime = opt.freq*60*60
    t = Timer(intertime, doit)#每86400秒（1天），发送1次，实际要86420-6240，因为每次发送大概持续2小时，不用linux的定时任务是因为每次登陆都需要扫描二维码登陆，很麻烦的一件事，就让他一直挂着吧
    t.start()

if __name__ == '__main__':
    opt = get_opt()
    print('check IP every %s hour(s)'%opt.freq)
    doit()
