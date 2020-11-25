
import requests
import json
 
class LoginTpLink(object):
    def __init__(self):
        self.password = '12345678'
        self.stok = self.login(self.password)  # 初始化类的时候就自动登录，获取到stok(动态key)
    def encrypt_pwd(self, password):
        input1 = "RDpbLfCPsJZ7fiv"
        input3 = "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW"
        len1 = len(input1)
        len2 = len(password)
        dictionary = input3
        lenDict = len(dictionary)
        output = ''
        if len1 > len2:
            length = len1
        else:
            length = len2
        index = 0
        while index < length:
            # 十六进制数 0xBB 的十进制为 187
            cl = 187
            cr = 187
            if index >= len1:
                # ord() 函数返回字符的整数表示
                cr = ord(password[index])
            elif index >= len2:
                cl = ord(input1[index])
            else:
                cl = ord(input1[index])
                cr = ord(password[index])
            index += 1
            # chr() 函数返回整数对应的字符
            output = output + chr(ord(dictionary[cl ^ cr]) % lenDict)
        return output
    def login(self, password=''):
        encryptPwd = self.encrypt_pwd(password)
        url = 'http://tplogin.cn/'
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        payload = '{"method":"do","login":{"password":"%s"}}' % encryptPwd
        response = requests.post(url, data=payload, headers=headers)
        stok = json.loads(response.text)['stok']
        return stok
    def all_host_info(self):
        payload = '{"hosts_info":{"table":"host_info"},"method":"get"}'
        response = self.post_tp_link(payload)
        return response.text
    def reboot(self):
        payload = '{"system":{"reboot":null},"method":"do"}'
        response = self.post_tp_link(payload)
        return response.text
    def post_tp_link(self, payload):
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        url = '%sstok=%s/ds' % ('http://tplogin.cn/', self.stok)
        response = requests.post(url, data=payload, headers=headers)
        return response
    def get_ip_info(self):
        payload = '{"network": {"name": "wan_status"}, "method": "get"}'
        response = self.post_tp_link(payload)
        return response.text
if __name__ == '__main__':
    login_tp_link = LoginTpLink()
    info=login_tp_link.get_ip_info()
    pos=info.find('ipaddr')
    print(info[pos+9:pos+20])
