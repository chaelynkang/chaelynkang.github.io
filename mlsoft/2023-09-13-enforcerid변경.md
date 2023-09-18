```
동일한 엔포서를 사용할때 agent_id 가 똑같으면 어느 서버로 명령을 내려야할지 몰라서 오작동이 있다. 그떄 에이전트 id를 변경해야한다.

mysql -u root -p
use tcosecuip;
select * from master_info;
agent_max 값을 확인해서 겹치는 쪽과 다르게 설정한다. 예를들어 10으로 설정하고 엔포서를 추가하면 agent id가 11로 생성된다.
update master_info set agent_max='10' where svcstate='AC';
select * from master_info; // 10 verify
웹 콘솔에서 엔포서를 추가 후 agent_id를 확인한다.
select * from agent_master;
agent_id // 11 verify
```
