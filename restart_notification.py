import smtplib
from email.mime.text import MIMEText  
# 引入smtplib和MIMEText
from datetime import datetime

def send_noti(msg_to):
    host = 'smtp.163.com'  
    port = 465  
    sender = 'xxxx@163.com'  
    # 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码
    pwd = 'CAxxxxxxxxxxxL'  
    
    body = 'sent at '+str(datetime.now())
    msg = MIMEText(body ) 
    msg['subject'] =  '机器重启了_(:_」∠)_'
    msg['from'] = sender  
    # 设置发送人
    msg['to'] = msg_to

    try:
        s = smtplib.SMTP_SSL(host, port)  
        # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, pwd)
	    #s.sendmail(sender, msg['to'].split(','), msg.as_string())
        s.sendmail(sender, msg_to, msg.as_string())
        # 发送邮件！
        print('Restart notification successed')
        # logging.info(str(datetime.now())+' sent to '+ key + ' successful'+' '+msg_to)
    except smtplib.SMTPException:
	    print('Error Restart notification failed')
        # logging.warning(str(datetime.now())+' sent to '+ key + ' fail')

'''
if __name__ == '__main__':
    # print('**************************Start*******************************************')
    msg_to = "9xxxxxx0@qq.com"
    send_noti(msg_to)
    # print('**************************End*********************************************')
'''