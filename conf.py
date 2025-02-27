# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
#template = {
#    "name": "Galileo",
#    "type": "local",
#    "path": "../Galileo"
#}
template = "Kepler"

enable_jsdelivr = {
    "enabled": True,
    "repo": "fejich/fejich.github.io@gh-pages"
}

# 站点设置
site_name = "瞎折腾分享"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "fejich"
email = "hi@imalan.cn"
author_homepage = "https://github.com/fejich"
description = "记录分享一些个人日常"
key_words = ['Maverick', 'GitHub', 'Share', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://sspai.com/post/58013",
        "brief": "🏄‍ Go My Own Way."
    }
#    {
#        "name": "三無計劃",
#        "url": "https://www.imalan.cn",
#        "brief": "熊猫小A的主页。"
#    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''

#评论系统
valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "lslkachJjiWR2FD0NiAxSuHH-gzGzoHsz",
    "appKey": "8YljktyttMGfrlKNHCDV3DPF",
}
