---
layout: single
title: "Cisco IOS hardware"
categories: keduit
tags: [ Cisco, Ios, hardware, router, switch ]
toc: true
comments: true
author_profile: true
sidebar:
    nav: "docs"
---

# Cisco IOS

* IOS는 Cisco사가 생산하고 있는 라우터나 스위치등의 장비에 embedded 소프트웨어 형태의 운영체제 플랫폼 이다.


* 하드웨어의 자원 관리와 사용자와 응용 프로그램들을 위한 인터페이스를 서비스한다.

* Network service를 제공 하는데 다음과 같다.

   * 네트워크 프로토콜들의 선택하고 그 기능을 활용하게 하는 특징


   * telnet, TFTP, DHCP NAT, VPN, Firewall, IDS와 같은 서비스를 제공


   * 네트워크 장치들 사이에 고속으로 트래픽을 전송하기 위한 연결 능력


   * 네트워크의 불법적인 사용을 방지하고, 네트워크 자원에 대한 접근을 제한하는 보안 능력


   * 네트워크의 성장에 따라 필요로 하는 능력이나 인터페이스를 추가함으로써 확장성 제공


   * 네트워크화된 자원들에게 접근을 보장하기 위한 신뢰성 제공


---

## IOS Device의 하드웨어 구성 요소

![image](https://user-images.githubusercontent.com/128279031/229275712-a2648d7d-7724-4272-a938-9cc689636563.png)

* `CPU` : 중앙처리장치로 운영체제와 응용 프로그램들을 실행하고 각종 주변 장치들을 제어하는 역할을 한다.


* `RAM` : 각종 소프트웨어나 데이터 구조들을 담고 있는 실제적인 작업 영역이다. 기초적인 Running-config file들이 포함되어 있다.


* `ROM` : IOS Devce가 부팅 시에 필요로 하는 기능들을 제공하고, 시스템을 유지 보수하기
위한 microcode들이 들어있다. Microcode란 소프트웨어가 하드웨어 형태(ASIC)형태로 있는 것을 말한다. 


* `Bootflash` : 일부 고성능 IOS device들은 부팅 시에 제공되는 기본적인 소프트웨어의 사이즈가 커서 ROM속에 모든 필요 기능들을 넣지 못하는 경우가 있다. 때문에 POST 루틴이나 Bootstrap등과 같은 기능들은 Bootflash라는 곳에 보관하여 쉽게 갱신할 수 있도록 한다.


* `Flash Memory` : IOS image형태로 있다가 필요에 따라 RAM에 load 되어 기동된다.


* `NVRAM` : IOS Device의 Configuration을 저장하는 용도로 사용한다. 


* `Configuration register` : 이 값은 NVRAM에 저장되며, IOS Device가 어떻게 부팅을 할 것인가를 제어하기 위해 사용한다. 


* `Interfaces` : 라우터나 스위치가 물리적으로 연결하기 위한 어댑터들을 말한다. Ethernet, Fast Ethernet, Gigabit Ethernet, 10 Gigabit Ethernet, Asynchronous Serial, Synchronous Serial, HSSI, Token-Ring, FDDI, ATM, Console과 Auxiliary Port와 같은 Line, 내부적으로 정의해서 사용하는 Loopback, Tunnel, Null 등이 있다. 


* `Backplane` : 하드웨어 구성 요소들이 연결된 system Bus 를 의미한다. 고성능 장비 일수록 분산되고 구조화된 backplane이 제공되며 처리 능력 또한 높다.


* `Switch Fabric` : 각각의 네트워크의 종류에 따라 NPU가 만든 프레임들을 각각의 다른 NPU에게 병목 없이 빠르게 전달해 주는 기능을 담당한다.

---

![image](https://user-images.githubusercontent.com/128279031/229276361-d21e5b04-8b0e-459f-badc-234de425f1fb.png)


* `Bootstrip` : 라우터나 스위치에서 부팅 시에 초기화 작업을 수행하는데 있어서 라우터나 스위치의 부팅 방법을 결정하기 위한 기능을 제공한다. NVRAM에 저장된 Configuration register값을 참조하여 어떻게 IOS를 로딩 할 것인지를 결정한다. POST에서 넘어온 후 ROM monitor 나 MINI IOS로갈지 결정하는데, 정상적인 부팅의 경우엔 flash로 넘어간다.


* `POST` : 장비 하드웨어 점검 및 기능 확인 등 자가진단을 한다.


* `Mini IOS` : IOS의 Sunet이다. 기본적인 유지보수와 관련된 작업을 수행할 수 있는다. 안전 관리자 같은 개념이다.


* `ROM monitor`: 비상 커맨드 프롬프트 기능을 한다.

---

## Cisco IOS 명령어 체계

![image](https://user-images.githubusercontent.com/128279031/229277014-aaf37ebe-ad05-418e-891e-0ef446bdc5c8.png)

* `User Mode` : 최초 IOS Device에 콘솔로 연결하면 User Mode로 접근하게 된다.

```
router>
```

* `privileged Mode` : User mode에서 이동.

```
router>enable
router#
```

* `Global Configuration Mode` : IOS Device에 특정 기능들을 설정하려면 반드시 Global Configuration Mode로 이동해야 한다.

```
router#configuration terminal (conf t)
router(config)#
```

* Global Configuration Mode에서 장비에게 필요한 기능에 따라 다양한 Mode로 진입 할 수 있다.

```
router(config)#router rip
router(config-router)#
```

```
router(config)#interface fastethernet0/0
rotuer(config-if)#
```

```
router(config)#line c 0
rotuer(config-line)#
```
* 각 Mode로 진입했다가 다시 상위 Mode로 이동하려면 exit 명령어를 사용한다.

```
router(config-if)#exit
router(config)#
```

---

# <mark style='background-color: #24292e'><font color= "white"> 한줄 요약 </font></mark>

* 학습 및 포스팅에 도움을 준 PDF 제목이 `Basic IOS configuration` 인데, 그중에서도 진짜 쪼오금만 정리 했다..