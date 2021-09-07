---
layout: post
title: SSH免密登录OpenWRT路由器并执行命令
slug: ssh_autologin
date: 2021-09-07 19:30
status: publish
author: fejich
categories: 
  - 默认分类
tags: 
  - Linux
  - OpenWRT
excerpt: 
---

![Dropbear](SSH免密登录OpenWRT路由器并执行命令.assets/Dropbear_Land.png)



# 前言

`Dropbear`是一款基于ssh协议的轻量sshd服务器，与OpenSSH相比，他更简洁，更小巧，运行起来占用的内存也更少。

每一个普通用户登录，OpenSSH会开两个sshd进程，而dropbear只开一个进程，所以其对硬件要求更低，也更利于系统的运行。

Dropbear常用于“嵌入”式的Linux（或其他Unix）系统，OpenWRT 路由系统就是其中之一

# 配置 ssh 密钥

`ssh-keygen -t rsa`

>连续三次回车,即在本地主机上生成了公钥和私钥,不设置密码

`cat ~/.ssh/id_rsa.pub | ssh -p 1022 root@192.168.168.1 'cat >> /etc/dropbear/authorized_keys'`

>将本地密钥写入到路由信任列表内



# 测试免密登录路由器并执行命令

`ssh -p 1022 root@192.168.168.1 "touch /root/test ; ls"`



# 配置 crontab 定时执行命令

`crontab -e`

```bash
#凌晨4点重启路由+5点进行时间同步
0 4 * * * ssh -p 1022 root@192.168.168.1 "reboot"
0 5 * * * ssh -p 1022 root@192.168.168.1 "ntpd -n -q -p ntp.aliyun.com"
```

# 参考

https://www.jqhtml.com/61355.html

