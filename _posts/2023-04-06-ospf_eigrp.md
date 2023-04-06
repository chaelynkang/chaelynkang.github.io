---
layout: single
title: " OSPF, EIGRP Redistribute  "
categories: keduit
tags: [ OSPF, DynamicRouting, Protocol, EIGRP, Redistribute ]
toc: true 
comments: true
author_profile: true
sidebar:
    nav: "docs"
---

# OSPF & EIGRP Redistribute

![image](https://user-images.githubusercontent.com/128279031/230278433-0b2b95ac-2b28-4039-8b93-6f72a2094e60.png)
![image](https://user-images.githubusercontent.com/128279031/230279619-4bf2cb07-817e-47aa-a200-74642a5c482c.png)

```
# 공통 설정

En
conf t
no ip domain lookup
line c 0
logg syn
exec-timeout 0
exit
hostname 

int s1/0
no shut
encap fram
no fram inver
clock rate 64000
exit
```

```
# IP Address & Mapping 

R1]
conf t
int l0
ip add 6.6.1.1 255.255.255.0
exit
int s1/0
ip add 6.6.12.1 255.255.255.0
fram map ip 6.6.12.2 102 br

R2]
conf t
int l0
ip add 6.6.2.2 255.255.255.0
exit
int s1/0.12 m
ip add 6.6.12.2 255.255.255.0
fram map ip 6.6.12.1 201 br
exit
int s1/0.23 m
ip add 6.6.23.2 255.255.255.0
fram map ip 6.6.23.3 203 br

R3]
conf t
int l0
ip add 6.6.3.3 255.255.255.0
exit
int s1/0.23 m
ip add 6.6.23.3 255.255.255.0
fram map ip 6.6.23.2 302 br
exit
int s1/0.34 p
ip add 6.6.34.3 255.255.255.0
fram inter 304

R4]
conf t
int l0
ip add 6.6.4.4 255.255.255.0
exit
int s1/0.34 p
ip add 6.6.34.4 255.255.255.0
fram inter 403
```

```
# OSPF & EIGRP

R1]
router ospf 6
router-id 6.6.1.1
net 6.6.1.1 0.0.0.0 a 0
net 6.6.12.1 0.0.0.0 a 0

R2]
router ospf 6
router-id 6.6.2.2
net 6.6.2.2 0.0.0.0 a 0
net 6.6.12.2 0.0.0.0 a 0
exit
router eigrp 6
no-auto
net 6.6.23.2 0.0.0.0

R3]
router eigrp 6
eigrp router-id 6.6.3.3
no auto
passive-interface lo0
net 6.6.3.3 0.0.0.0
net 6.6.23.3 0.0.0.0
net 6.6.34.3 0.0.0.0

R4]
router eigrp 6
eigrp router-id 6.6.4.4
no auto
passive-interface lo0
net 6.6.4.4 0.0.0.0
net 6.6.34.4 0.0.0.0
```

```
# DR, BDR 선출.

R1]
int s1/0
ip ospf network broad

R2]
int s1/0.12
ip ospf network broad
```

```
# OSPF & EIGRP Redistribute

R2]
router ospf 6
redistribute eigrp 6 subnets => 자동 산출.
exit
router eigrp 6
redistribute ospf 6 metric 1544 2000 255 1 1500

=>R1에서 sh ip route 로 확인하면 E2로 확인되는데, 이는 외부 고정 코스트. 
만약 외부 변동 코스트(E1)가 필요할땐 다음과 같은 명령을 한다.

R2]
router ospf 6
no redistribute eigrp 6 subnets
redistiribute eigrp 6 subnets metirc-type 1
```

```
# 6.6.0.0/20 null 0 가 보이게 하시오 =>summary

R2]
int s1/0.23
ip summary-address 6.6.0.0 255.255.240.0
```

* R1에서 sh ip route 하면 6.6.0.0/20로 자기자신이 외부 코스트로 잡힌 이상한 현상을 볼 수 있다. 
* 즉, R2에서 축약해서 보낸게, R4를 거쳤다가 돌아옴. 오바이트된 현상이라 볼 수 있다.
* 해결 방법 2가지가 있는데 그중 첫번 째가 route-map 활용.

```
# 1. route-map 활용.

R2]
ip prifix-list EIGRP_NET permit 6.6.23.0/24
ip prifix-list EIGRP_NET permit 6.6.3.0/24
ip prifix-list EIGRP_NET permit 6.6.34.0/24
ip prifix-list EIGRP_NET permit 6.6.4.0/24
route-map EIGRP_NET
match ip add prefix-list EIGRP_NET
exit
router ospf 6
no redistribute eigrp 6 subnets metirc-type 1
redistribute eigrp 6 subnets route-map EIGRP_NET => subnets 을 붙여야 classless.
```

```
# 2. distribute-list 활용.

R2]
ip prefix-list OVER_WRITE deny 6.6.0.0/20
ip prefix-list OVER_WRITE permit 0.0.0.0/ le 32 => 0~32bits 사이. 모든 prefix라는 이야기.
router ospf 6
no redistribute eigrp 6 subnets route-map EIGRP_NET
redistribute eigrp 6 subnets
distribute-list prefix OVER_WRITE out eigrp 6

=>OSPF가 아니니 outbound로 밀쳐낸다
```

```
# R4에 루브백5를 5.5.8~11.1/24 로 네 개 만드시오.

R4]
int l5
ip add 5.5.8.1 255.255.255.0
ip add 5.5.9.1 255.255.255.0 se
ip add 5.5.10.1 255.255.255.0 se
ip add 5.5.11.1 255.255.255.0 se
```

```
# R1에서는 R4의 루프백5가 5.5.8.0/22 하나로 보여야 한다.

R4]
router eigrp 6
network 5.5.8.0 0.0.3.255
exit
int s1/0.34
ip summary-address eigrp 6 5.5.8.0 255.255.252.0
```


