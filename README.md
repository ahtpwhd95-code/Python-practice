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
| Day37 | SQL 마무리 / DB 백업과 복원 / JSON 파싱 / 생성형 AI 윤리 |

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
├── day37_sql_json_ai/
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

### Day37: SQL 마무리, DB 백업과 복원, JSON 파싱, 생성형 AI 윤리

오늘은 관계형 데이터베이스 수업을 마무리하며 SQL 문제 풀이와 DB 백업/복원 흐름을 복습했습니다.  
`JOIN`으로 여러 테이블을 연결하고, `WHERE`, `GROUP BY`, `ORDER BY`를 함께 사용해 조건에 맞는 데이터를 조회하는 문제를 풀었습니다.

SQL 문제를 풀 때는 문법을 바로 작성하기보다 출력해야 하는 컬럼이 어느 테이블에 있는지 먼저 확인하는 과정이 중요하다는 점을 다시 느꼈습니다.  
특히 카드사별 수수료 계산 문제에서는 집계 함수와 계산 컬럼을 함께 사용했고, 문제 조건에 따라 `ROUND()`로 반올림 처리를 해야 한다는 점을 확인했습니다.

DB 백업과 복원에서는 `mysqldump`와 `mysql` 명령어를 실습했습니다.  
`mysqldump`는 데이터베이스 내용을 SQL 파일로 내보내는 데 사용하고, `mysql`은 SQL 파일을 다시 데이터베이스로 가져올 때 사용합니다.  
이 과정에서 `>`는 내보내기, `<`는 가져오기 방향이라는 점을 정리했습니다.

이후 데이터 포맷으로 XML과 JSON을 학습했습니다.  
JSON은 키-값 구조의 텍스트 기반 데이터 표현 방식이며, 통신 방법이나 프로그래밍 문법 자체가 아니라 데이터를 저장하고 교환하기 위한 형식이라는 점을 정리했습니다.  
Python에서는 `json` 라이브러리를 사용해 JSON 파일을 Python 객체로 읽거나, Python 객체를 JSON 파일로 저장할 수 있습니다.

마지막으로 생성형 AI의 개념과 윤리 문제를 함께 다뤘습니다.  
생성형 AI는 텍스트, 이미지, 영상 등 새로운 콘텐츠를 생성할 수 있지만, 할루시네이션, 개인정보, 저작권, 편향성 문제를 함께 고려해야 한다는 점이 중요했습니다.

#### 핵심 정리
- SQL 문제를 풀 때는 필요한 컬럼이 어느 테이블에 있는지 먼저 확인해야 함
- `JOIN`은 `ON 테이블1.컬럼 = 테이블2.컬럼` 구조로 연결 조건을 작성함
- `GROUP BY`와 집계 함수를 사용하면 그룹 단위 계산이 가능함
- 계산식이 맞더라도 `ROUND()` 같은 출력 조건을 놓치면 정답이 달라질 수 있음
- `mysqldump`는 DB를 SQL 파일로 백업할 때 사용함
- `mysql < 파일.sql`은 SQL 파일을 DB로 복원할 때 사용함
- `>`는 내보내기, `<`는 가져오기 방향으로 이해할 수 있음
- JSON은 키-값 구조의 데이터 표현 형식임
- `json.load()`는 JSON 파일을 Python 객체로 읽음
- `json.dump()`는 Python 객체를 JSON 파일로 저장함
- 생성형 AI 결과는 검증과 윤리적 사용이 함께 필요함

#### Troubleshooting
- `JOIN` 조건 작성에서 어떤 컬럼끼리 연결해야 하는지 헷갈렸음
  - 테이블 구조를 먼저 보고 공통 기준이 되는 키를 찾는 방식으로 해결
- 카드사 수수료 계산 문제에서 반올림 조건을 처음에 놓쳤음
  - 출력 컬럼, 정렬 조건, 반올림 여부를 문제에서 먼저 표시해두는 습관이 필요함
- DB 백업과 복원에서 `>`와 `<` 방향이 헷갈렸음
  - `>`는 파일로 내보내기, `<`는 파일에서 가져오기라고 정리

#### My Understanding
- SQL 문제 풀이 = 테이블 구조 확인 → 필요한 컬럼 찾기 → 조인 조건 작성 → 조건/집계/정렬 적용
- `JOIN` = 흩어진 테이블을 기준 컬럼으로 연결하는 방법
- `GROUP BY` = 같은 기준끼리 묶어서 계산하는 방법
- `mysqldump` = 현재 DB를 SQL 파일로 저장
- `mysql < backup.sql` = SQL 파일 내용을 DB에 다시 적용
- JSON = 데이터를 주고받기 위한 키-값 기반 텍스트 형식
- `load` / `dump` = 파일 기준
- `loads` / `dumps` = 문자열 기준
- 생성형 AI = 편리한 생성 도구이지만 검증과 책임이 필요한 기술

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
