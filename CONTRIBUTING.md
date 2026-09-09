# 협업 규칙

2인 팀 기준, 최대한 가볍게 — 속도를 죽이지 않는 선에서만 규칙을 둔다.

## 브랜치

`{영역}/{짧은-설명}` 형식. 영역은 저장소 폴더와 맞춘다.

- `chatbot/...` — rag-chatbot/ 관련 (예: `chatbot/embedding-pipeline`)
- `attack/...` — attacks/ 관련 (예: `attack/poisoning-scenarios`)
- `detect/...` — detection/ 관련 (예: `detect/anomaly-filter`)
- `docs/...` — docs/, README 등 문서 관련

`main`에는 직접 커밋하지 않고 항상 브랜치 → PR → 머지.

## 커밋 메시지

`{prefix}: {내용}` 형식.

- `chatbot:` `attack:` `detect:` `docs:` — 각 영역 작업
- `chore:` — 세팅, 의존성, 설정 파일 등
- `fix:` — 버그 수정
- `experiment:` — 결과가 불확실한 실험성 커밋 (나중에 리베이스/스쿼시 대상)

## 이슈

작업을 시작하기 전에 이슈부터 만든다. 제목은 `[1주차] 임베딩 모델 선정`처럼 `[N주차] 작업명` 형식. 라벨은 `week-1`~`week-7`, `chatbot`, `attack`, `detect`, `docs` 조합해서 붙인다.

## PR

- PR 본문에 관련 이슈를 `Closes #N`으로 연결
- 2인 팀이라 formal review는 생략 가능하지만, 머지 전에 상대방이 diff를 한 번은 훑어보고 리액션(👍)이나 코멘트 남기기
- 상대방이 24시간 안에 확인 못 하면 본인 판단으로 머지 가능 (발표 일정이 촉박하므로 블로킹 금지)
- 머지는 Squash and merge로 — 커밋 로그를 깔끔하게 유지
- 머지 후 브랜치는 삭제

## 발표 자료용 기록

실험 결과(탐지율, false positive 등 수치)는 이슈나 PR 설명에 남겨두면 나중에 발표자료 만들 때 그대로 재사용 가능.
