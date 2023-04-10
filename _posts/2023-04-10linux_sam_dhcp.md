---
layout: single
title: "Linux Server (2) "
categories: keduit
tags: [ linux, OS, DHCP Server, Samba Server,    ]
toc: true 
comments: true
author_profile: true
sidebar:
    nav: "docs"
---

# Samba Server

![image](https://user-images.githubusercontent.com/128279031/230845159-9bcedbd0-173a-489f-aa30-deda03b55c58.png)

![image](https://user-images.githubusercontent.com/128279031/230845243-0af08496-2359-473c-af03-e7ac641e7658.png)

![image](https://user-images.githubusercontent.com/128279031/230845320-7c13841a-bfd2-4f01-b5c2-7aaa7ee56ef5.png)

![image](https://user-images.githubusercontent.com/128279031/230845393-b7061b7c-33b4-40b0-82ec-bfbd5321cdad.png)

![image](https://user-images.githubusercontent.com/128279031/230845463-4c049114-c6d8-48a7-8a1f-52fe228a71e6.png)

![image](https://user-images.githubusercontent.com/128279031/230845509-f3064a4a-34a0-4154-895b-dd1c2342a5e1.png)


```
rpm -qa | grep samba 
ping 168.126.63.1
rpm -ivh system-config-samba-1.2.100-2.1.noarch.rpm => rpm으로 설치.
system-config-samba => 서버 설정 창 확인.
mkdir /share
chmod777 /share
system-config-samba => 위 사진처럼 설정.
WIN701 => sysdm.cpl WORKGROUP 확인.
```

![image](https://user-images.githubusercontent.com/128279031/230845580-4805da32-3614-4349-871a-9cced81bf04f.png)

* WIN701에서 clman (1111) \\192.168.10.100 으로 접속됨을 확인할 수 있다.

---

# DHCP Server

