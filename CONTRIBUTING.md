# 작업 규칙

개인 프로젝트 기준, 최대한 가볍게 — 속도를 죽이지 않는 선에서만 규칙을 둔다. 기록과 회고를 위해 GitHub 흐름(브랜치/이슈/PR)은 그대로 유지한다.

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
- 혼자 진행하므로 formal review는 생략하되, 머지 전에 diff를 한 번 훑어보고 셀프 코멘트로 정리하기
- 머지는 Squash and merge로 — 커밋 로그를 깔끔하게 유지
- 머지 후 브랜치는 삭제

## 기록 남기기

실험 결과(탐지율, false positive 등 수치)는 이슈나 PR 설명에 남겨두면 나중에 정리할 때 그대로 재사용 가능.
