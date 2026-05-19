# 2026-05-19 TIL - SQL 마무리, JSON 파싱, 생성형 AI 윤리

## 오늘 학습한 내용

### 1. 관계형 데이터베이스 마무리 및 SQL 실습

- `JOIN`을 사용해 여러 테이블을 연결하고, `WHERE`, `GROUP BY`, `ORDER BY`를 함께 사용하는 문제를 풀었다.
- SQL 문제를 풀 때는 출력해야 하는 컬럼이 어느 테이블에 있는지 먼저 확인해야 한다는 점을 다시 정리했다.
- 집계 함수(`SUM`, `AVG`, `MAX`, `MIN`)와 계산 컬럼을 활용해 카드사별 수수료를 계산했다.
- 카드사 수수료 계산 문제에서는 계산식뿐 아니라 `ROUND()`를 사용한 반올림 조건까지 확인해야 했다.
- `mysqldump`로 MySQL 데이터베이스를 백업하고, `mysql` 명령어로 복원하는 실습을 진행했다.
- 백업과 복원에서 `>`는 내보내기, `<`는 가져오기 방향이라는 점을 정리했다.

```bash
mysqldump -u 사용자명 -p 데이터베이스명 > backup.sql
mysql -u 사용자명 -p 데이터베이스명 < backup.sql
```

---

### 2. 데이터 포맷과 JSON 파싱

- 데이터를 저장하거나 교환하기 위한 대표적인 포맷으로 XML과 JSON을 학습했다.
- JSON은 키-값 구조의 텍스트 기반 데이터 표현 방식이다.
- JSON은 통신 방법이나 프로그래밍 문법 자체가 아니라, 데이터를 표현하는 형식이라는 점이 중요했다.
- Python의 `json` 라이브러리를 사용하면 JSON 문자열이나 파일을 Python 객체로 변환할 수 있다.
- `json.load()`는 JSON 파일을 읽어 Python 객체로 변환하고, `json.dump()`는 Python 객체를 JSON 파일로 저장한다.
- DataFrame은 `to_json()`을 사용해 다양한 `orient` 옵션으로 JSON 형태로 저장할 수 있다.

```python
import json

with open("day37_sql_json_ai/target.json", "r") as f:
    data = json.load(f)

print(data["employee"]["skills"])
```

```python
import json

data = {"name": "elice", "age": 25}

with open("day37_sql_json_ai/dump_test.json", "w") as f:
    json.dump(data, f)
```

---

### 3. 생성형 AI와 윤리

- 생성형 AI는 텍스트, 이미지, 영상 등 새로운 콘텐츠를 생성하는 인공지능이다.
- 생성형 AI를 사용할 때는 할루시네이션, 개인정보, 저작권, 편향성 문제를 함께 고려해야 한다.
- AI가 만든 결과를 그대로 믿기보다 검증하고, 민감한 정보가 포함되지 않도록 주의해야 한다.

---

## 실습 내용

### JSON 파일 읽기

- `test.txt` 파일을 `open()`과 `with open()` 방식으로 읽어보았다.
- `target.json` 파일을 `json.load()`로 읽고 Python 딕셔너리처럼 접근했다.
- `pprint`를 사용해 중첩된 JSON 구조를 보기 좋게 출력했다.

### JSON 파일 저장하기

- Python 딕셔너리를 만든 뒤 `json.dump()`를 사용해 `dump_test.json` 파일로 저장했다.
- Python 객체가 JSON 파일로 변환되는 흐름을 확인했다.

---

## Trouble Shooting

- `JOIN` 문제에서 처음에는 연결 조건을 작성하는 문법이 헷갈렸다.
  - `ON 테이블1.컬럼 = 테이블2.컬럼` 구조로 연결 조건을 명확히 작성해야 한다.
- 카드사 수수료 계산 문제에서 계산식은 맞게 작성했지만, 문제 조건에 있던 반올림 처리를 처음에는 놓쳤다.
  - 출력 컬럼, 정렬 조건, 반올림 여부 같은 세부 조건을 먼저 확인해야 한다.
- DB 복원 과정에서 `>`와 `<` 방향이 헷갈렸다.
  - `>`는 현재 DB 내용을 파일로 내보내기, `<`는 파일 내용을 DB로 가져오기라고 기억한다.

---

## 오늘의 회고

### 배운 점

- SQL은 문법을 외우는 것만큼 테이블 구조를 보고 필요한 컬럼의 위치를 파악하는 과정이 중요하다.
- `JOIN`, `GROUP BY`, 집계 함수를 함께 사용하면 여러 테이블의 데이터를 그룹 단위로 계산할 수 있다.
- `mysqldump`와 `mysql` 명령어의 차이를 통해 DB 백업과 복원 흐름을 이해했다.
- JSON은 API와 데이터 저장에서 자주 사용되는 데이터 표현 형식이라는 점을 정리했다.
- 생성형 AI는 편리하지만, 결과 검증과 윤리적인 사용이 함께 필요하다는 점이 인상 깊었다.

### 어려운 점 / 개선할 점

- SQL 문제를 풀 때 조건을 끝까지 꼼꼼히 읽는 습관이 필요하다.
- `ROUND`, `FLOOR`, `TRUNCATE`처럼 비슷해 보이는 숫자 처리 함수의 차이를 정리해야 한다.
- JSON의 `load`, `loads`, `dump`, `dumps` 차이를 예제로 다시 확인해야 한다.

---

## 다음에 복습할 것

- `JOIN`, `GROUP BY`, 집계 함수 문제 다시 풀어보기
- `ROUND`, `FLOOR`, `TRUNCATE` 차이 정리하기
- `mysqldump` 백업과 `mysql < 파일.sql` 복원 명령어 복습하기
- JSON의 `load`, `loads`, `dump`, `dumps` 차이 정리하기
- DataFrame `to_json()`의 `orient` 옵션 예제로 확인하기
- 생성형 AI 개념과 AI 윤리 내용 복습하기

---

## 참고자료

- MySQL 공식 문서
- Python `json` 라이브러리
- Pandas DataFrame `to_json` 문서
- 수업 실습 자료
- SQL 실습 데이터베이스 예제

---

## 한 줄 정리

SQL은 테이블 구조를 읽고 조건에 맞게 데이터를 연결하는 연습이 중요하고, JSON은 데이터를 주고받기 위한 기본 표현 형식으로 API와 AI 실습의 기반이 된다.
