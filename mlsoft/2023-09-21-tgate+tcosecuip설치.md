## 1. 방화벽, 셀리눅스, 네트워크매니저 해제

## 2. useradd tgate , passwd tgate

## 3. /home/tgate/tools/__installation__/bin/1.mysql 설치

## 4. 2.3.4.5 설치

## 5. /home/tgate/core/__installation__/consle & server 설치

## 6. tcosecuip config 설치

## 7. tcosecuipDB 설치

## 8. tcosecuip server설치

## 9. tcosecuip web설치

## 10. /home/tgate/config/env.properties nic 이름 설정

## 11. /home/tcosecuip/conf/pnsvrman.conf DEVICE에 인터페이스 이름 설정

## 12. 재부팅 후 라이센스 추가, 47 기본 라이센스일시 삭제 후 웹 재기동

## 13. 7.8.0.1 로 s_version master_info; 버전 확인 7.8.0.0일시 업데이트 
```
update master_info set s_version='7.8.0.1';
```

## 14. tcosecuip c/s콘솔 접속 후 라이센스 추가

## 15. openssl 업데이트 & ssh 업데이트 

## 16. /home/tcosecuip/cmd_restart

