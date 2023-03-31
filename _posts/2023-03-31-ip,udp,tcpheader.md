---
layout: single
title: " IP UDP TCP Header "
categories: keduit
tags: [ iP, UDP, FTP, Header ]
toc: true 
comments: true
author_profile: true
sidebar:
    nav: "docs"
---


# IPv4 Header

* IP의 header는 인터넷을 통해 packet를 routing 하는데 사용되며 다음의 필드를 포함한다.

![image](https://user-images.githubusercontent.com/128279031/228890436-65f43635-86f6-45c5-9fd2-7c46fd13c94f.png)

1. `Version` (4bits)
   * 사용된 IP protocol의 version을 나타낸다. IPv4에서는 4bit 고정.

2. `Internet Header Lengh (IHL)` (4bits) 
   * IPv4 header의 길이를 32bit word 단위로 나타낸다. 
   * 옵션을 포함한 경우, 최소값5 (4bytes*5=20bytes)부터 최소값 (4bytes*20=60bytes)까지의 값.

3. `Type of Service (TOS)` (8bits)
   * Packet에 대해 요청된 QoS (서비스 품질) 수준을 나타낸다. 
   * 뒤에 2bits는 혼잡 정도를 알리는 ECN(Explicit Congestion Notification) 필드로 사용된다.

4. `Total Lengh` (16bits) 
   * header와 payload를 포함한 packet의 총 length를 나타낸다.

5. `Identification` (16bits)  
   * data에 단편화(fragmentation)가 일어났을 경우 단편화된 각 datagram을 구분할 수 있는 일련의 번호이다.  
   * 이 값을 이용해서 이 datagram이 어떤 datagram에서 단편화 된것인지 알 수 있다.

6. `Flags` (3bits)  
   * datagram의 단편화에 대한 정보를 알려주기 위해 사용. 
   * 첫번째 bits는 예비로 사용하며 0으로 세팅된다. 
   * 두번째 비트와 세번째 비트는 단편화된 datagram의 정보를 의미하며, 1일경우 단편화 되지 않은 data를 의미한다.
   * 3번째 bits가 0일경우 마지막 단편화 임을 나타내며, 1일경우에는 단편화된 data가 더 있다는것을 나타낸다.

7. `Fragment Offset` (13bits) 
   * datagram에 대한 단편화가 일어났을 경우 현재 datagram이 원래 datagram의 몇번째 위치부터 단편화가 되었는지 나타낸다.

8. `Time to live (TTL)` (8bits) 
   * datagram이 살아있을 시간을 지정한다. router의 looping 을 방지하는 용도로 명시됨.
   * 패킷이 경유할 수 있는 최대 홉 수를 나타낸다.
   * 패킷이 라우터를 통과할때 마다 TTL값은 1씩 감소하며 , 0이되면 라우터가 패킷을 버린다.
   * 이때 송신측으로 ICMP message가 전달된다.

9. `Protocol` (8bits)
   * TCP, UDP, ICMP 등 Packet payload에 사용되는 protocol 유형을 나타낸다.

10. `Header Checksum` (16bits)
    * 헤더의 오류 감지에 사용된다.

11. `Source IP Address` (32bits)
    * 데이터를 전송하는 Host의 IP 주소.

12. `Destination IP Address` (32bits)
    * 데이터를 전송받는 Host의 IP 주소.

13. `Options (variable length)`
    * 프로그램의 특성에 의해 특정한 기능을 추가하기 위해 사용되나, 잘 사용하지 않는다.

---

# TCP Header

* TCP 헤더는 각 TCP Segment에 추가되는 가변 길이 헤더입니다. 헤더는 두 호스트 간의 연결을 설정하고 유지하는 데 사용되며 다음 필드를 포함합니다:

![image](https://user-images.githubusercontent.com/128279031/228929872-d35965d9-98f7-4abb-bf59-9a115653bb01.png)



1. `Source Port` (16bits)
   * 송신자 식별 포트 번호.

2. `Destination Port` (16bits)
   * 수신자 식별 포트 번호,

3. `Sequence Number` (32bits)
   * 시퀀스 번호는 SYN Flag를 설정했을 때 사용되는 번호이며, 전송하는 데이터의 순서를 의미한다.
   * 시퀀스 번호 덕분에 수신자는 쪼개진 Segment의 순서를 파악하여 올바른 순서로 data를 재조립할 수 있게 된다.
   * 자신이 보낼 데이터의 1bytes 당 시퀀스 번호를 1씩 증가시키며 데이터의 순서를 표현하다가 4,294,967,296를 넘어갈 경우 다시 0부터 시작한다.

4. `Acknowledgment Number` (32bits)
   * 데이터를 받은 수신자가 예상하는 다음 시퀀스 번호를 의미힌다.


5. `Data Offset` (4bits) 
   * 전체 TCP segment중 헤더가 아닌 데이터가 시작되는 위치를 표시한다.
   * 32bits의 Word 단위를 사용. (32bits 체계에서의 1 Work = 4Bytes)
   * 최소 값은 (5words) 20bytes , 최대 60byetes (15words) 의 offset까지 표현할 수 있다.
   * 옵션 필드의 길이가 고정되어 있지않아 필요한 필드이다.

6. `Reserved` (4bits)  
   * 미래를 위해 예약된 필드로 모두 0으로 설정한다.
  
7. `Flags` (8bits)
   * TCP Segment에 대한 정보를 제공하고 전송 중 동작을 제어하는 9bits flags field 이다. 
   * 혼잡 제어 기능의 향상을 위해 Reserved 필드를 사용하여 NS, CWR, ECE 플래그가 추가 되었다.
   * 각 비트는 다음과 같은 특정 의미를 갖는다.

```
URG : 1bits => TCP Segment에 긴급 데이터가 있음을 의미.
ACK : 1bits => TCP Segment가 이전에 수신한 데이터의 수신 확인을 전송하고 있음을 의미.
PSH : 1bits => 보낸 사람에게 즉시 전송해야하는 데이터가 있음을 의미.
RST : 1bits => TCP Segment가 잘못되었으며 수신시가 연결을 재설정해야 함을 의미.
SYN : 1bits => 송신자가 연결을 설정하고 초기 시퀀스 번호를 전송하고 있음을 의미. (시퀀스 번호 동기화)
FIN : 1bit => 전송할 데이터가 더 이상 없음을 의미.

NS  : RFC 3540에서 추가된 필드로 CWR, ECE 필드가 은폐되는 경우를 방어.
ECE : ECN Echo Flags 해당 필드가 1이고, syn Flags가 1일때 ECN 을 사용한다고 상대방에게 알리는 의미. SYN Flags가 0이라면 Segment Window Size를 줄여달라는 의미.
CWR : ECE Flags를 받아 전송하는 Segment Window size를 줄였다는 의미.
```

8. `Window Size` (16bits)
   * 수신받는 윈도우의 크기를 의미한다.
   * 감당하기에 큰 데이터일 경우 . 윈도우 사이즈를 줄인다.
   * 송신자는 해당 사이즈 만큼만 데이터를 전송해야만 한다.

9. `Checksum` (16bits)
   * 오류 검출 필드이다.

10. `Urgent Pointer` (16bits)
    * UGR Flags가 설정되어 있을 경우, 긴급 데이터의 위치를 알려주는 포인터이다.

11. `Options (variable length)`
    * 가변적인 크기의 필드이다.
    * 어디까지가 Header이고 어디부터가 Data인지를 알기 위해 Data Offset이 필요하다.

---

# UDP Header

* 각 UDP 데이터그램에 추가되는 고정 길이의 8bytes 헤더이다.
* 헤더는 두 호스트 간에 데이터를 전송하는 데 사용되며 다음 필드를 포함한다.


![image](https://user-images.githubusercontent.com/128279031/228930904-1178f327-d101-45be-8ee6-32e6cd3e6892.png)

1. `Source Port` (16bits)

2. `Destination Port` (16bits)

3. `UDP length` (16bits)
   * 헤더와 페이로드를 포함하여 UDP Datagram의 길이를 나타낸다.
   * 최소 8bytes , 최대 65,535bytes

4. `UDP checksum` (16bits)

---

