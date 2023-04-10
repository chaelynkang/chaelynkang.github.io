---
layout: single
title: " Linux DHCP Server "
categories: keduit
tags: [ linux, OS, DHCP Server, Samba Server ]
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

![image](https://user-images.githubusercontent.com/128279031/230876650-5b4114a8-5455-460d-ad1f-b895defa764e.png)

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

```
<win702>
- 네트워크드라이브 연결 => \\192.168.10.100\share로 연결 가능.
```

```
<linux>
- vi /etc/hostname => dd로 삭제 후 samba로 변경.

<WIN701>
- C:\Windows\System32\drivers hosts.sys 파일 바탕화면으로 옮긴 후 .text 연결하여 192.168.10.100 samba로 추가.
- 네트워크드라이브 연결 => \\samba\share로 연결 가능.
```

---

---

# DHCP Server

```
subnet 192.168.10.0 netmask
255.255.255.0 {
option routers 192.168.10.254;
option subnet-mask 255.255.255.0;
# option domain-name "kedu.edu";
   option domain-name-servers 192.168.10.100;
range dynamic-bootp 192.168.10.1 192.168.10.99;
default-lease-time 10000;
max-lease-time 50000;
}
```


```
yum -y install dhcp
getenforce
firewall-config             => dhcp 체크.
ps -ef | grep dnsmasq   => 프로레스 충돌 확인.
kill -9 XXXX => root 빼고는 삭제.
systemctl disable dnsmasq
vi /etc/dhcp/dhcpd.conf  => 위 내용으로 편집.
systemctl restart dhcpd  =>  vi 편집기 오류나면 오류 메세지창 뜸.
systemctl enable dhcpd
```

