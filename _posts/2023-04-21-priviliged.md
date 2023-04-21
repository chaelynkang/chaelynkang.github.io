---
layout: single
title: " Network 1차프로젝트 리허설 (2)  "
categories: keduit
tags: [ Privilege Level, keduit, 1차프로젝트  ]
toc: true 
comments: true
author_profile: true
sidebar:
    nav: "docs"
---

# Privilege Level

* Privilege Level - Cisco Device의 경우 Privilege Level의 범위가 0 - 15이다. (Privilege Level이 높을 수록 더 많은 권한을 가진다.)

* User(>) Mode의 경우 Privilege level이 1이기 때문에 기본적인 확인 명령어만 사용이 가능하다.

* Privilege Mode (#)의 경우 기본적인 Privilege level이 15이기때문에 모든 명령어 사용이 가능하다. 

* 관리자의 역할에 따라 Privilege level을 다르게 구성하여 명령어 사용을 level 별로 제한하는 것이 가능하다. 

* Privilege level 2부터 14까지는 관리자가 명령어 권한을 설정할 수 있다. 따로 권한을 설정하지 않으면 level 1의 권한을 갖게 된다.

![image](https://user-images.githubusercontent.com/128279031/232382761-34db15bb-cc05-4700-b6a1-00bbf143863b.png)

```
ASW1]
conf t
line c 0
no privilege level 15
exit
enable secret ccna123
enable secret level 2 ccna2
enable secret lever 3 ccna3
end
show run | section line con
privilege exec level => 어떤 명령을 듣게할꺼다 지정해주는 명령어 이다. 
privilege exec level 2 show running-config => 2레벨로 듣게할꺼다.
privilege exec level 3 configure terminal
privilege configure level 3 interface
privilege interface level 3 ip address
```
```
# WIN7에서 텔넷 192.168.10.11 접속 후 admin2로 접속했을떄 설정한대로 유저모드를 거치지않고 #으로 진입.
*Show VLAN-SW로 VLAN 있는것을 잡고 SVI를 만들어서 설정하면됨.

EX) VLAN 10 일경우
int VLAN 10
ip add 192.168.10.11 255.255.255.0
exit
line vty 0 4
login local
exit
username admin5 privilege 5 password ccna123 =>usermode를 거치지않고 #으로 접근 할 수 있다
```

---

# TACACS+



```
DSW1]
conf t
ip domain-name kedu.edu
crypto key generate rsa
768
ip ssh version 2

line vty 0 4
transport input ssh
login local
exit
line c 0
login local
exit
username admin password cisco

aaa new-mode => aaa mode 선언
aaa authentication login default group tacasc+ local    => 유저네임 패스워드 물어보게 해라 라는뜻.
test aaa group tacacs+ admin100 1111 legacy
no aaa authentication login default group tacacs+ local => 인증 확인을 지웠음.
aaa authentication login VTY_ACC group tacacs+ local    => 여기서 부터 인증과 권한.
line vty 0 4
login authentication VTY_ACC
username admin15 privilege 15 password cisco123
aaa authorization exec VTY_PRI group tacacs+ local
aaa authorization commands 15 VTY_PRI group tacacs+ local
line vty 0 4
authorization exec VTY_PRI
authorization commands 15 VTY_PRI
exit
=>텔넷으로 접근할떄 관리자 레벨하고 커맨드 권한을 타카시 서버한테 받아라 라는뜻.


# aacount

DSW1]
aaa accounting exec ACC start-stop group tacasc+
aaa accounting commands 15 ACC start-stop group tacacs+
line vty 0 4
accounting exec ACC
accounting commands 15 ACC
```


