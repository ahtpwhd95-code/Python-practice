from konlpy.tag import Kkma

sent = "안녕 나는 엘리스야 반가워. 너의 이름은 뭐야?"
kkma = Kkma()
print(kkma.nouns(sent)) 
print()
print(kkma.pos(sent))   
 
print()
print(kkma.sentences(sent))

from konlpy.tag import Okt
sent = "안녕 나는 엘리스야 반가워. 너의 이름은 뭐야?"
okt = Okt()
print(okt.nouns(sent)) 
print()
print(okt.pos(sent))
print()
print(okt.pos(sent, stem = True))

'''
from soynlp.utils import DoublespaceLineCorpus
from soynlp.word import WordExtractor
from soynlp.noun import LRNounExtractor_v2
train_data = DoublespaceLineCorpus(학습데이터의 경로)
noun_extractor = LRNounExtractor_v2()
nouns = noun_extractor.train_extract(train_data)
words = word_extractor.train_extract(train_data)
'''