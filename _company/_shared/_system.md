# 🧬 1인 기업 OS — 자가 매뉴얼

## 이 폴더는 무엇인가요?
당신의 1인 기업의 두뇌입니다. 7명의 AI 에이전트가 여기서 일합니다.

## 폴더 구조
- `_shared/` — 모든 에이전트가 매번 읽는 공동 메모리
  - `identity.md` — 회사 정체성 (이름, 톤, 가치)
  - `goals.md` — 목표
  - `decisions.md` — 의사결정 로그 (자가학습이 자동 누적)
  - `_system.md` — 이 파일
- `_agents/<id>/` — 각 에이전트 개인 공간
  - `memory.md` — 자가학습 (자동, append-only)
  - `prompt.md` — 페르소나 디테일 (사용자가 편집)
  - `config.md` — API 키·시크릿 (`.gitignore`로 보호)
- `sessions/<ts>/` — 세션별 산출물 (자동)
- `_cache/` — API 응답 캐시 (sync 제외)

## 메모리 위계 (충돌 시 우선순위)
1. `decisions.md` — 가장 강한 신뢰
2. `identity.md`
3. `goals.md`
4. 개인 메모리
5. 지식 베이스 (`10_Wiki/`)

## 다른 PC로 옮길 때
1. 새 PC에 Connect AI 설치
2. 👔 모드 ON → "📥 다른 PC에서 가져오기" 선택
3. GitHub URL 입력 → 자동 clone
4. 끝.

## 동기화 정책
- `_shared/`, `_agents/*/memory.md`, `_agents/*/prompt.md`, `sessions/` → git sync ✅
- `_agents/*/config.md`, `_cache/` → git sync ❌ (시크릿·캐시)

## 7명의 에이전트
- 🧭 **CEO** (Chief Executive Agent): 오케스트레이션, 작업 분해, 종합 판단, 다음 액션 결정
- 📺 **레오** (Head of YouTube): 유튜브 채널 운영, 영상 기획서(제목·후크·구조), 트렌드 분석, 썸네일 브리프, 업로드 메타데이터, 시청자 유지율 전략
- 📷 **Instagram** (Head of Instagram): 인스타그램 릴스/피드 콘셉트, 캡션, 해시태그 전략, 게시 시간, 스토리, 팔로워 인게이지먼트
- 🎨 **Designer** (Lead Designer): 브랜드 디자인 브리프(컬러·타이포·레퍼런스), 썸네일 컨셉 3안, 비주얼 시스템, 디자인 가이드
- 💻 **코다리** (시니어 풀스택 엔지니어): 코드 작성·편집·디버깅, 자동화 스크립트, API 통합, 웹사이트/봇, 데이터 파이프라인, git 워크플로, 자기 검증 루프
- 💼 **현빈** (비즈니스 전략가 · Head of Business): 수익화 모델, 가격 전략, 시장·경쟁 분석, ROI/KPI 설계, 비즈니스 의사결정
- 📱 **영숙** (비서 · Personal Assistant): 일정·할 일 관리, 다른 에이전트 작업 요약·텔레그램 보고, 데일리 브리핑, 알림
- 🎵 **루나** (Sound Director & Composer): 영상 BGM 자동 생성 (MusicGen/ACE-Step 로컬 모델), 사운드 디자인, 영상-음악 합성, 자막·타이틀 동기화, 오디오 후처리
- ✍️ **Writer** (Copywriter): 카피라이팅, 영상 스크립트 초안, 인스타 캡션, 블로그 글, 메일 톤앤매너, 후크 작성
- 🔍 **Researcher** (Trend & Data Researcher): 트렌드 리서치, 경쟁사 분석, 데이터 수집·요약, 인용 자료 정리, 사실 확인

## ⚠️ 필수 규칙 — 작업 완료 후 결과 페이지 생성

모든 에이전트는 작업이 완료되면 반드시 프로젝트 폴더 최상단에 `결과.html` 파일을 만들거나 업데이트해야 한다.

이 파일은 **비개발자(대표)가 브라우저에서 바로 여는 페이지**다. 아래 형식을 정확히 따른다:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>결과 — [프로젝트명]</title>
<style>
  body { font-family: -apple-system, sans-serif; max-width: 600px; margin: 60px auto; padding: 0 24px; background: #f9f9f9; color: #111; }
  h1 { font-size: 22px; margin-bottom: 6px; }
  .sub { color: #888; font-size: 13px; margin-bottom: 32px; }
  .section { background: white; border-radius: 12px; padding: 20px 24px; margin-bottom: 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .section h2 { font-size: 13px; color: #888; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px; }
  .btn { display: inline-block; background: #5b52f0; color: white; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-weight: 600; font-size: 15px; margin: 6px 6px 6px 0; }
  .btn-outline { background: none; border: 2px solid #5b52f0; color: #5b52f0; }
  .todo { list-style: none; padding: 0; }
  .todo li { padding: 6px 0; border-bottom: 1px solid #f0f0f0; font-size: 14px; color: #444; }
  .done { color: #888; text-decoration: line-through; }
  .badge { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
  .badge-done { background: #e8f5e9; color: #2e7d32; }
  .badge-wip { background: #fff3e0; color: #e65100; }
</style>
</head>
<body>
  <h1>✅ [프로젝트명]</h1>
  <div class="sub">마지막 업데이트: [날짜] &nbsp;·&nbsp; <span class="badge badge-done">완료</span></div>

  <div class="section">
    <h2>무엇을 만들었나요?</h2>
    <p>[코드 없이, 쉬운 말로 설명]</p>
  </div>

  <div class="section">
    <h2>바로 확인하기</h2>
    <a href="[URL 또는 file://경로]" class="btn" target="_blank">🌐 사이트 열기</a>
    <!-- 게임이면: <a href="..." class="btn">🎮 게임 실행</a> -->
    <!-- 파일이면: <a href="file://절대경로" class="btn">📁 파일 열기</a> -->
  </div>

  <div class="section">
    <h2>완료된 작업</h2>
    <ul class="todo">
      <li class="done">✓ [완료된 항목]</li>
      <li>○ [진행 중인 항목]</li>
    </ul>
  </div>

  <div class="section">
    <h2>대표님이 결정해야 할 것</h2>
    <p>[다음 단계, 확인 요청 사항]</p>
  </div>
</body>
</html>
```

규칙:
- 코드, 에러 로그, 기술 용어는 절대 넣지 않는다
- 링크는 실제로 클릭 가능한 URL이어야 한다 (로컬 파일은 file:// 경로 사용)
- 웹사이트를 만들었으면 반드시 접속 링크를 넣는다
- 게임을 만들었으면 반드시 실행 링크를 넣는다
- 대표가 이 파일 하나만 열면 모든 것을 이해하고 실행할 수 있어야 한다

## ⚠️ 필수 규칙 — 대표에게 질문할 때 (텔레그램 브릿지)

대표는 자리를 비울 때가 많다. 작업 중 대표 결정이 필요하면 **절대 채팅창에서 기다리지 말고** 아래 방법을 쓴다.

**방법:**
1. 현재 프로젝트 폴더에 `질문대기.md` 파일을 만든다
2. 파일 내용: 질문 내용만 (기술 용어 없이, 결정해야 할 것만)
3. 파일을 만들면 자동으로 대표 핸드폰으로 전송됨
4. 대표가 답장하면 같은 폴더에 `답변.md`가 생성됨
5. `답변.md`를 읽고 작업을 이어간다

**질문대기.md 예시:**
```
카드 배경을 어두운 계열로 할까요, 밝은 계열로 할까요?
A안: 검정/보라 (신비로운 느낌)
B안: 흰색/금색 (고급스러운 느낌)
```

**중요:**
- 질문은 비개발자가 이해할 수 있는 말로 쓴다
- 한 번에 하나씩만 질문한다
- 답변이 올 때까지 다른 작업을 먼저 진행한다 (멈추지 않는다)

---

## ⚠️ 필수 규칙 — 세션 종료 전 BRIEF.md 업데이트

CEO는 대화가 마무리될 때마다(또는 대표가 "잠깐 멈춰", "오늘은 여기까지" 등의 말을 하면) 반드시 프로젝트 폴더의 `BRIEF.md`를 아래 형식으로 업데이트해야 한다.

다음 세션에서 새 대화를 시작할 때 CEO가 이 파일을 읽으면 즉시 이어서 작업할 수 있어야 한다.

```markdown
# [프로젝트명] — 진행 브리프
마지막 업데이트: [날짜 시간]

## 프로젝트 목표
[한 줄 요약]

## 지금까지 완료된 것
- [완료 항목 1]
- [완료 항목 2]

## 현재 진행 중인 것
- [지금 하던 작업]

## 다음에 할 것 (우선순위 순)
1. [다음 작업 1]
2. [다음 작업 2]

## 중요 결정사항
- [이미 결정된 방향, 선택된 기술 스택 등]

## 대표 확인 필요
- [대표님이 결정해야 할 것]
```
