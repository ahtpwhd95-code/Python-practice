from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 전처리
doc = ["i am very happy", "this product is really great"]
emotion = ["happy", "excited"]

cv = CountVectorizer()
csr_doc_matrix = cv.fit_transform(doc)

print(csr_doc_matrix.toarray())
print(cv.get_feature_names_out())

# 학습하기
clf = MultinomialNB()
clf.fit(csr_doc_matrix, emotion)


# 검증하기
test_doc = ["i am really great"]
transformed_test = cv.transform(test_doc)
pred = clf.predict(transformed_test)
print(pred) # array(['excited'], dtype='<U7')
