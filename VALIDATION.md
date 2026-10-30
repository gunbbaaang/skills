# 검증 기록

2026-10-30, Windows PowerShell에서 작업용 시험 폴더로 검증했습니다. 사용자의 기존 전역 스킬을 변경하지 않았습니다.

| 확인한 것 | 결과 |
|---|---|
| OpenAI skill-creator 형식 검사 | 13개 SKILL.md 통과 |
| skills CLI 1.7.4, 로컬 저장소 전체 설치 | 13개 발견 및 복사 설치 성공 |
| 공개 GitHub 저장소에서 전체 설치 | `gunbbaaang/skills`를 새 시험 폴더에 내려받아 13개 설치 성공. 설치 대상 508개 파일을 원본과 비교해 누락·내용 차이 없음(텍스트 줄바꿈 정규화) |
| Python 설치기 | 새 설치, 동일 내용 재실행, 기존 수정본 백업·새 버전 설치, 없는 대상 폴더 오류 처리 통과 |
| Understand Anything 공유 런타임 | 설치된 복사본에서 경로 확인, pnpm 10.6.2 의존성 설치, core TypeScript 빌드, 실제 core import 성공 |
| Graphify | 별도 가상 환경에 graphifyy 0.9.97 설치, CLI 버전 출력 성공 |
| Visual Explainer | 설치된 kit/render.mjs로 한국어 샘플 HTML 렌더링 성공. `--no-check`로 브라우저 화면 검사는 생략 |
| 출처 보존 | 원본 커밋 기록, 타사 라이선스·NOTICE, 스킬 단위 복사 시 라이선스 포함 확인 |

Graphify의 실제 LLM 추출, Understand Anything의 전체 코드 분석·대시보드 사용, 브라우저별 화면 품질, Linux/macOS 실기기 설치, Probe 플랫폼의 자동 수집·실제 채점은 검증하지 않았습니다. 스킬이 목록에 나타나는 시점은 호스트 세션의 갱신 방식에 따라 달라집니다.

실행 준비 의존성은 설치 시 자동으로 모두 내려받는 방식이 아닙니다. 사용하려는 도구의 첫 실행에 준비합니다. 실제 대회 환경의 네트워크·도구 허용 범위도 별도 확인 대상입니다.
