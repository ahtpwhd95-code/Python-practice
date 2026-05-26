# Day41 복습 문제 - RAG와 LangChain

## 1. RAG 개념

RAG가 무엇인지 한 문장으로 설명하세요.

```text

```

---

## 2. RAG가 필요한 이유

RAG가 없을 때 LLM이 가질 수 있는 한계를 적으세요.

```text
1.
2.
3.
```

---

## 3. RAG 전체 흐름

아래 흐름을 완성하세요.

```text
문서 로드
-> (        )
-> (        )
-> 벡터DB 저장
-> (        )
-> LLM 답변 생성
-> (        )
```

---

## 4. LangChain 기본 구조

다음 파이프라인에서 각 요소의 역할을 설명하세요.

```python
chain = prompt | llm | output_parser
```

- prompt:
- llm:
- output_parser:

---

## 5. LangChain 구성 요소

아래 용어를 한 문장으로 설명하세요.

- Agent:
- Tool:
- Memory:
- Callback:

---

## 6. 외부 API와 로컬 LLM 비교

아래 표를 채우세요.

| 구분 | 장점 | 단점 |
|---|---|---|
| 외부 API |  |  |
| 로컬 LLM |  |  |

---

## 7. 실습 오류 정리

오늘 실습에서 발생한 문제와 해결 방법을 정리하세요.

```text
문제:

해결:
```

---

## 8. 프로젝트 연결

SchoolBridge 번역 파이프라인을 LangChain 관점에서 다시 표현하세요.

```text
입력 ->
전처리 ->
모델 처리 ->
후처리 ->
검증 ->
최종 출력 ->
```
