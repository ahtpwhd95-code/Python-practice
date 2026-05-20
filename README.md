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
| Day38 | 생성형 AI 트렌드 / 멀티모달 / AI Agent / GAN 계열 모델 |

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
├── day38_generative_ai_gan/
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

### Day38: 생성형 AI 트렌드와 GAN 계열 모델

오늘은 생성형 AI 기술 트렌드와 GAN 계열 모델의 흐름을 학습했습니다.  
최근 생성형 AI 흐름으로 멀티모달, 추론형 모델, AI Agent 개념을 정리했고, OCR, 객체 인식, 이미지 세그멘테이션, Grad-CAM처럼 이미지와 비정형 데이터를 다루는 기술도 함께 복습했습니다.

추론형 모델은 단순 질의응답보다 여러 단계의 사고 과정을 거쳐 답을 생성하는 모델로 이해했습니다.  
AI Agent는 특정 작업을 수행하기 위해 설계된 인공지능 시스템이며, 필요한 자료를 탐색하고 분석해 보고서를 만드는 Deep Research 같은 형태도 Agent의 예시로 볼 수 있습니다.  
조달청 공모전 프로젝트와 연결하면, 공공조달 데이터를 탐색하고 분석해 사용자의 의사결정을 보조하는 서비스로 확장할 수 있다는 점도 생각해봤습니다.

GAN은 생성자와 판별자가 서로 경쟁하면서 학습하는 생성형 모델입니다.  
생성자는 진짜 같은 가짜 데이터를 만들고, 판별자는 입력 데이터가 진짜인지 가짜인지 구분합니다.  
두 모델이 함께 학습되면서 생성자는 더 자연스러운 데이터를 만들고, 판별자는 더 정확하게 구분하도록 발전합니다.

DCGAN은 GAN에 CNN 구조를 도입한 모델입니다.  
생성자는 전치 합성곱으로 이미지를 점점 크게 만들고, 판별자는 스트라이드가 있는 합성곱으로 이미지를 줄이며 진짜와 가짜를 구분합니다.  
CGAN은 조건 정보를 추가해 특정 클래스나 스타일처럼 원하는 방향의 데이터를 생성할 수 있도록 확장한 모델입니다.

이미지 변환 모델에서는 pix2pix와 CycleGAN의 차이가 중요했습니다.  
pix2pix는 입력 이미지와 정답 이미지가 쌍으로 있는 paired dataset을 사용해 지도학습 방식으로 변환을 학습합니다.  
반면 CycleGAN은 paired dataset 없이 서로 다른 도메인 간 변환을 학습할 수 있으며, 변환한 이미지를 다시 원래 도메인으로 복원했을 때 원본과 비슷해야 한다는 Cycle Consistency를 핵심 원리로 사용합니다.

#### 핵심 정리
- 멀티모달은 텍스트, 이미지, 영상, 음성처럼 서로 다른 형태의 데이터를 함께 다룸
- OCR은 이미지나 문서에서 텍스트를 추출하는 기술임
- Grad-CAM은 모델이 이미지의 어느 부분을 근거로 판단했는지 시각화하는 방법임
- AI Agent는 특정 작업을 수행하기 위해 설계된 인공지능 시스템임
- GAN은 생성자와 판별자가 경쟁하면서 학습하는 생성형 모델임
- DCGAN은 CNN 구조를 GAN에 적용한 이미지 생성 모델임
- CGAN은 조건 정보를 추가해 원하는 방향으로 생성 결과를 제어함
- pix2pix는 paired dataset을 사용하는 지도학습 기반 이미지 변환 모델임
- CycleGAN은 unpaired dataset으로 도메인 변환을 학습할 수 있음
- GAN 계열 모델은 학습 안정성, 고해상도 생성, 조건 제어 같은 문제를 해결하며 발전함

#### Troubleshooting
- GAN 계열 모델 이름이 많아 각 모델의 차이가 헷갈렸음
  - 모델 이름보다 어떤 문제를 해결하려고 구조가 바뀌었는지 중심으로 정리
- DCGAN 구조에서 전치 합성곱, 스트라이드 합성곱, 배치 정규화 역할이 함께 나와 복습이 필요했음
  - CNN 기본 구성 요소를 이미지 생성 구조와 연결해 다시 확인할 예정
- WGAN, WGAN-GP, BEGAN처럼 학습 안정성을 개선한 모델은 손실 함수와 확률분포 개념이 들어가 어려웠음
  - 학습 안정성 개선 흐름을 별도로 정리할 필요가 있음

#### My Understanding
- 생성형 AI = 텍스트뿐만 아니라 이미지, 영상, 음성까지 생성하거나 변환하는 기술 흐름
- 멀티모달 = 여러 데이터 형태를 함께 이해하고 활용하는 방식
- GAN = 생성자와 판별자의 경쟁 학습 구조
- DCGAN = 이미지 생성을 위해 CNN 구조를 GAN에 적용
- CGAN = 조건을 넣어 원하는 클래스나 스타일을 생성
- pix2pix = 입력과 정답 이미지 쌍이 있는 변환 문제
- CycleGAN = 짝이 없는 두 도메인 사이의 변환 문제
- Cycle Consistency = 변환 후 다시 원래 도메인으로 되돌렸을 때 원본과 비슷해야 한다는 원리
- SchoolBridge의 OCR, 텍스트 추출, 번역, TTS 흐름도 멀티모달 관점에서 설명할 수 있음

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
