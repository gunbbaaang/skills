# gunbbaaang / skills

**이 주소 하나만 기억하세요: `github.com/gunbbaaang/skills`**

Probe 해커톤 준비를 위한 Codex 스킬 묶음입니다. 문제 정의와 검증을 돕는 한국어 코치, 작업 기록, 인계, 시각화, 웹·PPT 제작, 데이터 검증과 개발 작업을 **51개 스킬로 한 번에 설치**합니다. 원본 출처·버전·라이선스는 [출처 안내](THIRD_PARTY_NOTICES.md)와 [버전 기록](sources.lock.json)에 있습니다.

처음 쓴다면 **[Probe 실전 사용 순서 — 웹과 PPT까지](skills/probe-hackathon-coach/references/field-guide.md)**를 보세요. 단계별 요청문과 4시간을 가정한 시간표를 담았습니다.

## 현장에서 Codex에게 할 말

아래 문장을 **평가받는 Probe 환경 안의 Codex 대화창**에 붙여 넣으세요.

```text
https://github.com/gunbbaaang/skills 저장소의 README.md와 INSTALL.md를 읽고,
여기 있는 스킬을 지금 작업 중인 프로젝트에 전부 설치해줘.
기존에 수정한 스킬은 백업하고, 설치된 목록과 시작하는 방법을 알려줘.
```

“gunbbaaang 깃허브의 skills 레포에 있는 거 다 설치해줘”라고 짧게 말해도 찾을 수 있도록 [에이전트 설치 안내](AGENTS.md)를 넣었습니다. 주소까지 붙이면 동명의 저장소와 혼동할 가능성을 줄일 수 있습니다. 설치 대상은 현재 프로젝트의 `.agents/skills/`입니다. 이 PC에만 설치한 스킬은 다른 Probe 환경으로 자동 전달되지 않습니다.

## 셸에서 직접 한 줄 설치

깨끗한 작업 폴더에서 실행합니다. Node.js 22.20 이상과 Git이 필요하며 GitHub 로그인은 필요 없습니다.

Windows PowerShell:

```powershell
npx.cmd --yes skills@1.7.4 add gunbbaaang/skills --skill '*' --agent codex --copy --yes
```

macOS / Linux:

```bash
npx --yes skills@1.7.4 add gunbbaaang/skills --skill '*' --agent codex --copy --yes
```

기존 스킬을 수정했다면 Codex에게 위의 자연어 요청을 하세요. 포함된 Python 설치기는 변경된 기존 파일을 `.agents/skill-backups/`에 보존합니다. [설치·업데이트 상세](INSTALL.md)

## 들어 있는 것

| 역할 | 설치되는 스킬 | 언제 쓰나 |
|---|---|---|
| 해커톤 코치 | `probe-hackathon-coach` | AI 사원 인터뷰, 문제 정의, 범위 결정, 구현·검증, 참가자 이해 확인 |
| 작업 기록 | `planning-with-files` | 계획·발견·진행 상황을 파일에 남기고 다음 대화에서 복구 |
| 인계 | `handoff` | 새 세션이 이어받을 목표·현재 상태·다음 행동 요약 |
| 사람이 보는 요약 | `visual-explainer` | 기록과 근거를 바탕으로 HTML 현황판·구조도·설명 페이지 작성 |
| 관계도 | `graphify` | 코드와 문서의 연결을 탐색 가능한 그래프로 표현 |
| 웹 화면 제작 | `frontend-design` | 확정한 사용자·업무 흐름에 맞는 화면 디자인과 구현 |
| React 구현 | `vercel-react-best-practices` | React/Next.js를 쓸 때 성능·구현 방식 점검 |
| 웹 품질 점검 | `web-design-guidelines` | 접근성·키보드 조작·입력·모바일 화면 검토 |
| 웹 동작 검증 | `webapp-testing` | 실제 브라우저에서 핵심 흐름·오류·복구 확인 |
| 편집 가능한 PPT | `slides` | 발표용 `.pptx`와 다시 만들 수 있는 원본 작성 |
| 데이터 탐색 | `explore-data` | CSV·Excel·표의 구조, 결측·중복·패턴 확인 |
| 분석 근거 검증 | `validate-data` | PPT·보고서 수치의 분모·집계·비교와 주장 점검 |
| 발표용 차트 | `data-visualization` | 검증된 수치를 출처·단위가 있는 차트로 표현 |
| AI 출력 평가 | `llm-evaluation` | 챗봇·검색·요약의 실제 응답과 변경 전후 품질 비교 |
| 오류 원인 추적 | `systematic-debugging` | 오류 재현·원인 가설·최소 수정·재검증 |
| 코드 분석 | `understand` | 코드의 구조와 관계 분석 |
| 그래프 화면 | `understand-dashboard` | 생성된 그래프를 브라우저에서 탐색 |
| 코드 질문 | `understand-chat` | 분석한 코드베이스에 질문 |
| 변경 영향 | `understand-diff` | 바뀐 코드가 어디에 영향을 주는지 검토 |
| 업무 구조 | `understand-domain` | 업무 개념과 처리 흐름 정리 |
| 상세 설명 | `understand-explain` | 특정 파일·함수의 동작 설명 |
| 문서 지식 | `understand-knowledge` | 위키·지식 문서의 연결 분석 |
| 빠른 파악 | `understand-onboard` | 코드와 프로젝트를 이어받는 사람을 위한 안내 |

모두 설치해도 매 작업에 모두 실행할 필요는 없습니다. Figma 전용 연동은 이 해커톤 묶음에 포함하지 않았습니다.

### 추가 개발 스킬

| 묶음 | 포함 범위 | 쓰는 목적 |
|---|---|---|
| [Superpowers](https://github.com/obra/superpowers) | 15종. 위 표의 `systematic-debugging` 포함 | 설계·계획·테스트·구현·리뷰·완료 검증 |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | 6종 | 작은 완성형 구현, 변경 검토, 남은 한계 정리 |
| [ECC](https://github.com/affaan-m/ECC) | 선별 8종, `ecc-` 접두사 | 재사용 조사, API·오류 처리, 보안·검증, AI 비용, 근거 탐색·결정 기록 |

기존 23개에 새 스킬 28개를 추가했습니다. **[전체 이름과 상황별 요청 예시](skills/probe-hackathon-coach/references/workflow-skills.md)**를 확인하세요. Codex 자동 선택을 유지하며, `$using-superpowers`, `$ponytail full`, `$ecc-verification-loop`처럼 직접 지정할 수도 있습니다. 원본 플러그인의 자동 훅·전역 설정까지 설치하는 것은 아닙니다.

## 설치 후 바로 시작

```text
$probe-hackathon-coach
Probe 실전 모드로 진행해줘. 이 터미널에서 너와 나누는 대화가 평가 대상이야.
확인된 요구사항, 선택 이유, 실제 검증 결과, 다음 행동을 기록하면서 진행하자.
기존 기록 파일이 있으면 재사용하고, 사실·내 판단·AI 제안·미검증 가설을 구분해줘.
중요한 결정과 검증은 이 대화에서도 짧게 설명해줘.
기록을 보여달라고 하면 visual-explainer로 사람이 읽기 좋은 현황판을 만들고,
새 세션으로 넘길 때는 handoff로 현재 상태와 다음 행동을 인계해줘.
```

상황별로 이렇게 말해도 됩니다.

- **기록 시작:** `$planning-with-files 지금 과제의 계획과 진행 상황을 기록해줘. 기존 기록과 중복되지 않게 해줘.`
- **현황판:** `$visual-explainer 현재 목표·결정 이유·진행 상황·실제 검증 결과·다음 행동을 한국어 HTML로 보여줘. 원본 기록 링크와 갱신 시각을 넣어줘.`
- **인계:** `$handoff 다음 세션이 바로 이어갈 수 있도록 probe-notes/HANDOFF.md에 기록해줘. 기존 문서는 경로로 참조하고 다음 행동을 구체적으로 써줘.`
- **코드 이해:** `$understand --language ko` → `$understand-dashboard`
- **코드·문서 관계도:** `$graphify 현재 프로젝트에서 핵심 코드와 요구사항 문서의 연결을 보여줘.`
- **웹 제작:** `$frontend-design 합의한 문제와 완료 기준을 바탕으로 핵심 흐름 하나를 구현해줘. React/Next.js를 사용 중이면 vercel-react-best-practices도 적용해줘.`
- **웹 검증:** `$webapp-testing 핵심 흐름의 정상 입력·잘못된 입력·실패 후 복구를 실제 브라우저로 확인하고 기대 결과와 실제 결과를 기록해줘. 이어서 web-design-guidelines로 접근성과 모바일 화면을 점검해줘.`
- **발표 자료:** `$slides 실제 인터뷰·구현·검증 기록을 근거로 [발표 시간]에 맞는 편집 가능한 PPT를 만들어줘. 문제 → 근거 → 선택 이유 → 시연 → 검증 → 한계 순서로 구성하고, 실측과 가정을 구분해줘. PPT와 원본을 함께 남겨줘.`

데이터·AI 품질을 보강할 때는 [추가 스킬 사용 가이드](skills/probe-hackathon-coach/references/evidence-skills.md)를 보세요. 고득점 준비 진행표는 [실전 가이드](skills/probe-hackathon-coach/references/score-playbook.md)에 있습니다.

- **데이터 받기:** `$explore-data 제공된 데이터의 구조·결측·중복을 확인하고 확인된 사실과 인터뷰할 가설을 나눠줘.`
- **수치 점검:** `$validate-data PPT의 주장과 수치를 원본 데이터에 대조하고 재계산 결과와 미검증 부분을 알려줘.`
- **차트:** `$data-visualization 검증된 결과를 한국어 발표용 차트로 만들고 출처·기간·단위를 표시해줘.`
- **AI 기능 평가:** `$llm-evaluation 우리 AI 기능의 정상·근거 없음·모호한 질문을 같은 기준으로 평가하고 실제 출력과 실패 사례를 기록해줘.`
- **오류 해결:** `$systematic-debugging 오류를 재현하고 근거로 원인을 좁힌 뒤 최소 수정과 재검증을 진행해줘.`
- **개발 흐름:** `$using-superpowers 이미 합의한 문제와 완료 기준을 이어받아 필요한 계획·구현·검증을 진행해줘.`
- **작은 MVP:** `$ponytail full 핵심 흐름을 가장 작은 완성형으로 구현해줘. 필요한 오류 처리와 검증은 유지해줘.`
- **최종 검증:** `$ecc-verification-loop 이 프로젝트에 해당하는 빌드·타입·테스트·변경 검토를 실행하고 실제 결과를 기록해줘.`

스킬 목록이 현재 대화에서 아직 갱신되지 않으면 해당 `.agents/skills/<이름>/SKILL.md`를 읽어 달라고 하거나 새 Codex 세션에서 시작하세요.

## 설치와 실행 준비의 차이

한 줄 설치는 **스킬과 참고 자료·런타임 소스 파일**을 설치합니다. Graphify는 Python 패키지, Understand Anything은 Node 의존성과 빌드, 웹 테스트는 Playwright와 브라우저, PPT 작성은 PptxGenJS가 필요합니다. PPT를 이미지로 확인하는 과정에는 LibreOffice와 Poppler도 사용합니다. 첫 실행 준비에는 인터넷과 시간이 들 수 있으므로 행사 전에 사용할 도구를 한 번 실행해 보세요. [도구별 준비 조건](INSTALL.md#첫-사용-시-필요한-실행-환경)

이 묶음은 자동 기록 훅, 전역 Codex 설정, 외부 전송, 자동 공개를 설정하지 않습니다. 기록은 실제 작업 중 스킬을 적용하며 갱신합니다. 기록 파일이 Probe의 평가 로그에 자동 수집된다고 가정하지 않습니다.

공식 대회 운영사와 무관한 개인 준비용 자료입니다. 실제 대회의 규칙과 제출 형식이 우선합니다. [설치 확인 범위](VALIDATION.md)
