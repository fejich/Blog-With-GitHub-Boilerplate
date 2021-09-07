---
layout: post
title: Linux系统下使用 rsync 代替 cp
slug: rsync
date: 2021-09-07 16:50
status: publish
author: fejich
categories: 
  - 默认分类
tags: 
  - Linux
excerpt: rysnc 内置于大多数 Linux 发行版内，功能强大
---

![rsync](https://raw.githubusercontent.com/fejich/fejich.github.io/source/src/images/rsync-1920x800.png)

`rsync` 是一个常用的 Linux 应用程序，用于文件同步。

它可以在本地计算机与远程计算机之间，或者两个本地目录之间同步文件。它也可以当作文件复制工具，替代 `cp` 和 `mv` 命令。


### 显示单个文件进度，保留文件的权限

```shell
rsync -ah --progress /source /destination
```


### 显示总体进度，保留文件的权限

```shell
rsync -ah --info=progress2 --no-i-r /source/ /destination
```

> 目标目录destination如果不存在，rsync 会自动创建。执行上面的命令后，源目录source被完整地复制到了目标目录destination下面，即形成了destination/source的目录结构。

> > 如果只想同步源目录source里面的内容到目标目录destination，则需要在源目录后面加上斜杠 / 。


### 文件夹镜像

```
rsync -ah --info=progress2 --no-i-r --delete /source/ /destination
```


### 设置为命令别名，方便调用
```
alias cp="rsync -ah --progress"
alias rcp="rsync -ah --info=progress2 --no-i-r"
```

### rsync 常用选项：

`-a` 递归传输并保持所有文件属性，最常用

`-h` 以人类可读的格式输出

`-v` 详细模式输出

`-z` 文件在传输时进行压缩处理

`--delete` 删除只存在于目标目录、不存在于源目标的文件，即保证目标目录是源目标的镜像。

---
参考：http://www.ruanyifeng.com/blog/2020/08/rsync.html