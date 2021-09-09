---
layout: post
title: 通过网络唤醒(WOL)叫醒睡眠状态中的Mac
slug: waking-up-a-mac-with-wake-on-lan
date: 2021-09-10 00:00
status: publish
author: fejich
categories: 
  - 默认分类
tags: 
  - Mac
  - PC
  - WOL
excerpt: 通过意想不到的方法实现 Mac 的 WOL 唤醒
---

![WOL](通过网络唤醒(WOL)叫醒睡眠状态中的Mac.assets/WOL.png)

## WOL 是什么

Wake-on-LAN简称WOL或WoL，中文多译为“网络唤醒”、“远程唤醒”技术。WOL是一种技术，同时也是该技术的规范标准，它的功效在于让休眠状态或关机状态的电脑，透过局域网的另一台电脑对其发令，使其唤醒、恢复成运作状态，或从关机状态转成引导状态。

有关WOL技术，最初是在1997年4月由IBM公司的先进管理联盟（Advanced Manageability Alliance）所提出，然而当时仅约略透露，之后其他业者及产业也逐渐推行。

> 引用自：[网络唤醒 - 维基百科，自由的百科全书 (wikipedia.org)](https://zh.wikipedia.org/wiki/網路喚醒)



## Mac 电脑的 WOL 支持情况

WOL 基本上是个 PC电脑 都支持，然而苹果嘛~~不跟 PC 厂们玩这一套。

Mac 并没有完整支持 WOL ，**关机状态**是无法使用 WOL 唤醒的（黑苹果倒是支持关机唤醒）

但是会在**睡眠状态**下对会对 WOL 的**魔法数据包**（Magic Packet）有所反应，进入一个类似Android手机**超级省电模式**的状态。

+ 屏幕保持着关闭
+ 各种 App 也并没有运行
+ 机器会对 ping 的请求有所回应
+ 部分网络服务像是 文件共享 和 SSH远程登陆 能工作（前提是你在**系统偏好设置**打开了该功能）

这时候唯有通过按下键盘鼠标的按键才能真正唤醒 Mac 



## 通过 WOL 唤醒 Mac 的方法

由于睡眠状态下 Mac 会对 WOL 有所反应，而且可以进行 SSH远程登陆。

所以可以通过其他电脑 SSH 访问 Mac 执行 `caffeinate` 命令模拟鼠标键盘按键，实现曲线救国！

### 1）Mac 上的设置

![节能](通过网络唤醒(WOL)叫醒睡眠状态中的Mac.assets/节能.png)

![开启SSH](通过网络唤醒(WOL)叫醒睡眠状态中的Mac.assets/开启SSH.png)

开启服务后，在 系统偏好设置 `→` 网络 找到 IP 与 MAC地址 记下来后续操作要用到

让机器进入睡眠状态

### 2）其他电脑执行命令唤醒 Mac

于另一台电脑上，执行以下命令即可唤醒 Mac ！

```shell
etherwake {Mac_MAC_ADDRESS}
ssh {MacUserName}@{MacIP} 'caffeinate -u -t 1'
```



#### [可选]配置 ssh 免密码登陆 Mac

```shell
ssh-keygen -t rsa
```

>连续三次回车,即在本地主机上生成了公钥和私钥,不设置密码

```shell
cat ~/.ssh/id_rsa.pub | ssh {MacUserName}@{MacIP} 'mkdir .ssh ;cat >> .ssh/authorized_keys'
```

>将本地密钥写入到 Mac 主机信任列表内



---

参考：[Waking up a Mac with Wake On LAN – MacOS X Software – Forum](https://www.tweaking4all.com/forum/macos-x-software/waking-up-a-mac-with-wake-on-lan/)