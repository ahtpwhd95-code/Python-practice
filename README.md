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

### Day33: MySQL / PostgreSQL 기초와 Python DB 연결

오늘은 MySQL과 PostgreSQL의 기본 개념을 학습하고, 로컬 환경에서 데이터베이스를 직접 설치하고 연결하는 실습을 진행했습니다.

MySQL Community Server를 설치한 뒤 CMD에서 `mysql -u root -p` 명령어로 접속했고, `SHOW DATABASES;`, `CREATE DATABASE`, `USE`, `SHOW TABLES;`와 같은 기본 명령어를 실습했습니다.  
또한 DBeaver를 이용해 GUI 환경에서 MySQL 연결을 만들고, SQL Editor를 통해 명령어를 실행하는 흐름도 확인했습니다.

Python에서는 `mysql-connector-python`을 설치해 MySQL과 연결하는 코드를 작성했습니다.  
이 과정에서 비밀번호 불일치처럼 보이는 1045 에러, `db is not defined` 에러, 환경 변수 PATH 문제, 코드 저장 누락 문제를 직접 겪고 해결했습니다.

#### 핵심 정리
- MySQL Community Server 설치 및 CMD 접속
- `SHOW DATABASES;`, `CREATE DATABASE`, `USE`, `SHOW TABLES;` 실습
- DBeaver 연결 생성 및 SQL Editor 사용
- Python에서 `mysql-connector-python`으로 DB 연결
- PostgreSQL 기본 계정, 포트, 드라이버 개념 정리
- DB 접속 정보와 예외 처리 구조 이해

#### Troubleshooting
- `mysql` 명령어가 CMD에서 인식되지 않아 MySQL `bin` 폴더를 PATH에 추가했음
- MySQL 명령어 끝에 세미콜론을 빼먹어 `->` 상태에 빠졌음
- Python에서 DB 연결 실패 후 `db` 변수를 참조해 `NameError`가 발생했음
- VS Code에서 코드를 수정하고 저장하지 않아 이전 코드가 계속 실행되었음
- DBeaver에서 SQL Editor와 Database Navigator 사용법을 다시 확인했음

---

### Day34: 관계형 데이터베이스와 RDB / NoSQL 이해

오늘은 관계형 데이터베이스의 기본 구조와 키, 제약조건, 복합키, 테이블 간 관계를 집중적으로 학습했습니다.

공유 킥보드 서비스를 예제로 `kickboard`, `customer`, `borrow` 테이블을 만들고, 테이블 생성, 데이터 삽입, 컬럼 수정, 테이블 삭제, 제약조건 추가와 삭제를 실습했습니다.  
특히 `borrow` 테이블을 통해 고객과 킥보드 사이의 대여 관계를 표현했고, `customer_number + rental_time`을 복합 기본키로 설정하며 복합키의 의미를 이해했습니다.

처음에는 기본키, 외래키, 제약조건, 복합키가 모두 비슷하게 느껴졌지만, 이를 물류 흐름과 연결해 생각하니 이해가 쉬워졌습니다.  
테이블은 공정별 장부, 기본키는 한 줄을 구분하는 식별자, 외래키는 다른 장부와 이어지는 연결고리, 제약조건은 잘못된 데이터가 들어오지 못하게 막는 검수 규칙으로 이해했습니다.

또한 RDB와 NoSQL의 차이를 학습하면서, 회원가입·글로사리·주문·권한처럼 구조와 관계가 명확한 데이터는 RDB에 적합하고, AI 추론 결과·로그·원본 응답처럼 구조가 유동적인 데이터는 MongoDB 같은 NoSQL에 적합하다는 관점을 정리했습니다.

#### 핵심 정리
- 데이터와 정보의 차이 이해
- 파일 처리 시스템의 한계와 데이터베이스의 필요성 정리
- RDB와 NoSQL 차이 이해
- 테이블, 속성, 튜플, 도메인 개념 정리
- `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `INSERT`, `SELECT`, `DESC` 실습
- `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT` 제약조건 학습
- 복합 기본키와 관계 테이블 이해
- DBeaver ERD를 통해 테이블 관계 시각화 확인
- 프로젝트 기준으로 RDB / NoSQL 적용 대상 구분

#### Troubleshooting
- 날짜와 시간 데이터를 입력할 때 따옴표를 붙이지 않아 INSERT 문에서 문제가 발생했음
- `information_schema.table_constraints`를 조건 없이 조회해 시스템 DB 제약조건까지 모두 출력되었음
- `DESC` 결과에서 복합키 컬럼들이 모두 `PRI`로 표시되어 처음에는 각각의 단독 기본키로 오해했음
- MySQL 접속 후 `USE est;`를 하지 않아 `No database selected` 에러가 발생했음
- DBeaver에서 `Ctrl + Enter`가 현재 SQL문만 실행한다는 것을 확인했음

#### My Understanding
- DB = 데이터가 흘러가는 유통과정
- 테이블 = 공정별 장부
- 컬럼 = 장부의 항목
- 행 = 장부의 한 줄
- PK = 한 줄을 구분하는 식별자
- FK = 다른 장부와 이어지는 연결고리
- CONSTRAINT = 잘못된 데이터가 들어오지 못하게 막는 검수 규칙
- RDB = 정해진 장부
- NoSQL = 유연한 기록지

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
- 꾸준한 기록과 복습으로 성장하는 AI 학습자