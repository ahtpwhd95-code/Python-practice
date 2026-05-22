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
| Day39 | Style Transfer / VGG-19 / Gram Matrix / Fashion MNIST GAN 실습 |
| Day40 | LLM 발전 흐름 / GPT 계열 / 프롬프트 엔지니어링 / ChatGPT 활용 실습 |

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
├── day39_style_transfer_gan/
├── day40_prompt_engineering/
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

### Day40: 생성형 AI와 프롬프트 엔지니어링 기초

오늘은 LLM의 발전 흐름과 생성형 AI 서비스, 프롬프트 엔지니어링의 기본 개념을 학습했습니다.  
언어 모델은 단어의 등장 횟수와 확률을 기반으로 문장을 예측하던 통계적 언어 모델에서 시작해, 신경망 기반 모델, 사전학습 언어 모델, 대규모 언어 모델로 발전해왔습니다.

언어 모델의 발전 흐름은 `SLM -> NLM -> PLM -> LLM`으로 정리했습니다.  
SLM은 단어 등장 횟수와 확률을 바탕으로 문장을 예측하는 방식이고, NLM은 신경망을 활용한 언어 모델입니다.  
PLM은 비지도학습으로 사전학습한 언어 모델이며, LLM은 대규모 데이터와 파라미터를 기반으로 높은 수준의 언어 이해와 생성 능력을 가진 모델입니다.

GPT 계열 모델은 Decoder 기반 언어 모델로 발전해왔습니다.  
GPT-1은 비지도 사전학습과 지도 미세조정을 결합했고, GPT-2는 더 큰 데이터와 모델 크기를 기반으로 비지도 사전학습 중심으로 발전했습니다.  
GPT-3는 다양한 문제를 하나의 모델이 처리할 수 있도록 Meta-learning 흐름을 보여주었고, GPT-3.5는 지도학습과 인간 피드백 기반 강화학습을 활용해 대화형 AI 서비스 품질을 높였습니다.  
GPT-4 이후에는 멀티모달과 추론 성능이 강화되었고, o계열 모델과 Deep Research는 복잡한 문제 해결과 Agentic Reasoning 흐름으로 이해했습니다.

PLM과 LLM을 활용하는 대표적인 방식으로 Fine-tuning과 Prompt Engineering을 비교했습니다.  
Fine-tuning은 특정 task에 맞는 데이터셋으로 모델 가중치를 추가 학습하는 방식이고, Prompt Engineering은 모델의 가중치를 직접 수정하지 않고 자연어 지시를 설계해 원하는 결과를 유도하는 방식입니다.

실습에서는 ChatGPT를 활용해 개인 웹 홈페이지를 만들고, HTML과 CSS 파일을 분리해 `index.html`, `styles.css` 구조로 구성했습니다.  
또한 C++과 JavaScript 코드를 Python으로 변환하고, TensorFlow 코드를 PyTorch 코드로 바꾸는 실습을 진행했습니다.  
데이터 분석 코드 생성 실습에서는 pandas로 Excel 파일을 불러오고, 서울시 아파트 실거래 데이터를 기준으로 정렬, 그룹화, 평균 계산, 시각화 코드를 생성했습니다.

#### 핵심 정리
- 언어 모델은 `SLM -> NLM -> PLM -> LLM` 흐름으로 발전함
- SLM은 통계적 언어 모델, NLM은 신경망 기반 언어 모델임
- PLM은 비지도학습 기반 사전학습 언어 모델임
- LLM은 큰 규모의 PLM으로, 높은 수준의 언어 이해와 생성 능력을 가짐
- GPT 계열은 Decoder 기반 언어 모델로 발전해왔음
- Fine-tuning은 모델 가중치를 task에 맞게 추가 학습하는 방식임
- Prompt Engineering은 모델 가중치를 바꾸지 않고 입력 지시를 설계하는 방식임
- 좋은 프롬프트는 역할, 목표, 입력 정보, 출력 형식, 예시를 명확히 제공함
- 이미지 생성 프롬프트는 주제, 스타일, 프레이밍, 카메라 뷰, Negative Prompt 등을 고려함
- ChatGPT가 생성한 코드는 실행과 오류 메시지를 통해 반드시 검증해야 함

#### Troubleshooting
- SLM, NLM, PLM, LLM처럼 비슷한 약어가 많아 처음에는 구분이 헷갈렸음
  - 모델이 어떤 방식으로 언어를 학습하고 활용하는지 기준으로 정리
- GPT 모델별 차이는 이름이 비슷해 단순 암기보다 발전 흐름으로 이해할 필요가 있었음
  - 모델 크기, 사전학습, 미세조정, 멀티모달, 추론 강화 흐름으로 구분
- 프롬프트 엔지니어링은 쉬워 보이지만 원하는 결과를 얻으려면 조건을 구체적으로 작성해야 했음
  - 역할, 목표, 출력 형식, 예시를 함께 제공하는 습관이 필요함
- ChatGPT가 생성한 코드가 항상 바로 정답은 아니었음
  - 실행 결과와 오류 메시지를 통해 직접 검증해야 함

#### My Understanding
- LLM = SLM, NLM, PLM의 흐름 위에서 발전한 대규모 언어 모델
- Fine-tuning = 모델 자체를 task에 맞게 더 학습시키는 방식
- Prompt Engineering = AI에게 원하는 결과를 정확히 설명하는 방식
- 프롬프트 = 질문이 아니라 작업 지시서에 가까움
- 좋은 프롬프트 = 역할 + 목표 + 입력 + 출력 형식 + 예시
- 이미지 생성 프롬프트 = 주제와 스타일뿐 아니라 구도, 카메라, 제외 요소까지 설계
- AI 코드 생성 = 빠른 초안 생성 도구이지만 검증은 사람이 해야 함
- 프롬프트 엔지니어링은 코딩을 대체한다기보다 AI와 협업하기 위한 의사소통 방식임

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
