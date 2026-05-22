# 2026-05-21 TIL - Style Transfer와 GAN 실습

## 오늘 학습한 내용

### 1. Style Transfer 실습

- 이미지 변환에 사용되는 Style Transfer 개념을 실습했다.
- VGG-19 모델을 기반으로 style loss를 계산할 layer와 content loss를 계산할 layer를 선택했다.
- Style 이미지의 특징은 Gram matrix로 표현하고, Content 이미지는 feature map을 통해 특징을 추출한다는 것을 배웠다.
- `StyleTransferModel` 클래스의 `call` 메서드에서 style feature map과 content feature map을 추출하는 과정을 구현했다.

---

### 2. Style Loss / Content Loss 계산

- Style Transfer에서는 새로 생성되는 이미지가 스타일 이미지의 질감과 컨텐츠 이미지의 구조를 동시에 따라가도록 loss를 계산한다.
- `compute_style_loss`, `compute_content_loss`, `compute_total_loss` 함수를 구현했다.
- 전체 loss는 style loss와 content loss에 각각 가중치를 곱한 뒤 더해서 계산한다.
- Style loss는 Gram matrix를 기준으로 계산하고, content loss는 feature map 차이를 기준으로 계산한다.

```text
total_loss = style_weight * style_loss + content_weight * content_loss
```

---

### 3. GAN 모델 구조 실습

- GAN은 생성자(Generator)와 판별자(Discriminator)가 서로 경쟁하면서 학습하는 구조이다.
- 생성자는 랜덤 노이즈 벡터를 입력받아 실제 이미지와 비슷한 이미지를 생성한다.
- 판별자는 입력 이미지가 실제 이미지인지, 생성자가 만든 가짜 이미지인지 구분한다.
- 생성자에서는 이미지 크기를 키우기 위해 `Conv2DTranspose`를 사용했다.
- 판별자에서는 일반적인 CNN 구조를 사용해 입력 이미지의 진짜/가짜 여부를 판단했다.

---

### 4. Fashion MNIST 기반 GAN 학습

- Fashion MNIST 데이터셋을 사용해 GAN 학습 과정을 실습했다.
- 생성자 손실 함수에서는 가짜 이미지를 판별자가 진짜로 판단하도록 학습시키기 위해 `tf.ones_like(fake_output)`을 사용했다.
- 판별자 손실 함수에서는 실제 이미지는 1, 가짜 이미지는 0으로 판단하도록 `tf.ones_like`, `tf.zeros_like`를 사용했다.
- `train_step` 안에서 생성자와 판별자가 각각 loss를 계산하고 경사 하강법으로 업데이트되는 흐름을 확인했다.

---

## 핵심 개념 정리

| 개념 | 역할 |
|---|---|
| VGG-19 | 이미지 feature를 추출하는 사전학습 모델 |
| Feature Map | 이미지의 구조나 특징을 담은 중간 출력 |
| Gram Matrix | feature 간 상관관계를 계산해 스타일 정보를 표현 |
| Style Loss | 생성 이미지가 스타일 이미지의 질감을 따라가도록 계산하는 loss |
| Content Loss | 생성 이미지가 컨텐츠 이미지의 구조를 유지하도록 계산하는 loss |
| Generator | 노이즈를 입력받아 가짜 이미지를 생성하는 모델 |
| Discriminator | 입력 이미지가 진짜인지 가짜인지 판별하는 모델 |
| Conv2DTranspose | 이미지 크기를 키우는 업샘플링 계층 |

---

## 실습 내용

### Style Transfer

- VGG-19에서 style layer와 content layer를 선택했다.
- Style 이미지와 Content 이미지를 모델에 넣어 각각의 feature를 추출했다.
- Style feature는 Gram matrix로 변환해 style loss 계산에 사용했다.
- Content feature는 feature map 차이를 통해 content loss 계산에 사용했다.
- 최종 loss를 기준으로 생성 이미지를 업데이트하는 흐름을 확인했다.

### GAN

- Fashion MNIST 데이터셋을 불러와 GAN 학습에 사용했다.
- Generator 모델에서 노이즈를 이미지 형태로 변환하는 구조를 확인했다.
- Discriminator 모델에서 이미지가 진짜인지 가짜인지 구분하는 구조를 확인했다.
- `generator_loss`, `discriminator_loss`, `train_step`의 역할을 구분했다.

---

## 오늘의 회고

### 배운 점

- 이미지 생성 모델은 단순히 이미지를 출력하는 것이 아니라 feature map, Gram matrix, loss 계산 같은 수학적 구조를 기반으로 동작한다.
- Style Transfer에서는 이미지의 내용과 스타일을 분리해서 다룬다는 점이 인상 깊었다.
- GAN에서는 생성자와 판별자가 서로 반대 목표를 가지고 학습하면서 결과가 점점 개선되는 구조를 이해했다.
- `Conv2DTranspose`가 이미지 크기를 키우는 데 사용된다는 점을 새롭게 정리할 수 있었다.

### 어려운 점 / 개선할 점

- Gram matrix와 feature map의 차이가 처음에는 헷갈렸다.
- Style loss와 content loss가 모두 feature 기반으로 계산되지만, style loss는 Gram matrix를 사용한다는 점을 확실히 구분해야 한다.
- GAN의 생성자 loss와 판별자 loss는 목표가 다르기 때문에 target 값을 1로 둘지 0으로 둘지 다시 복습해야 한다.
- 모델 구조 자체보다 loss 함수가 왜 그렇게 설계되는지 이해하는 것이 더 중요하다고 느꼈다.

---

## 다음에 복습할 것

- Style Transfer에서 VGG-19가 어떤 역할을 하는지 다시 정리하기
- Gram matrix가 왜 스타일 정보를 표현하는 데 사용되는지 복습하기
- GAN의 생성자와 판별자 학습 흐름을 그림으로 정리하기
- `generator_loss`, `discriminator_loss`, `train_step` 흐름 다시 읽기
- `Conv2DTranspose`, `BatchNormalization`, `LeakyReLU` 역할 복습하기

---

## 참고자료

- 실습 자료: 이미지 변환에 특화된 GAN 모델
- VGG-19
- Style Transfer
- Gram Matrix
- GAN
- Fashion MNIST
- TensorFlow / Keras

---

## 한 줄 정리

Style Transfer는 feature map과 Gram matrix를 활용해 내용과 스타일을 분리해 다루고, GAN은 생성자와 판별자가 경쟁하며 이미지 생성 능력을 학습하는 구조이다.
