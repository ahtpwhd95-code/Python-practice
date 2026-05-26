# 2026-05-26 TIL - RAG와 LangChain 기초

## 오늘 학습한 내용

### 1. RAG 개념

- RAG는 Retrieval Augmented Generation의 약자로, 정보 검색과 생성 과정을 결합해 더 정확한 응답을 생성하는 방법론이다.
- RAG가 없으면 LLM은 미리 학습된 데이터에만 의존하고, 모르는 내용에 대해 허위 정보를 생성할 수 있다.
- RAG를 적용하면 최신 정보, 내부 문서, 데이터베이스, 검색 결과 등을 근거로 활용할 수 있다.
- 응답에 사용되는 정보의 출처를 어느 정도 통제할 수 있다는 점도 중요하다.
- 지금까지 배운 파일 데이터 추출, SQL 기반 데이터 조회, 인터넷 검색 기반 응답 생성도 넓은 의미에서는 RAG 방식으로 볼 수 있다.

---

### 2. LangChain 개념과 필요성

- LangChain은 거대 언어 모델을 활용한 애플리케이션 개발을 돕는 오픈소스 프레임워크이다.
- 기존에는 정보 검색, 프롬프트 구성, 모델 호출, 응답 후처리를 하나의 흐름으로 직접 구현해야 했다.
- LangChain은 각 기능을 모듈화하여 PromptTemplate, LLM, OutputParser, Chain, Agent, Tool, Memory, Callback 등을 조립할 수 있게 해준다.
- 이를 통해 기능 교체, 흐름 관리, 디버깅, 확장이 쉬워진다.

---

### 3. LangChain 기본 작동 원리

- 기본 흐름은 사용자 입력, 프롬프트 템플릿 적용, LLM 응답 생성, OutputParser 적용, 최종 응답 반환으로 이어진다.
- 핵심 구조는 `prompt | llm | output_parser`처럼 파이프라인 형태로 연결할 수 있다.
- PromptTemplate은 일관된 형태의 프롬프트를 자동으로 생성한다.
- OutputParser는 LLM 응답을 문자열, JSON, 리스트, Pydantic 모델 등 원하는 형태로 가공한다.

```text
사용자 입력 -> PromptTemplate -> LLM -> OutputParser -> 최종 응답
```

---

### 4. Agent, Tool, Memory, Callback

- Agent는 LLM 기반의 의사결정 엔진으로, 상황에 따라 어떤 Tool을 사용할지 선택한다.
- Tool은 검색, 계산, API 호출 등 LLM이 단독으로 처리하기 어려운 외부 기능을 연결하는 단위이다.
- Memory는 이전 입력, 대화 이력, 맥락을 저장해 대화 흐름을 유지하는 기능이다.
- Callback은 실행 과정 추적 도구로, 디버깅, 모니터링, 실험 기록에 활용할 수 있다.

---

### 5. 로컬 LLM과 외부 API의 차이

- ChatGPT, Gemini 같은 외부 API는 성능이 좋지만 호출 비용, 사용량 제한, 데이터 전송 이슈가 있다.
- 로컬 LLM은 외부 서버가 아닌 내부 환경에서 직접 모델을 실행하기 때문에 데이터가 외부로 전송되지 않는 장점이 있다.
- 하지만 구현 난이도가 높고, 하드웨어 자원이 많이 필요하며, 긴 문서나 PDF context를 처리할 때 속도가 느릴 수 있다.
- 오늘 실습에서는 Ollama를 설치하고 `gemma2:2b` 모델 연결을 시도했다.
- PATH 문제로 `ollama` 명령 대신 전체 경로를 사용해야 했다.

---

### 6. 오늘 실습 내용

- `Rag-practice` 폴더에서 Jupyter Notebook 기반으로 실습했다.
- 기존 OpenAI 기반 코드를 일부 Gemini 기반 코드로 변경했다.
- 주로 `gemini-2.5-flash-lite` 모델을 사용했다.
- 검색 Agent 실습에서는 DuckDuckGo 검색 도구를 연결했고, `Thought / Action / Observation` 로그를 확인했다.
- Gemini가 Agent 형식을 가끔 틀려 `Invalid Format`이 발생했지만, `handle_parsing_errors=True` 설정으로 최종 답변 생성은 가능했다.
- PDF 챗봇 실습에서는 `PyPDFLoader`를 사용해 PDF 문서를 불러오는 구조를 확인했다.
- OutputParser 실습에서는 `DatetimeOutputParser`, `StrOutputParser` 등을 사용해 응답을 원하는 형태로 가공하는 방법을 확인했다.
- Chain 실습에서는 `PromptTemplate -> Gemini LLM` 구조로 `chain = prompt | llm` 형태의 연결 방식을 실습했다.

---

### 7. 프로젝트와 연결해서 이해한 점

- LangChain의 기본 흐름은 SchoolBridge 번역 파이프라인과 구조적으로 유사하다고 느꼈다.
- SchoolBridge에서도 입력 문장, slot protection, glossary/template 적용, NLLB 번역, 후처리/검수, 최종 응답 흐름을 만들었다.
- LangChain을 배우기 전에도 입력, 처리, 모델 호출, 후처리, 검수로 이어지는 도메인 특화 AI 파이프라인을 직접 구현한 경험이 있었다.
- 앞으로 RAG/LangChain을 배우면 기존 프로젝트에서 감으로 설계했던 구조를 더 표준화된 방식으로 이해하고 확장할 수 있을 것 같다.

---

## RAG 전체 흐름

```text
문서 로드
-> 텍스트 분할
-> 임베딩
-> 벡터DB 저장
-> 관련 문서 검색
-> LLM 답변 생성
-> 출처/근거 반환
```

---

## 핵심 개념 정리

| 개념 | 정리 |
|---|---|
| RAG | 검색된 외부 정보를 LLM 답변 생성에 함께 활용하는 방식 |
| LangChain | LLM 애플리케이션 개발을 위한 프레임워크 |
| PromptTemplate | 일관된 프롬프트 형식을 만드는 도구 |
| OutputParser | LLM 응답을 원하는 형식으로 가공하는 도구 |
| Chain | Prompt, LLM, Parser 등을 연결한 실행 흐름 |
| Agent | 상황에 따라 사용할 Tool을 선택하는 의사결정 구조 |
| Tool | 검색, 계산, API 호출 같은 외부 기능 연결 단위 |
| Memory | 이전 대화나 맥락을 저장하는 기능 |
| Callback | 실행 과정을 추적하고 디버깅하는 기능 |

---

## 오늘의 회고

### 배운 점

- RAG는 단순히 검색 기능이 아니라, LLM이 답변할 때 외부 정보나 내부 데이터를 근거로 사용할 수 있게 하는 구조이다.
- LangChain은 LLM 자체가 아니라, 프롬프트, 모델, 파서, 검색기, 도구 등을 연결하는 프레임워크이다.
- `PromptTemplate -> LLM -> OutputParser` 흐름이 AI 서비스 파이프라인의 기본 구조와 비슷하다는 것을 알게 되었다.
- Agent는 LLM이 상황에 따라 Tool을 선택하는 구조이고, Callback은 실행 과정을 추적하는 데 사용할 수 있다.
- 로컬 LLM은 보안이나 내부망 환경에서는 장점이 있지만, 실제 사용을 위해서는 성능과 하드웨어 제약을 함께 고려해야 한다.

### 어려운 점 / 개선할 점

- 기존 OpenAI 코드와 Gemini 코드의 사용 방식이 달라서 모델 호출 부분을 수정해야 했다.
- LangChain 버전에 따라 import 경로가 달라지는 문제가 있었다.
- Gemini Agent 실습 중 출력 형식이 맞지 않아 `Invalid Format` 오류가 발생했다.
- Gemini 무료 사용량 제한 때문에 셀을 여러 번 실행하면 RPM/RPD 제한에 걸릴 수 있다.
- Ollama는 설치 후에도 PATH 문제 때문에 전체 실행 경로를 직접 지정해야 했다.
- 로컬 LLM은 PDF context가 길어질수록 속도가 느려질 수 있어, 먼저 짧은 질문으로 동작을 확인하는 과정이 필요하다.

---

## 다음에 복습할 것

- `prompt | llm | output_parser` 흐름을 작은 예제로 다시 복습하기
- RAG 흐름을 문서 기준으로 정리하기
- Gemini 기반 코드와 Ollama 기반 코드를 따로 정리하기
- 외부 API 방식과 로컬 LLM 방식 비교하기
- SchoolBridge 번역 파이프라인을 LangChain 관점에서 다시 해석하기
- 다음 프로젝트에서 RAG를 사용한다면 근거가 남는 답변 구조를 우선 설계하기

---

## 참고자료

- 수업 실습 자료: RAG / LangChain 실습 노트북
- `Rag-practice` 폴더
- LangChain Agent 실습 노트북
- LangChain OutputParser 실습 노트북
- LangChain Chain 구조 실습 노트북
- `키오스크(무인정보단말기) 이용실태 조사.pdf`
- Gemini API 실습 코드
- Ollama 로컬 LLM 실습 코드

---

## 한 줄 정리

RAG와 LangChain은 LLM을 단순 호출하는 단계를 넘어, 외부 정보 검색과 프롬프트 구성, 모델 호출, 응답 후처리를 하나의 AI 서비스 파이프라인으로 연결하는 구조이다.
