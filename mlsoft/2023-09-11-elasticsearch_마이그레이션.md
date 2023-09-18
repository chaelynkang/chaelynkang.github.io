Elasticsearch 마이그레이션

1번 스크립트를 돌리면 1.x 하나 6.x 돌게됨

3번 생략 후
4번 import 진행

Export 날짜는 고객과 협의해서 뺄 날짜를 정해서 설정하면 됨
Realtime은 항상 확인해야함 . Event가 계속 쌓이면서 장애가 크게 터질 수 있으므로 .. 항상 체크 

메모리는 웬만하면 디폴트
리부트후 버전확인하면 6. 버전으로 됨을 확인



Cd /home/tgate/elasticsearch/data/nodes/0/indices

해당 경로의 난수를 고도화할 서버에서 옮기면 index를 불러오며 읽는다.

Export와 import 작업도중에는 세션이 끊기면 안됨.

엘라스틱서치 폴더 자체를 백업해야함 (서버 하드 용량 체크)
