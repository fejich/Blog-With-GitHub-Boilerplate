---
layout: post
title: unRAID 系统下虚拟机黑群辉硬盘无损扩容记录
slug: qemu-img_resize
date: 2021-09-07 15:20
status: publish
author: fejich
categories: 
  - 默认分类
tags: 
  - unRAID
  - NAS
excerpt: 原本只分配了 30G 虚拟硬盘容量，后期空间不够用所以有了这次扩容
---

# 0）测试环境
黑群辉DSM 6.1.X，Basic 磁盘，btrfs 分区格式
虚拟硬盘为 img 格式，原始容量 30G

# 1）调整虚拟硬盘容量
务必虚拟机关机情况下再操作

`qemu-img resize 30G.img -- +70G`

> 使用 qemu-img 命令给虚拟硬盘增加 70G 容量

# 2）使用 fdisk 无损扩容

`fdisk 30G.img`

> 具体操作记录，注意看 #号后面的中文注解


```shell
Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p #查看硬盘信息
Disk vdisk2.img: 100 GiB, 107374182400 bytes, 209715200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xed294359

Device      Boot   Start      End  Sectors  Size Id Type
vdisk2.img1         2048  4982527  4980480  2.4G fd Linux raid autodetect
vdisk2.img2      4982528  9176831  4194304    2G fd Linux raid autodetect
vdisk2.img3      9437184 62709759 53272576 25.4G fd Linux raid autodetect  #记录下第三分区的开始位置 9437184，后边要用到

Command (m for help): d #首先删掉分区
Partition number (1-3, default 3): 

Partition 3 has been deleted.

Command (m for help): n #然后新建一个，按默认选主分区跟编号即可
Partition type
   p   primary (2 primary, 0 extended, 2 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (3,4, default 3): 
First sector (9176832-209715199, default 9177088): 9437184 #这里是无损扩容的关键，必须不能填错
Last sector, +/-sectors or +/-size{K,M,G,T,P} (9437184-209715199, default 209715199): 

Created a new partition 3 of type 'Linux' and of size 95.5 GiB.
Partition #3 contains a linux_raid_member signature.

Do you want to remove the signature? [Y]es/[N]o: n # 必须选 N ，不要移除签名

Command (m for help): p #再次查看信息已经看到分区是扩容状态

Disk vdisk2.img: 100 GiB, 107374182400 bytes, 209715200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xed294359

Device      Boot   Start       End   Sectors  Size Id Type
vdisk2.img1         2048   4982527   4980480  2.4G fd Linux raid autodetect
vdisk2.img2      4982528   9176831   4194304    2G fd Linux raid autodetect
vdisk2.img3      9437184 209715199 200278016 95.5G 83 Linux

Command (m for help): w #最后按 w 保存分区表
The partition table has been altered.
Syncing disks.
```

# 3）打开虚拟机，使用 存储空间管理员 扩容即可
点 `管理`，按提示操作

![存储空间管理员](https://raw.githubusercontent.com/fejich/fejich.github.io/source/src/images/%E5%AD%98%E5%82%A8%E7%A9%BA%E9%97%B4%E7%AE%A1%E7%90%86%E5%91%98.png)
