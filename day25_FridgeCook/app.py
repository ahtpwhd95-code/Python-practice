from flask import Flask, render_template, request
import sqlite3
import numpy as np
import os
import re

app = Flask(__name__)
DB_FILENAME = 'refrigerator_pro.db'

class RecipeRecommender:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row 
        self.cur = self.conn.cursor()
        self.recipes = []
        self.vocab = []
        self.categorized_vocab = {}
        self._load_data()

    def _load_data(self):
        try:
            self.cur.execute("SELECT * FROM recipes")
            rows = self.cur.fetchall()
            all_words = set()
            for row in rows:
                # 데이터 정제
                ing_str = row['ingredients']
                clean_ing = ing_str.replace('\n', ', ').replace('재료', '').replace('양념', '')
                clean_ing = re.sub(r'\([^)]*\)', '', clean_ing)
                clean_ing = re.sub(r'[0-9.]+[g|ml|kg|L|컵|스푼|개|쪽|줌|톨]*', '', clean_ing)
                clean_list = [i.strip() for i in clean_ing.split(',') if len(i.strip()) > 1]

                # 💡 조리 단계 (1단계부터 20단계까지 싹 훑기)
                steps = []
                for i in range(1, 21):
                    m_key, mi_key = f'M{i}', f'MI{i}'
                    # 컬럼이 존재하고 내용이 있을 때만 추가
                    if m_key in row.keys() and row[m_key] and str(row[m_key]).strip():
                        steps.append({'text': row[m_key], 'img': row[mi_key]})
                
                self.recipes.append({
                    'name': row['menu_name'], 
                    'ingredients': clean_list, 
                    'img_url': row['img_url'],
                    'steps': steps 
                })
                all_words.update(clean_list)
            
            self.vocab = sorted(list(all_words))
            self.categorized_vocab = self._get_categorized(self.vocab)
            print(f"✅ 20단계 조리법 포함 {len(self.recipes)}개 로드 완료")
        except Exception as e:
            print(f"❌ 에러: {e}")

    def _get_categorized(self, vocab):
        categories = {
            '🥩 고기/계란': ['소고기', '돼지고기', '닭고기', '계란', '베이컨', '소시지', '오리'],
            '🐟 수산물': ['새우', '오징어', '고등어', '멸치', '조개', '굴', '게살', '어묵'],
            '🥦 채소/버섯': ['양파', '대파', '마늘', '버섯', '호박', '당근', '감자', '고추', '깻잎'],
            '🧀 유제품/가공품': ['치즈', '우유', '버터', '두부', '햄', '면', '빵', '만두', '떡'],
            '🧂 양념/소스': ['간장', '고추장', '된장', '소금', '설탕', '식초', '카레', '후추'],
            '🍎 과일/기타': ['사과', '배', '토마토', '딸기', '호두', '밤', '잣']
        }
        res = {cat: [] for cat in categories.keys()}
        res['ETC 기타'] = []
        for word in vocab:
            found = False
            for cat, keywords in categories.items():
                if any(k in word for k in keywords):
                    res[cat].append(word)
                    found = True
                    break
            if not found: res['ETC 기타'].append(word)
        return res

    def recommend(self, my_fridge):
        results = []
        for r in self.recipes:
            matched = [ri for ri in r['ingredients'] if any(mi in ri for mi in my_fridge)]
            if matched:
                score = len(matched) / len(r['ingredients'])
                results.append({
                    'name': r['name'], 'score': round(score, 2), 'matches': list(set(matched)),
                    'img_url': r['img_url'], 'steps': r['steps'], 'all_ingredients': ", ".join(r['ingredients'])
                })
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:12]

recommender = RecipeRecommender(DB_FILENAME)

@app.route('/', methods=['GET', 'POST'])
def index():
    results, my_ingreds = None, ""
    if request.method == 'POST':
        combined = [i.strip() for i in request.form.get('ingredients', '').replace(',', ' ').split() if i.strip()]
        combined.extend(request.form.getlist('selected_ingredients'))
        combined = list(set(combined))
        results = recommender.recommend(combined)
        my_ingreds = ", ".join(combined)
    return render_template('index.html', results=results, my_ingreds=my_ingreds, categorized_vocab=recommender.categorized_vocab)

if __name__ == '__main__':
    app.run(debug=True)