# youtube_account.py (분류기, 전문가 분석 chain)

명령: [자율 사이클 — 2026-05-28] 너는 CEO다. 작업 완료 후 자동 호출된다.

⚠️ 반드시 이 순서로:
1. /Users/kks/Desktop/kks/_company/_shared/last_report.md 읽기
   - 결과물 경로 있으면 → read_file로 실제 파일 존재 확인
   - 파일 존재 확인됨 → roadmap에서 해당 항목 ✅ 완료로 이동
   - 파일 없거나 실패 → 🔄 진행 중에서 📋 예정으로 복귀
2. /Users/kks/Desktop/kks/_company/_shared/roadmap.md 읽기
   - 🔄 진행 중 항목 있으면 → 위에서 처리 완료된 것 제외하고 모두 📋 예정으로 복귀
   - 📋 예정이 비어있으면 → 임의로 채우지 마라. 5번 판단으로 이동
3. /Users/kks/Desktop/kks/_company/_shared/goals.md 읽기 (방향 파악)
4. /Users/kks/Desktop/kks/_company/_shared/decisions.md 확인 (1시간 내 중복 방지)
5. 판단:
   - 📋 예정 있음 → 1개 골라 적합한 에이전트에게 구체적으로 지시 (무엇을/어디에/어떻게)
   - 📋 예정 없고 🔄 진행 중도 없음 → Secretary에게 "모든 작업 완료, 사용자에게 최종 결과 보고" 지시

🚫 금지:
- "다음 단계를 진행하시겠습니까?" 질문 X — 네가 결정해라
- "보고합니다" "검토했습니다" 메타 답변 X — 결과물을 만들어라
- 같은 작업 1시간 안에 두 번 X
- 작업 크다 싶으면 더 작게 쪼개서 지시

─── YouTube 계정 / 채널 설정 ───
  API 키            : AIza…CjM
  내 채널 핸들       : (없음)
  내 채널 ID        : UCEa0YtYmiRMvgRLKDigg2YA
  감시 채널 (0개) : (없음)
  경쟁 채널 (0개): (없음)
  텔레그램          : 미설정 (보고 알림 비활성)
  LLM 서버 URL      : http://127.0.0.1:8080/v1
  분석 모델          : mlx-community/Qwen3-32B-4bit

✅ 공유 설정 로드 OK. 다른 도구들이 이 값을 자동으로 사용합니다.

---

> ⚠️ LLM 추가 인사이트 단계 스킵: `connect ECONNREFUSED 127.0.0.1:8080`
> 💡 모델 오케스트레이션 모달 → 레오 모델을 더 작은 것으로 변경하면 다음번엔 인사이트도 같이 옵니다. 위 데이터 분석은 LLM 없이 정상 집계된 결과예요.
