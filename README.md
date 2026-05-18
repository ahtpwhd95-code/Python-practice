# Python-to-AI

Python 기초부터 머신러닝, 딥러닝, NLP, 벡터 검색, API/풀스택, Linux/Docker, Speech AI, 데이터베이스 실습까지의 학습 과정을 기록한 저장소입니다.  
AI Human 교육 과정을 기반으로, 직접 작성한 코드와 복습 내용, 실습 프로젝트, 시각화 자료를 함께 정리하고 있습니다.

---

## 📌 About

이 저장소는 단순한 코드 모음이 아니라,  
**Python → ML → DL → NLP → Vector Search → Linux/Docker → Speech AI → Database → AI 프로젝트**로 이어지는 학습 흐름을 정리한 공간입니다.

- 직접 작성한 코드 중심
- 복습 기반 학습 기록
- 개념과 실습을 함께 정리
- 시행착오와 디버깅 과정까지 기록
- 프로젝트 경험을 바탕으로 개념을 다시 해석하고 연결

---

## 🛠 Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn
- TensorFlow / Keras
- PyTorch
- Transformers
- ChromaDB
- FastAPI
- Streamlit
- Flask
- SQLite3
- MySQL
- PostgreSQL
- MongoDB
- Linux / Ubuntu
- Docker
- Audio / Speech Processing
- Git / GitHub

---

## 🎯 Current Focus

- Python 기반 문제 해결력 강화
- 머신러닝 / 딥러닝 핵심 개념 정리
- NLP와 Transformer 구조 이해 및 실습
- Linux / Docker 기초와 컨테이너 환경 이해
- STT / TTS / 음성 데이터 처리 흐름 이해
- 음성 명령 기반 데스크톱 어시스턴트 구현 실습
- 관계형 데이터베이스와 NoSQL의 차이 이해
- 데이터 구조, 키, 제약조건, 테이블 관계 설계 학습
- 벡터 검색, FastAPI, Flask, 풀스택 프로젝트 경험 확장
- SQL 조건 조회, 집계, JOIN, 서브쿼리를 통한 데이터 조회 흐름 이해
- SQL 집합 연산, 재귀 CTE, 윈도우 함수를 활용한 고급 조회 흐름 이해

---

## 🚀 Featured Projects

- **[SchoolBridge - 다문화 가정 학교 안내 AI 서비스](https://github.com/Maxmunzy/multicultural-ai)**
  - 다문화 가정 학부모를 위한 학교 가정통신문 분석·번역·TTS 서비스
  - 공지 원문에서 할 일 문장을 추출하고, 일정 / 준비물 / 제출 / 비용 / 건강·안전 / 기타 항목으로 분류
  - NLLB 번역 모델과 글로사리, 슬롯 보호, 후처리 구조를 결합해 학교 도메인 용어와 날짜·금액·URL 같은 핵심 정보를 보존
  - Android 앱, FastAPI 서버, 모델 파이프라인, TTS 기능을 연결한 팀 프로젝트
  - 단순 생성형 AI API 의존이 아니라, 규칙·검수·파이프라인 구조로 서비스 품질을 제어하는 방향으로 설계

- **[Day20 API Project](./day20_api/)**
  - 공공데이터 OpenAPI 호출 및 페이지네이션 처리
  - `pandas` 기반 데이터 정리 및 `folium` 지도 시각화 실습

- **[Day21 Chatbot Project](./day21_chatbot/)**
  - 텍스트 전처리 및 패턴 매칭 기반 챗봇 구현
  - 입력 문장에 따라 적절한 응답을 반환하는 간단한 대화 시스템 실습

- **[Day23 Attention NMT Project](./day23_attention_nmt/)**
  - Seq2Seq + Attention 기반 번역 모델 구현
  - 전처리 최적화로 학습 효율을 개선하며 성능 향상 과정을 경험

- **[Day24 Furniture Awards AI](./day24_Chroma_Fullstack/)**
  - DINOv2 + ChromaDB 기반 가구 이미지 유사도 검색 프로젝트
  - Streamlit 프로토타입과 FastAPI + HTML/JS 풀스택 구조를 함께 구현

- **[Day25 FridgeCook Project](./day25_FridgeCook/)**
  - 냉장고 재료를 기반으로 레시피를 추천하는 Flask 웹 프로젝트
  - SQLite 레시피 데이터, 정규표현식 전처리, 단계별 조리 구조를 함께 구현

---

## 🎨 Interactive Visual Notes

- **[Transformer Interactive Flow](./visual_notes/transformer_interactive_flow.html)**
  - Transformer의 전체 처리 흐름을 시각적으로 복습할 수 있는 인터랙티브 페이지

- **[CNN/RNN/LSTM/GRU Interactive Flow](./visual_notes/cnn_rnn_lstm_gru_interactive_flow.html)**
  - CNN과 RNN 계열 모델의 핵심 흐름을 시각적으로 복습할 수 있는 인터랙티브 페이지

---

## 📚 Learning Log

| Day   | Topic |
|------|------|
| Day02 | Python 기본 문법 |
| Day03 | 클래스 / 상속 |
| Day04 | 미니 게임 구현 |
| Day05 | 문제 풀이 |
| Day06 | 파일 처리 |
| Day07 | Git / GitHub |
| Day08 | NumPy |
| Day09 | 선형대수 / 통계 |
| Day10 | 전처리 / 시각화 |
| Day11 | 머신러닝 입문 |
| Day12 | 데이터 분석 기초 |
| Day13 | 클러스터링 / PCA |
| Day14 | 의사결정나무 / 앙상블 |
| Day15 | 딥러닝 기초 / 퍼셉트론 |
| Day16 | TensorFlow / MLP 기초 |
| Day17 | CNN 기초 및 이미지 분류 개념 |
| Day18 | 이미지 데이터 이해와 PyTorch 파이프라인 구현 |
| Day19 | 순차 데이터와 RNN 기초 / 온도 예측 앙상블 실험 |
| Day20 | OpenAPI 기초 / 공공데이터 API / 페이지네이션 / 지도 시각화 |
| Day21 | NLP 기초 / 텍스트 전처리 / 챗봇 구현 |
| Day22 | NLP 심화 / Naive Bayes / Cosine Similarity |
| Day23 | Seq2Seq + Attention 번역 모델 구현 / 성능 최적화 |
| Day24 | DINOv2 / ChromaDB / Streamlit → FastAPI 풀스택 프로젝트 |
| Day25 | Flask / SQLite / 레시피 추천 웹 프로젝트 |
| Day26 | Transformer 아키텍처 / 사전학습 / 미세조정 / 듀얼 인코더 실습 |
| Day27 | Linux / Ubuntu / Vim / WSL2 환경 이해 / KoGPT-2 챗봇 페르소나 매핑 |
| Day28 | 정규표현식 / grep / 리다이렉션 / 파이프 / mount / 프로세스 관리 / crontab / SSH |
| Day29 | Docker 기초 / 이미지와 컨테이너 / 볼륨 / 환경변수 / Redis / MariaDB / WordPress 실습 |
| Day30 | Docker 심화 / 다중 컨테이너 / Docker Network / Kubernetes 기초 |
| Day31 | 음성인식 / 음성합성 / STT / TTS / Fourier Transform / STFT / CTC / RNN-T 기초 |
| Day32 | Speech AI 실습 / Tacotron2 TTS / Whisper STT / 음성 명령 데스크톱 어시스턴트 / Freesound Audio Tagging 코드 보완 |
| Day33 | MySQL / PostgreSQL 기초 / DBeaver / Python DB 연결 |
| Day34 | 관계형 데이터베이스 / 키 / 제약조건 / 복합키 / RDB와 NoSQL |
| Day35 | SQL 조회 / 집계 함수 / GROUP BY / JOIN / 서브쿼리 실습 |
| Day36 | SQL 고급 조회 / 집합 연산 / 재귀 CTE / 윈도우 함수 / ROLLUP |

---

## 📂 Structure

```text
Python-to-AI/
├── day02_python_basics/
├── day03_oop/
├── day04_mini_game/
├── day05/
├── day06/
├── day07/
├── day08_numpy/
├── day09_linear_algebra_statistics_probability/
├── day10_practice/
├── day11_ml/
├── day12/
├── day13_ml/
├── day14_ml/
├── day15_dl/
├── day16_dl/
├── day17_dl_cnn/
├── day18_pytorch/
├── day19_rnn/
├── day20_api/
├── day21_chatbot/
├── day22_nlp_advance/
├── day23_attention_nmt/
├── day24_Chroma_Fullstack/
├── day25_FridgeCook/
├── day26_transformer/
├── day27_linux/
├── day28_linux_system/
├── day29_docker/
├── day30_docker_kubernetes/
├── day31_speech_ai/
├── day32_speech_ai/
├── day33_db_connection/
├── day34_db_relationship/
├── day35_sql_query/
├── day36_sql_advanced/
├── visual_notes/
│   ├── index.html
│   ├── python_basics_summary.html
│   ├── ml_flow_summary.html
│   ├── cnn_rnn_lstm_gru_interactive_flow.html
│   ├── transformer_interactive_flow.html
│   ├── linux_docker_interactive_flow_animated.html
│   ├── speech_ai_interactive_flow.html
│   └── project_journey_map.html
└── README.md
```

---

## 🔥 Recent Update

### Day36: SQL 고급 조회, 집합 연산, 재귀 CTE, 윈도우 함수

오늘은 MySQL 환경에서 SQL 고급 조회 문법을 실습했습니다.  
단순 조회와 JOIN, 서브쿼리 복습을 넘어 여러 결과를 합치는 집합 연산, 계층형 데이터를 조회하는 재귀 CTE, 순위와 비율을 계산하는 윈도우 함수를 중심으로 학습했습니다.

먼저 `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT`를 사용해 여러 SELECT 결과를 합치거나 비교하는 방법을 실습했습니다.  
`UNION ALL`은 중복을 포함해 결과를 모두 합치고, `UNION`은 중복을 제거한다는 차이를 확인했습니다.  
`INTERSECT`는 양쪽 결과에 모두 존재하는 데이터, `EXCEPT`는 앞쪽 결과에만 존재하는 데이터를 조회하는 방식으로 이해했습니다.

이후 `WITH RECURSIVE`를 사용해 관리자-직원, 멘토-멘티처럼 위아래 관계가 있는 데이터를 계층형으로 조회했습니다.  
최상위 데이터는 `manager_id IS NULL` 또는 `mento_id IS NULL` 조건으로 찾고, 이후 CTE 자기 자신을 다시 조인하여 다음 계층을 반복해서 찾는 구조를 실습했습니다.

JOIN에서는 `ON`과 `USING`의 차이를 다시 정리했습니다.  
`USING`은 양쪽 테이블에 같은 이름의 컬럼이 있을 때 짧게 사용할 수 있고, `ON`은 컬럼명이 다르거나 조건을 직접 작성해야 할 때 사용하는 더 넓은 범위의 문법이라는 점을 이해했습니다.

윈도우 함수에서는 `RANK()`, `SUM() OVER()`, `CUME_DIST()`, `NTILE()`을 실습했습니다.  
`GROUP BY`가 행을 묶어서 줄이는 방식이라면, 윈도우 함수는 기존 행을 유지하면서 순위, 합계, 비율, 그룹 번호 같은 계산 결과를 컬럼처럼 붙이는 방식이라는 점을 정리했습니다.

마지막으로 `GROUP BY ... WITH ROLLUP`을 사용해 그룹별 합계뿐만 아니라 중간 합계와 전체 합계까지 함께 조회하는 방법을 실습했습니다.

#### 핵심 정리
- `UNION ALL`은 중복 포함, `UNION`은 중복 제거 후 결과를 합침
- `INTERSECT`는 교집합, `EXCEPT`는 차집합처럼 이해할 수 있음
- `WITH RECURSIVE`는 시작점과 반복 규칙으로 계층형 데이터를 조회함
- 재귀 CTE에서 자기 자신을 조인하는 이유는 지금까지 찾은 중간 결과를 기준으로 다음 계층을 찾기 위함
- `ON`은 직접 조인 조건을 작성하는 방식이고, `USING`은 같은 이름 컬럼끼리 연결할 때 쓰는 축약형
- 윈도우 함수는 행을 줄이지 않고 계산 결과를 옆에 붙임
- `OVER` 안의 `ORDER BY`는 계산 기준이고, 마지막 `ORDER BY`는 출력 순서
- 윈도우 함수 결과에 조건을 걸려면 서브쿼리로 한 번 감싸야 함
- `RANK()`는 동점자에게 같은 순위를 부여하고 다음 순위를 건너뜀
- `NTILE(n)`은 데이터를 n개의 그룹으로 나눔
- `ROLLUP`은 그룹별 합계뿐만 아니라 중간 합계와 전체 합계까지 출력함

#### Troubleshooting
- 테이블명을 작은따옴표로 작성해 SQL 문법 오류가 발생했음
  - `FROM 'member'`는 문자열로 인식되므로 잘못된 작성
  - 테이블명은 `FROM member` 또는 `FROM \`member\``처럼 작성해야 함
- 재귀 CTE에서 `SELECT *`를 사용하면 컬럼 개수와 순서가 맞지 않을 수 있다는 점을 확인함
  - 시작 SELECT와 반복 SELECT의 컬럼 개수, 순서가 같아야 함
- `NTILE`을 별칭으로 그대로 사용해 문법 오류가 발생했음
  - `NTILE`은 함수 이름이므로 `AS \`NTILE\``처럼 백틱을 사용하거나 `tile_group` 같은 다른 별칭을 사용하는 것이 안전함
- 윈도우 함수에서 만든 별칭을 같은 SELECT문의 `WHERE`에서 바로 사용할 수 없었음
  - SQL 실행 순서상 `WHERE`가 `SELECT`보다 먼저 실행되므로 서브쿼리로 감싸야 함
- `OVER` 안의 `ORDER BY`와 마지막 `ORDER BY`의 역할이 달라 헷갈렸음
  - `OVER` 안의 정렬은 계산 기준, 마지막 정렬은 출력 순서임

#### My Understanding
- `UNION ALL` = 중복 포함해서 모두 붙이기
- `UNION` = 붙인 뒤 중복 제거
- `INTERSECT` = 양쪽에 모두 있는 데이터
- `EXCEPT` = 앞쪽에는 있고 뒤쪽에는 없는 데이터
- `WITH RECURSIVE` = 최상위 데이터부터 시작해 아래 계층을 반복해서 찾는 방식
- `cte` = 완성된 테이블이라기보다 지금까지 찾은 중간 결과
- `ON` = 직접 조인 조건을 작성하는 큰 범위
- `USING` = 같은 이름 컬럼끼리 조인할 때 쓰는 축약형
- `GROUP BY` = 행을 묶어서 줄임
- `윈도우 함수` = 행은 유지하고 계산 결과만 옆에 붙임
- `PARTITION BY` = 윈도우 함수에서 계산할 그룹 기준
- `CUME_DIST` = 정렬 기준에 따른 누적 백분율
- `NTILE` = 정렬 기준에 따라 데이터를 여러 그룹으로 나누는 함수
- `ROLLUP`의 `NULL` = 실제 NULL이 아니라 합계 행을 의미할 수 있음

---

## 📖 Study Rules

- 매일 학습 내용 기록
- 직접 코드 작성
- 복습 후 정리
- GitHub 업로드
- 단순 문법 암기보다 구조와 흐름 중심으로 이해
- 프로젝트 경험과 수업 개념을 연결해서 정리

---

## 📝 Note

프로젝트 진행 상황과 복습 일정에 따라  
업로드 간격이 일정하지 않을 수 있습니다.

단순히 진도를 나가는 것보다,  
**이해한 내용을 다시 정리하고 직접 구현하는 학습**을 목표로 하고 있습니다.

최근에는 수업에서 배운 개념을 개인 프로젝트와 팀 프로젝트의 구조에 연결해보며,  
코딩 자체뿐 아니라 데이터 흐름, 서비스 설계, 검수 구조까지 함께 이해하는 방향으로 학습하고 있습니다.

---

## 👨‍💻 Author

- GitHub: [mosejong](https://github.com/mosejong)
- Python부터 AI 프로젝트까지 직접 만들고 기록하며 성장 중
- 현실의 업무 흐름을 데이터와 서비스 구조로 바꾸는 개발자를 목표로 학습하고 있습니다.