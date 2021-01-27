import smtplib
import random
from email.mime.text import MIMEText  
# 引入smtplib和MIMEText
from time import sleep
from datetime import datetime
from tplink import LoginTpLink
import logging
from socket import gethostbyname, gaierror
# 在此更改收件人字典列表
msg_to={
	'test':'9********0@qq.com'
}

logging.basicConfig(filename='checkip.log',level=logging.INFO)

def get_news():
    ''' 
    获取路由器中当前IP
    '''
    login_tp_link = LoginTpLink()
    info=login_tp_link.get_ip_info()
    pos=info.find('ipaddr')
    return info[pos+9:pos+23]

def get_last_news(filename):
    '''
    读取上一次保存的ip
    '''
    with open(filename,'r') as f:
        ip = f.readline()
    return ip

def save_new_news(filename,ip):
    '''
    保存最新ip
    '''
    with open(filename,'w') as f:
        f.write(ip)

def send_email(msg_to,ip):
    '''
    发送ip
    '''
    host = 'smtp.163.com'  
    port = 465  
    sender = 'x****t@163.com' # 设置发件邮箱，如果此处使用的不是163，前面host和port也要更改
    # 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码
    pwd = 'CA*****WL'
    rnl = [random.random() for i in range(len(msg_to))]
    totaltime = 60*3*len(msg_to) # 每个用户三分钟
    sumrnl = sum(rnl)
    rnt = [totaltime*k/sumrnl for k in rnl]
    #print('rnt',rnt)
    flag = True

    for key,dt in zip(msg_to.keys(),rnt):
        body = 'sent at '+str(datetime.now()) + ' from 244'
        msg = MIMEText(body ) 
        msg['subject'] =  'IP Changed:'+ip
        #msg['subject'] =  '不要慌，是测试:'+iptoday
        # 设置邮件标题
        msg['from'] = sender  
        # 设置发送人
        msg['to'] = msg_to[key]
        # 设置接收人
        if flag==True:
            logging.info('Title: '+ msg['subject'] + '\n\t Content: '+ body)
            flag = False
        try:
            s = smtplib.SMTP_SSL(host, port)  
            # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            s.login(sender, pwd)
	        #s.sendmail(sender, msg['to'].split(','), msg.as_string())
            s.sendmail(sender, msg_to[key], msg.as_string())
            # 发送邮件！
            #print (body,msg['subject'],'.sent email to',key ,'success')
            logging.info(str(datetime.now())+' sent to '+ key + ' successful'+' '+msg_to[key])
	except smtplib.SMTPException as e1:
	        #print ('Error.sent email to',key, 'fail')
            logging.warn(str(datetime.now())+' sent to '+ key + ' fail due to Exception:'+e1)
        except gaierror as e2:
            logging.warn(str(datetime.now())+' sent to '+ key + ' fail due to Exception:'+e2)
        sleep(dt)


if __name__ == "__main__":
    ipfile = "latestip.txt"
    ip_new = get_news()
    ip_old = get_last_news(ipfile)
    if ip_old != ip_new:
        logging.warning('======new IP'+ip_new+', changed at '+str(datetime.now()))
        print('new IP'+ip_new+', changed at '+str(datetime.now()))
        save_new_news(ipfile,ip_new)
        send_email(msg_to,ip_new)
        #
    else:
        logging.info(str(datetime.now())+' Not changed')
        print(str(datetime.now())+' Not changed')

