# Superpowers · Ponytail · ECC 사용 안내

설치 후에도 기본 진행은 `$probe-hackathon-coach`로 유지한다. 필요한 단계에서 관련 스킬을 골라 쓰며, 이미 합의한 문제·완료 기준·기록을 이어 쓴다. 같은 일을 세 가지 방식으로 다시 수행할 필요는 없다.

## 어떤 때 무엇을 쓰나

| 상황 | 요청 예 |
|---|---|
| 전체 개발 과정을 체계적으로 진행 | `$using-superpowers 이미 정한 문제와 완료 기준을 이어받아 계획·구현·검증 순서로 진행해줘.` |
| 4시간 안에 핵심 MVP 만들기 | `$ponytail full 합의한 핵심 흐름을 가장 작은 완성형으로 구현해줘. 필요한 오류 처리와 검증은 유지해줘.` |
| 구현 계획 세우기 | `$writing-plans 작업별 입력·결과물·완료 기준·검증 방법을 정리해줘. 기존 계획은 재사용해줘.` |
| 변경 내용 검토 | `$ponytail-review 이번 변경에서 실제 오동작과 빠진 검증을 근거와 함께 찾아줘.` |
| 결과를 완료로 보고하기 전 | `$verification-before-completion 완료 주장마다 실제 실행 근거가 있는지 확인해줘.` |
| 이미 있는 도구로 해결할 수 있는지 조사 | `$ecc-search-first 현재 코드와 설치된 도구부터 확인하고 재사용·확장·직접 구현 중 가장 적절한 방법을 골라줘.` |
| API와 데이터 전달 방식 설계 | `$ecc-api-design 핵심 흐름에 필요한 입력·출력·오류 응답만 정리해줘.` |
| API 실패·잘못된 입력 처리 | `$ecc-error-handling 실패를 성공으로 표시하거나 데이터를 잃는 경로가 있는지 확인하고 필요한 부분을 수정해줘.` |
| 사용자 입력·인증·비밀키 검토 | `$ecc-security-review 이번 구현과 관련된 입력 검증·접근 권한·키 노출을 점검해줘. 실제 비밀값은 출력하지 마.` |
| 빌드·테스트·변경 범위 점검 | `$ecc-verification-loop 현재 프로젝트에 해당하는 검사를 실행하고 통과·실패·미실행·해당 없음을 구분해줘.` |
| AI API 호출 비용 관리 | `$ecc-cost-aware-llm-pipeline 현재 제공자·모델과 실제 사용량을 기준으로 비용·재시도·캐시를 검토해줘.` |
| 관련 코드나 근거가 너무 많음 | `$ecc-iterative-retrieval 현재 질문에 필요한 파일과 근거를 단계적으로 좁혀줘.` |
| 중요한 선택 이유 기록 | `$ecc-architecture-decision-records 방금 내린 결정을 기존 decisions.md에 대안·이유·영향과 함께 남겨줘.` |

자동 선택은 허용되어 있다. 확실히 특정 방법을 쓰려면 `$이름`을 붙인다. 설치만으로 모든 스킬의 절차가 동시에 시작되거나 실제 테스트가 수행되는 것은 아니다.

## Superpowers — 15종

`using-superpowers`, `brainstorming`, `writing-plans`, `executing-plans`, `test-driven-development`, `systematic-debugging`, `verification-before-completion`, `requesting-code-review`, `receiving-code-review`, `finishing-a-development-branch`, `using-git-worktrees`, `dispatching-parallel-agents`, `subagent-driven-development`, `writing-skills`, `diagnosing-superpowers`.

기존 `systematic-debugging`은 중복 설치하지 않고 유지했다. 본 묶음은 Codex의 실제 도구를 사용하도록 연결했으며, 과거 예시의 모델 이름·도구 호출·전역 설정을 그대로 적용하지 않는다. 병렬 작업은 실행 환경에서 지원되고 허용될 때만 사용한다. 지원하지 않으면 한 세션에서 순서대로 진행할 수 있다.

원본의 설계·승인 절차는 이미 받은 사용자 지시와 결정 내용을 먼저 확인한다. 작은 수정에도 별도 기획 회의를 열거나, 완료된 인터뷰를 반복하지 않는다. 구현 방식의 검증과 참가자의 직접 설명은 계속 구분한다.

## Ponytail — 6종

`ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help`.

- 해커톤에서는 `full`로 시작하면 작은 구현을 완성하는 데 도움이 된다. `lite`는 더 작은 대안을 제안하고, `ultra`는 요구 자체가 필요한지도 적극 검토한다.
- `ponytail-review`는 이번 변경, `ponytail-audit`는 전체 저장소를 검토한다.
- `ponytail-debt`는 실제 코드의 `shortcut:` 표식을 찾아 남은 한계를 정리한다.
- `ponytail-gain`의 수치는 원저자의 발표한 벤치마크다. 내 프로젝트의 절감량이나 Probe 점수로 해석하지 않는다.
- 이 묶음에는 Claude 전용 상태 표시줄, 과거 세션 가져오기, 자동 시작 훅을 설치하지 않는다.

## ECC — 선별한 8종

`ecc-search-first`, `ecc-api-design`, `ecc-error-handling`, `ecc-security-review`, `ecc-verification-loop`, `ecc-cost-aware-llm-pipeline`, `ecc-iterative-retrieval`, `ecc-architecture-decision-records`.

원본은 [affaan-m/ECC](https://github.com/affaan-m/ECC)이며 이전 이름은 `everything-claude-code`다. 원저자는 README에서 2025년 9월 Anthropic × Forum Ventures 해커톤에서 zenith.chat으로 우승했다고 설명한다. 이는 원저자의 설명을 확인한 것이며, 현재 저장소의 모든 스킬이 그 대회 당시 사용됐다는 뜻은 아니다.

본 묶음에는 해커톤 개발과 근거 정리에 직접 쓰는 8개만 포함했다. ECC 전체 설정, 자동 학습, 백그라운드 작업, 외부 MCP 연결은 포함하지 않았다. `ecc-` 접두사는 다른 스킬과 출처를 구분하기 위한 것이다.

## 기록은 하나로 연결

`Probe 코치로 문제·완료 기준 유지 → 필요한 개발 스킬 적용 → 실제 실행 결과 기록 → 참가자가 선택 이유와 구조 설명` 순서로 이어 간다. 빌드 성공과 업무 문제 해결, 자동 생성된 설명과 참가자의 이해, 원저자의 벤치마크와 현재 실측을 각각 구분한다.
