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
| Day42 | Pillow / MongoDB / RAG&LLM / Gemini API / STT-TTS 구조 |
| Day43 | 강화학습 / Q-Learning / Policy Gradient / SFT / LoRA / DPO |

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
├── day42_mongodb_rag_assistant/
├── day43_reinforcement_learning_llm/
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

### Day43: 강화학습과 LLM 학습 흐름

오늘은 강화학습의 기본 개념부터 Q-Learning, Policy Gradient, LLM 학습에서의 SFT와 Preference/DPO 흐름까지 학습했습니다.  
강화학습은 에이전트가 환경 안에서 행동을 선택하고, 그 결과로 받은 보상을 기준으로 더 나은 행동을 찾아가는 학습 방식입니다.

강화학습의 주요 구성요소는 Agent, Environment, State, Action, Reward입니다.  
MDP는 강화학습 문제를 수학적으로 표현하는 틀이며, 가능한 상태 집합 `S`, 행동 집합 `A`, 전이 함수 `P`, 보상 함수 `R`, 감가율 `γ`로 구성됩니다.  
Q함수는 현재 상태에서 특정 행동을 했을 때 기대되는 누적 보상의 값을 나타냅니다.

Q-Learning 실습에서는 Q-table을 사용해 각 상태에서 각 행동이 얼마나 좋은지 저장하고 업데이트했습니다.  
`np.argmax(Q[state, :])`는 선택할 행동의 위치를 구할 때 사용하고, `np.max(Q[next_state, :])`는 다음 상태에서 얻을 수 있는 가장 큰 Q값 자체를 구할 때 사용합니다.  
Epsilon-Greedy는 일정 확률로 탐험하고 나머지 확률로 현재 가장 좋은 행동을 선택해 탐험과 활용의 균형을 맞추는 방법입니다.

Taxi-v3와 FrozenLake에서는 이산 상태/행동 환경에서 Q-Learning을 실습했습니다.  
CartPole에서는 REINFORCE 알고리즘을 사용해 정책 모델이 각 행동을 선택할 확률을 출력하고, Categorical 분포에서 행동을 샘플링하는 흐름을 확인했습니다.  
Gymnasium에서는 종료 조건이 `done`과 `truncated`로 나뉘며, 정식 규칙을 따르려면 `done = done or truncated`처럼 처리해야 한다는 점을 확인했습니다.

Pendulum-v1은 연속 action 환경이므로 단순한 Categorical 기반 Policy Gradient로는 적합하지 않았다.  
이를 통해 강화학습에서는 상태 공간과 행동 공간의 특성에 맞는 알고리즘을 선택해야 한다는 점을 배웠습니다.  
또한 RC카 예시를 통해 최단거리만 reward로 삼으면 실제 성능과 어긋날 수 있으며, reward 설계가 문제 정의의 핵심이라는 점을 이해했습니다.

오후에는 강화학습 개념이 LLM 학습으로 연결되었습니다.  
LLM 학습 흐름은 사전학습, SFT/모방학습, Preference/RLHF/DPO로 정리할 수 있습니다.  
SFT는 질문과 모범답변을 보고 답변 형식을 따라 배우는 단계이고, Preference 데이터는 `chosen`과 `rejected`를 비교해 어떤 답변이 더 좋은지 학습하는 데 사용됩니다.  
KoAlpaca LoRA SFT 실습에서는 전체 파라미터 중 약 0.2184%만 학습 가능한 상태로 효율적인 파인튜닝을 진행했지만, 짧은 학습만으로 정확한 지식 답변을 안정적으로 만들기는 어렵다는 점을 확인했습니다.

#### 핵심 정리
- 강화학습은 보상의 합을 최대화하는 방향으로 행동을 개선하는 학습 방식임
- MDP는 강화학습 문제를 표현하기 위한 수학적 틀임
- Q-table은 각 상태에서 각 행동의 가치를 저장하는 표임
- `argmax`는 어떤 행동을 선택할지, `max`는 그 행동의 가치가 얼마인지 구할 때 사용함
- Epsilon-Greedy는 탐험과 활용의 균형을 맞추기 위한 방법임
- CartPole에서는 `done`과 `truncated`를 함께 처리해야 원래 규칙을 유지할 수 있음
- Pendulum처럼 연속 action 환경에는 PPO, DDPG, TD3, SAC 같은 알고리즘이 더 적합함
- Reward 설계는 강화학습 문제 정의의 핵심임
- SFT는 모범답변을 따라 배우는 단계이고, Preference/DPO는 더 좋은 답변을 선호하도록 조정하는 단계임
- LoRA는 전체 모델이 아니라 작은 어댑터만 학습해 효율적으로 파인튜닝하는 방법임

#### Troubleshooting
- 강화학습 코드에서 `state`, `action`, `reward`, `next_state`, `done`, `truncated` 흐름을 놓치기 쉬웠음
  - 실습 코드를 상태 전이와 업데이트 위치 중심으로 다시 읽을 필요가 있음
- Policy Gradient와 REINFORCE는 episode 수집 후 학습하는 흐름이 Q-Learning보다 직관적이지 않았음
  - episode 수집 단계와 학습 단계를 나누어 정리할 예정
- DPO 실습에서 `DPOConfig` import, 데이터셋 변수, tensor dtype 관련 오류가 발생했음
  - 라이브러리 버전과 데이터 포맷을 다시 맞춰볼 필요가 있음

#### My Understanding
- 강화학습 = 좋은 행동의 기준을 reward로 정의하고 반복적으로 개선하는 시스템
- Q-Learning = Q값을 업데이트하며 좋은 행동 정책을 찾는 방식
- Policy Gradient = 행동 확률을 직접 학습하는 방식
- 환경과 알고리즘의 궁합 = 상태/행동 공간이 이산인지 연속인지 먼저 확인해야 함
- LLM의 action = 다음 토큰 선택
- LLM의 reward = 답변 품질, 안전성, 선호도
- SFT = 답변 형식과 패턴을 따라 배우는 단계
- DPO = chosen 답변이 rejected 답변보다 선호되도록 조정하는 단계
- AI 모델 개발은 코드를 작성하는 일뿐 아니라 문제와 평가 기준을 설계하는 일임

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
