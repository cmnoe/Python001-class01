import argparse
import json
import os
import re
import socket
import threading
from multiprocessing.pool import Pool
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue, Manager

# 常用端口列表
port_list = [20, 21, 22, 23, 24, 25, 53, 80, 110, 443, 3306]

# 设置命令行参数
def getArgs():
    parser = argparse.ArgumentParser(description='tcp/ip')
    parser.add_argument('-n', type=int, default=4)
    parser.add_argument('-f', type=str, default='')
    parser.add_argument('-ip', type=str, default='')
    parser.add_argument('-w', type=str, default='result.json')
    parser.add_argument('-m', type=str, default='proc')
    parser.add_argument('-v', type=str, default='')
    return parser.parse_args()

# 监测ip地址是否正确
def checkIp(ip):
    pattern = re.compile(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
    if (re.match(pattern, ip)):
        return True 
    else:
        return False

# 处理ip格式
def formatIp(ip_Range):
    # 统一单独ip和范围ip的格式 
    if (len(ip_Range) == 1):
        ip_Range.append(ip_Range[0])
    start = int(ip_Range[0].rpartition('.')[2])
    end = int(ip_Range[1].rpartition('.')[2]) + 1
    pre = ip_Range[0].rpartition('.')[0] + '.'
    return [start, end, pre]

# 检查ip地址能否ping通
def ping(ip):
    try:
        if (os.system(f"ping -n 1 {ip} >nul 2>nul") == 0):
            print(f"useful: {ip}")
    except Exception as e:
        print(e)
    
# 检查端口是否开放
def tcp(ip, port, q, flag):
    s = socket.socket()
    try:
        if(s.connect_ex((ip, port)) == 0):
            print(port)
            if (flag == 'process'):
                q.put(port)
            else:
                q.append(port)
    except socket.error as e:
        print(e)
    finally:
        s.close()

# 读取数据
# def read(q, flag):
#     while True:
#         ip = q.get(True)

# 使用多进程处理ping命令
def processPing(ip, num):
    ip_Range = ip.split('-')
    # 检查ip地址
    for ip in ip_Range:
        if (not checkIp(ip)):
            print('请输入正确的ip地址')
            return
    [start, end, pre] = formatIp(ip_Range)
    p = Pool(num)
    for i in range(start, end):
        p.apply_async(ping, args=(pre + str(i), ))
    p.close()
    p.join()

# 使用多进程处理tcp命令
def processTcp(ip, num, file_name):
    if (not checkIp(ip)):
        print('请输入正确的ip地址')
        return
    q = Manager().Queue() # 如何确定队列需要的长度？
    print(f'{ip}可用端口：')
    p = Pool(num)
    for port in port_list:
        p.apply_async(tcp, args=(ip, port, q, 'process'))
    p.close()
    p.join()
    # 从queue中取出数据，生产json文件
    data = {ip: []}
    while not q.empty():
        data[ip].append(q.get())
    with open(f'./{file_name}', 'w') as f:
        json.dump(data, f)

# 使用多线程处理ping命令
def threadPing(ip, num):
    ip_Range = ip.split('-')
    # 检查ip地址
    for ip in ip_Range:
        if (not checkIp(ip)):
            print('请输入正确的ip地址')
            return
    [start, end, pre] = formatIp(ip_Range)
    with ThreadPoolExecutor(num) as executor:
        for i in range(start, end):
            executor.submit(ping, pre + str(i))

# 使用多线程处理tcp命令
def threadTcp(ip, num, file_name):
    if (not checkIp(ip)):
        print('请输入正确的ip地址')
        return
    q = []
    print(f'{ip}可用端口：')
    with ThreadPoolExecutor(num) as executor:
        for port in port_list:
            executor.submit(tcp, ip, port, q, 'thread')
    # 从queue中取出数据，生产json文件
    data = {ip: []}
    while len(q):
        data[ip].append(q.pop())
    with open(f'./{file_name}', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    # 拿的传入的参数
    args = getArgs()
    if (args.m == 'proc' and args.f == 'ping'):
        processPing(args.ip, args.n)
    if (args.m == 'proc' and args.f == 'tcp'):
        processTcp(args.ip, args.n, args.w)
    if (args.m == 'thread' and args.f == 'ping'):
        threadPing(args.ip, args.n)
    if (args.m == 'thread' and args.f == 'tcp'):
        threadTcp(args.ip, args.n, args.w)
    




