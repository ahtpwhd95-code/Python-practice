# 
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

# 1. 코사인 유사도 함수 (수학적 정석)
def cal_cosine_sim(v1, v2):
    # 분자: 내적 / 분모: 각 벡터 크기의 곱
    return np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))

# 2. Doc2Vec 모델 로드 및 벡터 추출
# 주의: 실습 환경에 따라 dv 또는 docvecs 사용
model = Doc2Vec.load('my_doc2vec.model')
v1 = model.dv[0]
v2 = model.dv[1]

# 3. 유사도 계산 결과 출력
sim_score = cal_cosine_sim(v1, v2)
print(f"문서 간 유사도: {sim_score:.4f}")