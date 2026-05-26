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
| Day41 | RAG / LangChain / Agent / Tool / 로컬 LLM과 Gemini 실습 |

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
├── day41_rag_langchain/
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

### Day41: RAG와 LangChain 기초

오늘은 RAG와 LangChain의 기본 개념을 학습하고, Jupyter Notebook 기반 실습을 진행했습니다.  
RAG는 Retrieval Augmented Generation의 약자로, 정보 검색과 생성 과정을 결합해 LLM이 더 정확하고 근거 있는 응답을 생성하도록 돕는 방법론입니다.

RAG가 없으면 LLM은 미리 학습된 데이터에만 의존하고, 모르는 내용에 대해 허위 정보를 생성할 수 있습니다.  
RAG를 적용하면 최신 정보, 내부 문서, 데이터베이스, 검색 결과 등을 근거로 활용할 수 있고, 응답에 사용되는 정보의 출처를 어느 정도 통제할 수 있습니다.  
지금까지 배운 파일 데이터 추출, SQL 기반 데이터 조회, 인터넷 검색 기반 응답 생성도 넓은 의미에서는 RAG 방식으로 이해할 수 있었습니다.

LangChain은 LLM 애플리케이션 개발을 돕는 오픈소스 프레임워크입니다.  
기존에는 정보 검색, 프롬프트 구성, 모델 호출, 응답 후처리를 직접 하나의 흐름으로 구현해야 했지만, LangChain은 PromptTemplate, LLM, OutputParser, Chain, Agent, Tool, Memory, Callback 등을 모듈처럼 조립할 수 있게 해줍니다.  
이를 통해 기능 교체, 흐름 관리, 디버깅, 확장이 쉬워진다는 점을 정리했습니다.

LangChain의 기본 작동 흐름은 `prompt | llm | output_parser`처럼 파이프라인 형태로 연결할 수 있습니다.  
PromptTemplate은 일관된 형태의 프롬프트를 자동으로 생성하고, OutputParser는 LLM 응답을 문자열, JSON, 리스트, Pydantic 모델 등 원하는 형태로 가공합니다.  
Agent는 상황에 따라 어떤 Tool을 사용할지 선택하는 LLM 기반 의사결정 엔진이고, Tool은 검색, 계산, API 호출 같은 외부 기능을 연결하는 단위입니다.

실습에서는 `Rag-practice` 폴더의 노트북을 기반으로 기존 OpenAI 코드를 일부 Gemini 기반 코드로 바꾸고, `gemini-2.5-flash-lite` 모델을 사용했습니다.  
검색 Agent 실습에서는 DuckDuckGo 검색 도구를 연결하고 `Thought / Action / Observation` 로그를 확인했습니다.  
Gemini가 Agent 형식을 가끔 틀려 `Invalid Format` 오류가 발생했지만, `handle_parsing_errors=True` 설정으로 최종 답변 생성은 가능했습니다.

로컬 LLM 실습에서는 Ollama를 설치하고 `gemma2:2b` 모델 연결을 시도했습니다.  
외부 API는 성능이 좋지만 비용, 사용량 제한, 데이터 전송 이슈가 있고, 로컬 LLM은 데이터가 외부로 전송되지 않는 장점이 있지만 하드웨어 자원과 속도 제약을 고려해야 한다는 점을 확인했습니다.

#### 핵심 정리
- RAG는 검색된 외부 정보를 LLM 답변 생성에 함께 활용하는 방식임
- RAG를 사용하면 최신 정보, 내부 문서, 데이터베이스 등을 근거로 답변할 수 있음
- LangChain은 LLM 애플리케이션을 구성하는 여러 기능을 모듈처럼 연결하는 프레임워크임
- 기본 흐름은 `PromptTemplate -> LLM -> OutputParser` 구조로 이해할 수 있음
- Agent는 어떤 Tool을 사용할지 선택하는 LLM 기반 의사결정 구조임
- Tool은 검색, 계산, API 호출 같은 외부 기능을 연결하는 단위임
- Memory는 대화 이력과 맥락을 저장하는 기능임
- Callback은 실행 과정을 추적하고 디버깅하는 데 활용됨
- 외부 API는 성능과 편의성이 좋지만 비용과 데이터 전송 이슈가 있음
- 로컬 LLM은 보안 측면의 장점이 있지만 하드웨어와 속도 제약이 있음

#### Troubleshooting
- 기존 OpenAI 코드와 Gemini 코드의 사용 방식이 달라 모델 호출 부분을 수정해야 했음
  - Gemini 기반 코드와 Ollama 기반 코드를 따로 정리할 필요가 있음
- LangChain 버전에 따라 import 경로가 달라지는 문제가 있었음
  - 실습 환경의 버전과 문서의 버전을 함께 확인해야 함
- Gemini Agent 실습 중 출력 형식이 맞지 않아 `Invalid Format` 오류가 발생했음
  - `handle_parsing_errors=True` 설정으로 최종 답변 생성은 가능했음
- Ollama 설치 후에도 PATH 문제로 `ollama` 명령이 바로 실행되지 않았음
  - 전체 실행 경로를 직접 지정해 실행함

#### My Understanding
- RAG = LLM이 답변할 때 외부 근거를 함께 참고하게 하는 구조
- LangChain = 프롬프트, 모델, 파서, 검색기, 도구를 연결하는 파이프라인 도구
- Chain = 입력부터 출력까지 이어지는 실행 흐름
- Agent = 상황에 따라 도구를 고르는 구조
- OutputParser = 모델 응답을 원하는 형식으로 정리하는 단계
- SchoolBridge의 slot protection, glossary, template, 후처리 검증 구조도 LangChain 관점에서 다시 해석할 수 있음
- 앞으로 RAG를 사용할 때는 단순 챗봇보다 근거가 남는 답변 구조를 우선 설계해야 함

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
