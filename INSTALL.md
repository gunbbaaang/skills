# Codex에서 전체 설치

사용자가 이 저장소의 전체 설치를 요청하면 다음 순서로 진행합니다. 현재 작업 프로젝트 위치를 먼저 기억합니다.

1. 이 저장소를 임시 폴더에 다운로드하거나 clone합니다. 공개 저장소라 다운로드에 GitHub 로그인이 필요 없습니다. 이미 있는 사용자 폴더는 덮어쓰지 않습니다.
2. `scripts/install.py`를 읽고 Python 3.10 이상으로 실행합니다.

   ```sh
   python /absolute/path/to/skills/scripts/install.py --project /absolute/path/to/working-project
   ```

   Windows에서는 경로에 공백이 있으면 따옴표로 감쌉니다. macOS/Linux에서 `python`이 없으면 `python3`를 사용합니다. 이 스크립트는 현재 프로젝트의 `.agents/skills/`에 51개 스킬을 복사합니다. 기존 내용이 다르면 `.agents/skill-backups/<시각>/`에 먼저 옮겨 보존합니다. 같은 내용은 다시 쓰지 않습니다. 경로가 프로젝트 밖으로 연결되어 있으면 자동 덮어쓰지 않고 오류를 보고합니다.

3. 설치된 `SKILL.md` 51개와 `understand/runtime/package.json`, Graphify의 `references/`, Visual Explainer의 `kit/render.mjs`, Slides와 Webapp Testing의 `scripts/` 및 `BUNDLE.md`를 확인합니다. Superpowers 참고 자료·보조 스크립트, Ponytail 6종, `ecc-` 스킬 8종도 포함되어야 합니다.
4. 스킬 파일 설치와 실행 프로그램 준비는 구분해서 보고합니다. 분석을 당장 요청하지 않았다면 무거운 의존성 설치나 전체 프로젝트 분석을 자동 시작하지 않습니다.
5. 사용자는 README의 시작 문장으로 진행합니다. 현재 세션 목록에 안 보이면 설치한 SKILL.md를 직접 읽어 적용하거나 새 Codex 세션을 엽니다.

## 깨끗한 프로젝트에서 한 줄로 설치

Node.js 22.20 이상과 Git이 필요합니다. 아래 명령은 셸에서 실행합니다. `--skill '*'`는 이 저장소의 모든 스킬을 선택합니다. `--agent codex`는 다른 에이전트까지 설치되는 것을 막고, `--copy`는 심볼릭 링크 대신 복사합니다.

```sh
npx --yes skills@1.7.4 add gunbbaaang/skills --skill '*' --agent codex --copy --yes
```

Windows PowerShell에서는 `npx.cmd`를 사용합니다. 기존 스킬을 수정했다면 위 명령 대신 백업 기능이 있는 Python 설치기를 사용합니다.

## 첫 사용 시 필요한 실행 환경

Superpowers·Ponytail·ECC는 기본적으로 현재 Codex가 읽고 적용하는 지침입니다. Superpowers의 선택적 작업 기록 도우미에는 Git와 Bash, 시각적 브레인스토밍에는 Node.js·브라우저, 흐름도 렌더러에는 Graphviz가 필요할 수 있습니다. Windows에서는 Git Bash 사용 가능 여부를 확인하며, 필요한 도구가 없으면 가능한 수동 절차와 미실행 부분을 구분합니다. 설치만으로 서버·병렬 에이전트·외부 API 호출을 시작하지 않습니다.

| 도구 | 준비 |
|---|---|
| 해커톤 코치·Handoff | 추가 실행 프로그램 없음 |
| Planning with Files | 파일 기록은 바로 사용. 보조 스크립트는 Python/PowerShell 또는 sh. 이 묶음은 자동 훅을 설치하지 않음 |
| Visual Explainer | 포함된 Node 렌더러와 HTML을 볼 브라우저. 자동 화면 검사는 브라우저 환경에 따라 달라짐 |
| Graphify | Python 3.10+, `graphifyy==0.9.97`. 설치된 `graphify/BUNDLE.md`의 분리된 설치 방식 사용 |
| Understand Anything | Node.js 22+, 인터넷으로 pnpm 의존성 설치 및 core 빌드. `node <설치경로>/understand/scripts/runtime.mjs --setup` |
| Frontend Design·React Best Practices | 스킬 자체에 별도 실행 프로그램 없음. 실제 웹 프로젝트의 개발 환경 사용 |
| Web Design Guidelines | 가이드 원문 조회에 인터넷 사용. 실패하면 포함된 기준 스냅샷으로 검토하고 기준 시점을 밝힘 |
| Webapp Testing | Playwright와 실행 가능한 브라우저. 기존 프로젝트 환경을 우선하며 자세한 준비는 `webapp-testing/BUNDLE.md` 참조 |
| 데이터 탐색·분석 검증 | 로컬 파일은 기존 Python 환경 사용. CSV는 표준 라이브러리로도 가능하며 필요할 때 pandas·openpyxl 등 준비. 데이터 창고 연결은 선택 |
| Data Visualization | 선택한 작업에 필요한 Python 차트 패키지와 한국어 글꼴. 결과 이미지의 실제 표시 확인 필요 |
| LLM Evaluation | 평가 설계는 추가 프로그램 없음. 실제 호출은 프로젝트의 모델·허용된 데이터·API 환경 사용. 외부 평가 서비스는 필수 아님 |
| Systematic Debugging | 프로젝트의 기존 로그·테스트 사용. 선택 보조 스크립트는 Bash·npm이 필요하며 자동 실행하지 않음 |
| Slides | PPT 작성: Node.js와 PptxGenJS. 화면 검사: Python 패키지, LibreOffice, Poppler. `slides/BUNDLE.md` 참조 |

이 묶음은 유료 API 키, Codex 계정, 대회 플랫폼 사용 권한을 제공하지 않습니다. 외부 데이터 전송이나 자동 Git 훅은 설정하지 않습니다. 새 도구의 실행 환경은 실제 대회 환경에서 허용된 범위 안에서 준비합니다.
