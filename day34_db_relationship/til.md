# 2026-05-14 TIL - Database Relationship & NoSQL Practice

## Today I Worked On
- 관계형 데이터베이스 개요 학습
- RDB와 NoSQL 차이 이해
- MySQL 테이블 생성, 수정, 삭제 실습
- `PRIMARY KEY`, `FOREIGN KEY`, `CONSTRAINT` 개념 정리
- 복합 기본키 실습
- `customer`, `kickboard`, `borrow` 관계 테이블 설계
- MongoDB와 Cassandra 개념 비교
- 프로젝트 관점에서 RDB/NoSQL 활용 기준 정리

---

## 1. Database Basic Concept

오늘은 데이터베이스의 기본 개념부터 다시 정리했다.

데이터는 현실 세계에서 수집된 단순한 사실과 값이고, 정보는 데이터를 특정 목적에 맞게 해석하거나 가공한 결과이다.

예를 들어 다음은 데이터이다.

```text
kmax6
김민준
서울시 관악구 신림동
2020-05-14 12:01:55
4700
```

하지만 이것을 다음처럼 해석하면 정보가 된다.

```text
김민준 회원은 2020년 5월 14일에 서울시 관악구 신림동에서 킥보드를 대여했고,
354m를 이동하여 4,700원을 결제했다.
```

### What I Learned
데이터베이스는 단순히 값을 저장하는 곳이 아니라, 데이터를 목적에 맞게 관리하고 활용하기 위한 구조이다.

---

## 2. File System Limitation

파일 처리 시스템의 한계도 학습했다.

### Problems
- 데이터 구조가 바뀌면 응용 프로그램 구조도 함께 바뀌어야 한다.
- 프로그램마다 데이터를 따로 저장하면 중복이 발생할 수 있다.
- 잘못된 값이나 중복된 값을 막기 어려워 데이터 무결성을 지키기 어렵다.

### What I Learned
파일로 데이터를 관리하면 처음에는 단순해 보이지만, 데이터가 많아지고 여러 사용자가 함께 사용하기 시작하면 문제가 커진다.

데이터베이스는 이런 문제를 줄이기 위해 나온 구조라고 이해했다.

---

## 3. RDB and NoSQL

오늘은 RDB와 NoSQL의 차이도 학습했다.

### RDB

RDB는 관계형 데이터베이스이다.  
데이터를 행과 열을 가진 테이블 형태로 저장하고, 테이블 간 관계를 이용해 데이터를 관리한다.

대표적인 RDBMS는 다음과 같다.

```text
MySQL
PostgreSQL
MariaDB
Oracle
MSSQL
```

RDB는 구조가 명확한 데이터에 적합하다.

예를 들면 다음과 같은 데이터이다.

```text
회원가입
주문
결제
대여 이력
권한 관리
글로사리
```

### NoSQL

NoSQL은 Not Only SQL의 의미로, 전통적인 관계형 방식만이 아닌 다양한 데이터 저장 방식을 포함한다.

대표적인 NoSQL은 다음과 같다.

```text
MongoDB
Redis
Apache Cassandra
```

NoSQL은 구조가 자주 바뀌거나, JSON 형태의 유동적인 데이터를 저장할 때 편하다.

예를 들면 다음과 같은 데이터이다.

```text
AI 추론 결과
로그 데이터
원본 API 응답
프롬프트/응답 기록
실험 결과
디버깅 trace
```

### My Understanding

오늘 나는 RDB와 NoSQL을 다음처럼 이해했다.

```text
RDB = 정해진 장부
NoSQL = 유연한 기록지
```

---

## 4. My Project Perspective

오늘 배운 RDB와 NoSQL 개념을 내가 진행 중인 프로젝트에도 연결해봤다.

### SchoolBridge

SchoolBridge에서는 다음 데이터가 RDB에 어울린다고 생각했다.

```text
사용자
학생/학부모 관계
공지
할 일 카드
체크리스트
캘린더 일정
글로사리
검수 상태
```

반대로 다음 데이터는 NoSQL에 어울릴 수 있다.

```text
OCR 원본 결과
모델 raw output
번역 실험 로그
미등록 용어 탐지 로그
LLM 분석 결과
디버깅용 pipeline trace
```

특히 글로사리는 정해진 구조와 검수가 중요하기 때문에 RDB가 잘 맞는다고 느꼈다.

---

### Stock Sentiment Project

스톡 프로젝트에서는 다음 데이터가 RDB에 어울릴 수 있다.

```text
종목 기본 정보
관심 종목
사용자 설정
일자별 최종 점수
백테스트 결과 요약
```

반대로 다음 데이터는 MongoDB 같은 NoSQL이 더 편할 수 있다.

```text
뉴스 원문 묶음
LLM 분석 JSON
수집 로그
원본 API 응답
프롬프트/응답 히스토리
```

AI 분석 결과는 매번 필드 구조가 달라질 수 있기 때문에 MongoDB가 더 잘 맞을 수 있다고 바로 떠올릴 수 있었다.

### What I Learned
DB를 배운 뒤에는 프로젝트를 볼 때 “어떤 데이터는 RDB에 넣고, 어떤 데이터는 NoSQL에 넣어야 할지”를 생각하게 되었다.

이것이 단순 코딩보다 설계 감각에 가까운 부분이라고 느꼈다.

---

## 5. Table, Attribute, Tuple, Domain

관계형 데이터베이스의 구성요소도 정리했다.

| 용어 | 의미 | 내가 이해한 방식 |
| --- | --- | --- |
| 테이블 | 행과 열로 구성된 데이터 구조 | 하나의 장부 |
| 속성 | 데이터의 특성을 나타내는 열 | 장부의 항목 |
| 튜플 | 속성들이 모여 구성된 행 | 장부의 한 줄 |
| 도메인 | 속성이 가질 수 있는 값의 집합 | 해당 칸에 들어갈 수 있는 값의 범위 |

예를 들어 `customer` 테이블은 고객 장부이고, `id`, `name`, `address`는 장부의 항목이다.

```sql
CREATE TABLE customer (
    id VARCHAR(10),
    name VARCHAR(10),
    address VARCHAR(30)
);
```

---

## 6. SQL Classification

SQL은 관계형 데이터베이스를 다루기 위한 표준 언어이다.

오늘은 SQL을 크게 다음처럼 나누어 이해했다.

| 분류 | 의미 | 예시 |
| --- | --- | --- |
| DDL | 데이터 구조 정의 | CREATE, ALTER, DROP |
| DML | 데이터 조작 | INSERT, SELECT, UPDATE, DELETE |
| DCL | 권한 제어 | GRANT, REVOKE |

오늘 실습에서는 주로 DDL과 DML을 사용했다.

---

## 7. Kickboard Table Practice

공유 킥보드 서비스를 위한 `kickboard` 테이블을 생성했다.

### Table Structure

```sql
CREATE TABLE kickboard (
    member_id VARCHAR(16),
    member_name VARCHAR(16),
    kickboard_id VARCHAR(16),
    kickboard_brand VARCHAR(16),
    rental_location VARCHAR(32),
    rental_date DATETIME,
    distance INT,
    price INT
);
```

### What I Did
- 테이블 생성
- `SHOW TABLES;`로 테이블 목록 확인
- `DESC kickboard;`로 구조 확인

### What I Learned
테이블을 만들 때는 컬럼 순서, 데이터 타입, 제약조건을 정확히 작성해야 한다.

실습 환경에서는 컬럼 순서도 정답 처리에 영향을 주기 때문에, 문제에서 요구한 순서를 그대로 맞추는 것이 중요했다.

---

## 8. Insert Practice

공유 킥보드 이용 기록 데이터를 삽입했다.

### Example

```sql
INSERT INTO kickboard (
    member_id,
    member_name,
    kickboard_id,
    kickboard_brand,
    rental_location,
    rental_date,
    distance,
    price
)
VALUES (
    'kmax6',
    '김민준',
    '7YWC',
    'boardkick',
    '서울시 관악구 신림동',
    '2020-05-14 12:01:55',
    354,
    4700
);
```

### What I Learned
날짜와 시간 데이터도 작은따옴표로 감싸서 입력해야 한다.

```sql
'2020-05-14 12:01:55'
```

처음에는 날짜니까 따옴표가 필요 없을 것 같았지만, SQL에서는 날짜/시간 값을 문자열 형태로 입력한다고 이해했다.

```text
문자열      → '김민준'
날짜/시간   → '2020-05-14 12:01:55'
숫자        → 354
```

---

## 9. ALTER TABLE Practice

테이블 구조를 수정하기 위해 `ALTER TABLE`을 실습했다.

### Add Column

```sql
ALTER TABLE kickboards ADD member_birthday DATE;
```

### Modify Column Type

```sql
ALTER TABLE kickboards MODIFY rental_date TIME;
```

### Change NOT NULL

```sql
ALTER TABLE kickboards MODIFY member_id VARCHAR(16) NOT NULL;
```

### Change Column Name

```sql
ALTER TABLE kickboards CHANGE kickboard_id id VARCHAR(16);
ALTER TABLE kickboards CHANGE kickboard_brand brand VARCHAR(16);
```

### Drop Column

```sql
ALTER TABLE kickboards DROP distance;
```

### Rename Table

```sql
ALTER TABLE kickboards RENAME kickboard;
```

### What I Learned
`ALTER TABLE`은 이미 존재하는 테이블 구조를 바꿀 때 사용한다.

컬럼 추가, 타입 수정, 이름 변경, 삭제, 테이블 이름 변경까지 모두 가능하다.

---

## 10. Key Concept

오늘은 KEY 개념을 집중적으로 학습했다.

KEY는 조건에 만족하는 튜플을 찾거나, 정렬하거나, 각 행을 식별할 때 기준이 되는 속성이다.

| 키 종류 | 의미 |
| --- | --- |
| 기본키 | 서로 다른 튜플을 유일하게 식별하는 키 |
| 외래키 | 다른 테이블의 기본키를 참조하는 키 |
| 후보키 | 기본키가 될 수 있는 키 |
| 대체키 | 후보키 중 기본키가 아닌 키 |
| 슈퍼키 | 유일성은 만족하지만 최소성은 만족하지 않을 수 있는 키 |

### My Understanding

```text
기본키 = 이 장부에서 한 줄을 구분하는 값
외래키 = 다른 장부와 매핑되는 연결고리
```

처음에는 용어가 어렵게 느껴졌지만, 장부와 연결고리로 생각하니 훨씬 이해가 쉬웠다.

---

## 11. Primary Key

기본키는 테이블에서 각 행을 유일하게 구분하는 기준이다.

```sql
CREATE TABLE customer (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(10),
    address VARCHAR(30)
);
```

여기서 `id`는 고객 한 명을 구분하는 값이다.

### Primary Key Rules

```text
중복될 수 없다.
NULL이 될 수 없다.
각 행을 식별할 수 있어야 한다.
```

### What I Learned
기본키는 테이블의 각 행을 구분하는 식별자이다.

물류로 비유하면 송장번호나 관리번호처럼, 하나의 대상을 구분하는 기준이라고 느꼈다.

---

## 12. Foreign Key

외래키는 다른 테이블의 기본키를 참조하는 속성이다.

```sql
FOREIGN KEY (customer_id) REFERENCES customer(id)
```

처음에는 “참조한다”라는 표현이 어렵게 느껴졌다.  
하지만 “매핑한다”라고 생각하니 이해가 쉬웠다.

```text
order_history.customer_id 값이 customer.id 값 중 하나와 매핑된다.
```

예시:

```text
customer

id     name
c001   김민준
c002   이서연
```

```text
order_history

customer_id   order_id
c001          o001
c001          o002
c002          o003
```

여기서 `order_history.customer_id = c001`은 `customer.id = c001`인 고객과 연결된다.

### What I Learned

```text
외래키 = 다른 테이블과 연결되는 매핑값
```

외래키는 없는 값을 마음대로 넣지 못하게 막아준다.  
예를 들어 `customer` 테이블에 없는 `c999`를 `order_history.customer_id`에 넣으려고 하면 에러가 발생한다.

---

## 13. Constraint

제약조건은 데이터가 잘못 들어오지 못하게 막는 규칙이다.

SQL에서는 `CONSTRAINT` 키워드를 이용해 제약조건에 이름을 붙일 수 있다.

| 제약조건 | 의미 |
| --- | --- |
| PRIMARY KEY | 기본키 |
| FOREIGN KEY | 외래키 |
| UNIQUE | 중복 금지 |
| NOT NULL | NULL 금지 |
| CHECK | 조건 검사 |
| DEFAULT | 기본값 |

### Example

```sql
CREATE TABLE customer (
    id VARCHAR(10),
    name VARCHAR(10) NOT NULL,
    age INT,
    CONSTRAINT id_unique UNIQUE (id),
    CONSTRAINT age_check CHECK (age >= 0)
);
```

### My Understanding

```text
CONSTRAINT = 불량 데이터가 들어오지 못하게 막는 검수 규칙
```

이렇게 이해하니 물류에서 검수 기준을 두는 것과 비슷하게 느껴졌다.

---

## 14. Check Constraints

제약조건을 확인하기 위해 `information_schema.table_constraints`를 조회했다.

처음에는 다음 명령어를 실행했다.

```sql
SELECT * FROM information_schema.table_constraints;
```

그랬더니 내가 만든 DB뿐 아니라 MySQL 시스템 DB의 제약조건까지 모두 출력되었다.

### Fixed Query

```sql
SELECT
    table_name,
    constraint_name,
    constraint_type
FROM information_schema.table_constraints
WHERE table_schema = 'est';
```

### What I Learned
`information_schema`는 DB의 메타 정보를 담고 있는 시스템 영역이다.

내가 만든 DB의 제약조건만 확인하려면 `WHERE table_schema = 'est'`처럼 조건을 붙여야 한다.

---

## 15. Composite Primary Key

복합 기본키는 하나의 컬럼이 아니라 여러 컬럼의 조합으로 한 행을 구분하는 기본키이다.

```sql
CONSTRAINT order_history_pk PRIMARY KEY (customer_id, order_id)
```

이 경우 `customer_id` 하나만 기본키도 아니고, `order_id` 하나만 기본키도 아니다.

```text
customer_id + order_id
```

이 조합이 하나의 기본키가 된다.

### Valid

```text
customer_id | order_id
c001        | o001
c001        | o002
c002        | o001
```

### Invalid

```text
customer_id | order_id
c001        | o001
c001        | o001
```

두 컬럼의 조합이 완전히 같으면 중복이므로 불가능하다.

### What I Learned
`DESC`로 보면 복합키에 포함된 컬럼이 모두 `PRI`로 표시된다.

처음에는 각각이 단독 기본키처럼 느껴졌지만, 실제로는 두 컬럼이 기본키 세트에 포함되어 있다는 뜻이다.

---

## 16. Customer and Kickboard Tables

공유 킥보드 서비스의 데이터를 분리하기 위해 `customer`와 `kickboard` 테이블을 만들었다.

### Customer Table
고객 정보를 저장하는 테이블이다.

```text
customer_number
name
phone_number
```

### Kickboard Table
킥보드 정보를 저장하는 테이블이다.

```text
id
brand
status
```

### What I Learned
처음에는 모든 데이터를 하나의 `kickboard` 테이블에 넣어도 된다고 생각했지만, 실제 서비스에서는 회원 정보, 킥보드 정보, 대여 이력을 나누어 관리하는 것이 더 적절하다.

이렇게 나누면 데이터 중복을 줄이고, 각 데이터의 역할이 명확해진다.

---

## 17. Borrow Relationship Table

마지막으로 `borrow` 테이블을 만들었다.

`borrow`는 고객과 킥보드 사이의 대여 관계를 나타내는 테이블이다.

```text
고객이 킥보드를 대여한다.
```

이 문장을 데이터베이스 구조로 바꾸면 다음과 같다.

```text
customer
kickboard
borrow
```

### Borrow Table

```sql
CREATE TABLE borrow (
    customer_number VARCHAR(10),
    rental_time DATETIME,
    rental_status ENUM('대여', '반납'),
    rental_location VARCHAR(20),
    kickboard_id VARCHAR(10),

    PRIMARY KEY (customer_number, rental_time),
    FOREIGN KEY (customer_number) REFERENCES customer(customer_number),
    FOREIGN KEY (kickboard_id) REFERENCES kickboard(id)
);
```

### Important Points

```text
customer_number + rental_time = borrow 테이블의 복합 기본키
customer_number = customer 테이블과 연결되는 외래키
kickboard_id = kickboard 테이블과 연결되는 외래키
```

### DESC Result

```text
customer_number | PRI
rental_time     | PRI
kickboard_id    | MUL
```

`customer_number`와 `rental_time`이 모두 `PRI`로 보이는 이유는 두 컬럼이 복합 기본키 세트에 포함되어 있기 때문이다.

`kickboard_id`는 외래키로 사용되기 때문에 `MUL`로 표시될 수 있다.

---

## 18. ERD and GUI Understanding

DBeaver에서 ERD를 확인하면서 테이블 간 관계를 그림으로 볼 수 있었다.

SQL로 만든 관계가 GUI에서는 선으로 연결되어 보였다.

```text
borrow.customer_number → customer.customer_number
borrow.kickboard_id → kickboard.id
```

### What I Learned
GUI 도구는 테이블 관계를 시각적으로 확인할 때 유용하다.

하지만 GUI가 편하다고 해서 SQL 구조를 몰라도 되는 것은 아니다.  
SQL을 직접 쳐보고 관계를 이해한 상태에서 ERD를 보면 훨씬 더 잘 이해된다.

---

## 19. MongoDB and Cassandra

MongoDB와 Cassandra도 간단히 비교했다.

### MongoDB
MongoDB는 JSON과 비슷한 문서 형태로 데이터를 저장한다.

구조가 유동적인 데이터에 적합하다.

```text
AI 추론 결과
뉴스 원문
로그 데이터
실험 결과
```

### Cassandra
Cassandra는 대량의 데이터를 분산 저장하고 빠르게 쓰는 데 강한 NoSQL이다.

대규모 로그나 시간 순서로 계속 쌓이는 데이터에 어울린다.

```text
센서 로그
사용자 행동 로그
시간별 이벤트 기록
AI 추론 로그
주식 뉴스 수집 이력
```

### My Understanding

```text
RDB = 정해진 업무 장부
MongoDB = 유연한 JSON 기록지
Cassandra = 대량으로 쌓이는 시간/로그 데이터 저장소
```

---

## 20. Database as a Pipeline

오늘 가장 크게 이해한 부분은 DB를 단순 저장소가 아니라 데이터가 흘러가는 유통과정으로 볼 수 있다는 점이다.

내가 이해한 방식은 다음과 같다.

```text
DB = 데이터 유통과정
테이블 = 공정별 장부
컬럼 = 장부의 항목
행 = 장부의 한 줄
PK = 한 줄을 구분하는 식별자
FK = 다른 장부와 이어지는 연결고리
CONSTRAINT = 잘못된 데이터가 들어오지 못하게 막는 검수 규칙
```

물류 흐름과 비슷하게 생각하니 이해가 쉬웠다.

```text
입고 → 검수 → 적재 → 피킹 → 포장 → 출고
```

데이터베이스도 다음처럼 흐름을 나누고 연결한다.

```text
고객 → 대여 → 킥보드
```

또는 실제 서비스에서는 다음처럼 확장될 수 있다.

```text
고객 → 주문 → 주문상세 → 결제 → 배송
```

각 단계의 output이 다음 단계의 input이 된다는 점에서 AI 파이프라인과도 비슷하다고 느꼈다.

---

## 21. AI Era Developer Perspective

오늘 DB를 배우면서 코딩 자체보다 설계가 중요하다는 것을 더 크게 느꼈다.

AI가 코드는 잘 만들어줄 수 있지만, 다음과 같은 판단은 사람이 해야 한다.

```text
어떤 데이터를 RDB에 저장할지
어떤 데이터를 NoSQL에 저장할지
무엇을 기본키로 잡을지
어디에 외래키를 걸지
어떤 제약조건으로 잘못된 데이터를 막을지
로그와 원본 결과를 어디에 보관할지
```

요즘 풀스택은 단순히 프론트엔드와 백엔드를 모두 하는 것이 아니라, DB 구조, API, 모델, 로그, 배포, 보안까지 전체 흐름을 이해하는 것에 가깝다고 느꼈다.

특히 AI를 활용하는 개발자는 “이거 만들어줘”라고 요청하는 사람이 아니라, 각 파트의 역할을 나누고 오케스트라처럼 지휘하는 사람에 가까워야 한다고 느꼈다.

---

## Trouble Shooting

### 1) Date Quotation Issue

날짜와 시간 데이터를 입력할 때 따옴표를 빼먹었다.

Wrong:

```sql
2020-05-14 12:01:55
```

Correct:

```sql
'2020-05-14 12:01:55'
```

---

### 2) Constraint Query Explosion

다음 명령어를 실행했더니 너무 많은 결과가 나왔다.

```sql
SELECT * FROM information_schema.table_constraints;
```

이 명령어는 MySQL 서버 전체의 제약조건을 보여주기 때문이다.

해결:

```sql
SELECT
    table_name,
    constraint_name,
    constraint_type
FROM information_schema.table_constraints
WHERE table_schema = 'est';
```

---

### 3) Composite Key Confusion

`DESC borrow;`를 실행했을 때 `customer_number`와 `rental_time`이 모두 `PRI`로 보여서 처음에는 둘 다 각각 기본키인 줄 알았다.

하지만 실제로는 두 컬럼이 함께 하나의 복합 기본키를 구성하는 것이었다.

```text
customer_number + rental_time = 하나의 기본키 세트
```

---

### 4) No Database Selected

MySQL에 접속한 후 바로 `DESC borrow;`를 실행했더니 다음 에러가 발생했다.

```text
ERROR 1046 (3D000): No database selected
```

해결:

```sql
USE est;
DESC borrow;
```

---

### 5) DBeaver Execution Scope

DBeaver에서 `Ctrl + Enter`는 현재 커서가 있는 SQL문만 실행한다.

여러 테이블을 만들 때 앞쪽 SQL이 실행되지 않은 상태에서 뒤쪽 SQL만 실행하면, 외래키가 참조할 테이블이 없어서 에러가 발생할 수 있다.

---

## Review

오늘은 데이터베이스의 기본 개념에서 시작해서 RDB, NoSQL, 키, 제약조건, 복합키, 관계 테이블까지 실습했다.

처음에는 용어가 많아서 어렵게 느껴졌지만, DB를 데이터 유통과정으로 생각하니 이해가 쉬워졌다.

특히 다음 표현들이 기억에 남는다.

```text
기본키 = 장부의 한 줄을 구분하는 값
외래키 = 다른 장부와 매핑되는 연결고리
제약조건 = 불량 데이터 방지 검수 규칙
복합키 = 여러 값을 묶은 세트 식별자
RDB = 정해진 장부
NoSQL = 유연한 기록지
```

오늘은 단순히 SQL 문법을 배운 날이 아니라, 현실 세계의 흐름을 데이터 구조로 바꾸는 감각을 얻은 날이었다.

팀프로젝트에서 배운 파이프라인 감각이 DB에도 그대로 적용된다는 점이 인상 깊었다.

---

## Next
- JOIN 개념 학습
- 외래키로 연결된 테이블을 함께 조회하는 방법 이해
- RDB와 NoSQL을 프로젝트 데이터에 맞게 구분하는 연습
- Python에서 MySQL CRUD 연결 실습
- SchoolBridge와 Stock 프로젝트의 DB 구조를 다시 생각해보기