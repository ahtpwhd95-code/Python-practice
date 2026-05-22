# Day39 복습 문제 - Style Transfer와 GAN

## 1. Style Transfer 개념

아래 용어를 한 문장으로 설명하세요.

- Style Transfer
- Feature Map
- Gram Matrix
- Style Loss
- Content Loss

---

## 2. VGG-19의 역할

Style Transfer에서 VGG-19를 사용하는 이유를 정리하세요.

```text
VGG-19를 사용하는 이유:

```

---

## 3. Style Loss와 Content Loss

아래 표를 채우세요.

| 구분 | 기준으로 사용하는 값 | 목적 |
|---|---|---|
| Style Loss |  |  |
| Content Loss |  |  |

---

## 4. Total Loss

다음 식을 완성하세요.

```text
total_loss = (        ) * style_loss + (        ) * content_loss
```

---

## 5. GAN 기본 구조

Generator와 Discriminator의 역할을 정리하세요.

```text
Generator:
-

Discriminator:
-
```

---

## 6. GAN Loss

다음 질문에 답하세요.

```text
generator_loss에서 fake_output의 target을 1로 두는 이유는?

discriminator_loss에서 real_output과 fake_output의 target은 각각 무엇인가?
```

---

## 7. 모델 계층 복습

아래 계층의 역할을 간단히 적으세요.

- Conv2DTranspose:
- BatchNormalization:
- LeakyReLU:

---

## 8. 학습 흐름

`train_step` 안에서 일어나는 일을 순서대로 정리하세요.

```text
1.
2.
3.
4.
```
