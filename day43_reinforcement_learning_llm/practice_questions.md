# Day43 복습 문제 - 강화학습과 LLM 학습

## 1. 강화학습 구성요소

아래 용어를 한 문장으로 설명하세요.

- Agent:
- Environment:
- State:
- Action:
- Reward:

---

## 2. MDP

MDP의 구성요소를 채우세요.

| 기호 | 의미 |
|---|---|
| `S` |  |
| `A` |  |
| `P` |  |
| `R` |  |
| `γ` |  |

---

## 3. Q-Learning 흐름

Q-Learning의 기본 흐름을 순서대로 적으세요.

```text
1.
2.
3.
4.
5.
```

---

## 4. `argmax`와 `max`

아래 코드가 각각 무엇을 의미하는지 설명하세요.

```python
np.argmax(Q[state, :])
np.max(Q[next_state, :])
```

---

## 5. Epsilon-Greedy

Epsilon-Greedy가 필요한 이유를 설명하세요.

```text

```

---

## 6. 종료 조건

Gymnasium에서 `done`과 `truncated`의 차이를 설명하세요.

- `done`:
- `truncated`:

---

## 7. 환경과 알고리즘 궁합

아래 환경에 적합한 알고리즘 방향을 적으세요.

| 환경 | 특징 | 적합한 방향 |
|---|---|---|
| Taxi-v3 |  |  |
| FrozenLake |  |  |
| CartPole |  |  |
| Pendulum |  |  |

---

## 8. LLM 학습 흐름

LLM 학습 흐름을 완성하세요.

```text
사전학습 -> (        ) -> (        )
```

---

## 9. SFT와 Preference 데이터

아래 표를 채우세요.

| 구분 | 데이터 구조 | 학습 목적 |
|---|---|---|
| SFT |  |  |
| Preference |  |  |

---

## 10. LoRA SFT

LoRA가 전체 모델을 모두 학습하지 않고 작은 어댑터만 학습하는 이유를 설명하세요.

```text

```

---

## 11. DPO 실습 에러

DPO 실습에서 발생할 수 있는 환경 문제를 적으세요.

```text
1.
2.
3.
```

---

## 12. Reward 설계

RC카 예시를 바탕으로, 최단거리만 reward로 사용하는 것이 왜 부족할 수 있는지 설명하세요.

```text

```
