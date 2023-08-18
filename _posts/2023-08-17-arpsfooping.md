---
layout: single
title: " Tgate 4.0 Guide "
categories: MLSoft
tags: [ tgate ]
toc: true 
comments: true
author_profile: true
sidebar:
    nav: "docs"
---

# Tgate v4.0

* Tgate Server : Tgate Servers는 사내 망에 연결되어 있는 단말을 모니터링하고 통제 합니다.
사내 인사 DB 또는 사원 목록 파일 등을 연동하여 사용자 인증 시스템을 구축하고,  각 노드 별로 설치되어 있는 Tgate Smart Agent를 통해 사용자 및 장비 인증 신청 및 승인, 장비 인증서 폐기 등을 실행할 수 있는 모듈입니다. 

* Tgate Console : Tgate Console은 Tgate 정책 설정을 할 수 있는 사용자 인터페이스 입니다. Tgate Server에서 전송 받은 사용자 인증 현황 및 에이전트 현황 등을 표시하고, 리포트를 통해 해당 정책 보고서를 확인할 수 있습니다. 

* Enforcer: Enforcer는 각 네트워크 세그먼트(Broadcasting Domain)에 설치 되며, 에이전트가 설치 및 미설치된 모든 MAC 정보를 Tgate Server 로 전송합니다.

---

![image](https://github.com/chaelynkang/chaelynkang.github.io/assets/128279031/bcae271f-f097-42e9-a4b9-e8a793b4846c)

* Tgate 솔루션을 실행하기 전에 `반드시 Windows 개인 방화벽 등이 설치되어 있는지 확인 위의 통신 포트들에 대한 예외 포트 설정을 해야` 구성 요소 간 원활한 통신을 할 수 있습니다.

---

```
# Tgate Server 설치 및 설정 (설치 과정은 root 계정으로 진행)

adduser tgate
passwd tgate
mv TgateServerSetup.tar.gz /home/tgate
mv TgateServerTools.tar.gz /home/tgate
cd /home/tgate
./1.install_tgate_mysql.sh  // MySQL 설치
./2.install_tgate_was.sh → Apache Tomcat 설치
./3.install_jasper_server.sh → Jasper Server(ReportServer) 설치
./4.install_node_server.sh → Node Server(Realtime Server) 설치
./5.install_search_server.sh →  Elastic Search 설치
./6.install_radius_server.sh → Free Radius(ZTS) 설치
cd /home/tgate/tools/systemInfo → 시스템 대시보드 폴더로 이동
vi config.json → 시스템 대시보드 설정파일 열고 서버 IP 설정
!
./setautostart.sh → 시스템 대시보드 구동
cd /home/tgate/core/__installation__/ → Tgate 모듈 설치 폴더로 이동
./install_tgate_console.sh → Tgate Console 설치
./install_tgate_np.sh → Tgate np 설치
./install_tgate_pms_server.sh → Tgate pms 설치
./install_tgate_sdp.sh → Tgate ZTS 설치
./install_tgate_server.sh → Tgate Server 설치
```

```
# OS 업데이트 / 필수 라이브러리 설치

CentOS Version5.x/6.x/7.x 별로 스크립트 다름
tar zxvf config_tcosecuip_v7.x.x.x.tar.gz 
install_tcosecuip_config_centos_x.x
```

```
# mysql 설치 (tgate 과 같은 장비시에는 with_tgate 붙은 파일 사용) 
(※) 32/64bit, CentOS Version5.x/6.x/7.x 별로 설치파일 다름

tar zxvf mysql_tcosecuip_rpm_centos_x.x_64bit_v7.x.x.x.tar.gz
./install_tcosecuip_mysql_centos_x.x_64bit_with_tgate
reboot
cd /home/tgate/bin
./openConfig.sh
3번을 선택해서 /etc/sysconfig/elasticsearch 파일을 연다.
Xms4g -> Xms2g 변경
Xmx4g -> Xmx2g 변경
cd /home/tgate/config/  → tgate 의 환경설정 폴더로 이동
vi env.properties           → 각 IP 정보들을 NAC Server IP로 변경
```
---
## Tgate V4.0 설치 후 유의사항(모두 설치 옵션 기준)

* /home/tgate/core/common/ 아래 jdk 폴더가 생성되고 java 모듈이 설치됩니다.

* (어떤 옵션을 선택하더라도 jdk 는 설치됩니다.)

* deploy 폴더 아래 각종 웹 모듈(폴더)이 생성됩니다.

* 설치 후 모든 서버(엔진)가 시작됩니다.

* 서버 reboot 후에도 모든 서버(엔진)들은 시작됩니다.

* 검색엔진(ElasticSearch)의 메모리 설정이 매우 중요합니다. 

* MySQL 기본 메모리 설정은 4g 입니다.

※ 검색엔진은 메모리를 많이 사용하므로 2g이상 세팅을 권장합니다. 기본은 512M입니다.

---














