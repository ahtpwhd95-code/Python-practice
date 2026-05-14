# 2026-05-13 TIL - MySQL & PostgreSQL Basic Practice

## Today I Worked On
- MySQL Community Server 설치 및 기본 접속
- DBeaver 연결 및 SQL Editor 사용
- MySQL 데이터베이스 생성과 선택
- Python과 MySQL 연결 실습
- PostgreSQL 기본 개념 및 드라이버 설치
- 환경 변수 PATH 문제 해결
- DB 연결 에러와 예외 처리 구조 확인

---

## 1. MySQL Installation & Basic Access

오늘은 MySQL Community Server를 설치하고, CMD에서 MySQL에 접속하는 방법을 실습했다.

처음에는 `mysql` 명령어가 CMD에서 인식되지 않았고, 이후 MySQL 실행 파일이 있는 `bin` 폴더를 환경 변수 PATH에 추가해야 한다는 것을 확인했다.

### What I Checked
- MySQL Community Server 설치
- 기본 포트 `3306` 확인
- CMD에서 MySQL 접속
- `mysql -u root -p` 명령어 사용
- MySQL 실행 파일 경로 확인

### Command

```bash
mysql -u root -p
```

### What I Learned
MySQL에 접속할 때는 단순히 `mysql`만 입력하는 것이 아니라, 사용할 계정을 명시하는 것이 중요하다.

```bash
mysql -u root -p
```

여기서 `-u root`는 root 사용자로 접속한다는 뜻이고, `-p`는 비밀번호를 입력받겠다는 의미이다.

---

## 2. MySQL Database Basic Commands

MySQL에 접속한 후 데이터베이스를 만들고 선택하는 기본 명령어를 실습했다.

### Commands

```sql
SHOW DATABASES;
CREATE DATABASE est;
USE est;
SHOW TABLES;
```

### What I Did
- 현재 존재하는 데이터베이스 목록 확인
- `est` 데이터베이스 생성
- `USE est;`로 사용할 데이터베이스 선택
- 현재 DB 안의 테이블 목록 확인

### What I Learned
MySQL에 로그인했다고 해서 자동으로 특정 데이터베이스를 사용하는 것은 아니다.

테이블을 조회하거나 생성하기 전에 반드시 사용할 데이터베이스를 선택해야 한다.

```sql
USE est;
```

이 과정을 빼먹으면 다음과 같은 에러가 발생할 수 있다.

```text
ERROR 1046 (3D000): No database selected
```

---

## 3. DBeaver Setup

DBeaver를 이용해서 MySQL 서버에 연결하고, GUI 환경에서 데이터베이스를 확인했다.

처음에는 화면이 비어 있어서 당황했지만, Database Navigator를 열고 MySQL 연결을 만든 뒤 데이터베이스 목록을 확인할 수 있었다.

### What I Checked
- Database Navigator 표시
- MySQL 연결 생성
- Host, Port, Username, Password 입력
- Test Connection 확인
- `est` 데이터베이스 확인
- SQL Editor 열기

### What I Learned
DBeaver는 SQL을 직접 입력하지 않고도 데이터베이스 구조를 확인할 수 있는 GUI 도구이다.

하지만 DB 구조와 명령어를 이해하지 못한 상태에서 GUI만 사용하면, 실제로 어떤 SQL이 실행되는지 놓칠 수 있다.

그래서 초반에는 SQL을 직접 입력하고, DBeaver는 확인용으로 함께 쓰는 것이 좋다고 느꼈다.

---

## 4. SQL Editor Execution Issue

DBeaver에서 SQL을 여러 줄 작성하고 `Ctrl + Enter`를 눌렀을 때, 전체 코드가 실행되는 것이 아니라 현재 커서가 위치한 SQL문 하나만 실행된다는 것을 알게 되었다.

이 때문에 테이블 생성 SQL을 여러 개 작성해놓고, 뒤쪽 SQL만 실행되어 외래키 참조 테이블이 없다는 에러가 발생하기도 했다.

### What I Learned
DBeaver에서 실행 방식은 중요하다.

```text
Ctrl + Enter = 현재 SQL문 실행
전체 선택 후 실행 = 선택한 SQL문 실행
Script 실행 = 여러 SQL문 전체 실행
```

앞으로 여러 테이블을 순서대로 생성할 때는 실행 범위를 먼저 확인해야 한다.

---

## 5. Python MySQL Connector

Python에서 MySQL에 연결하기 위해 `mysql-connector-python` 패키지를 설치했다.

### Install

```bash
pip install mysql-connector-python
```

### Basic Connection Code

```python
import mysql.connector

db = None

try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="비밀번호",
        database="est"
    )

    if db.is_connected():
        print("MySQL 연결 성공")

except mysql.connector.Error as err:
    print(f"에러 발생: {err}")

finally:
    if db is not None and db.is_connected():
        db.close()
        print("MySQL 연결 종료")
```

### What I Learned
Python에서 DB에 연결할 때는 접속 정보가 정확해야 한다.

필요한 정보는 다음과 같다.

```text
host
port
user
password
database
```

또한 연결이 실패했을 때 `db` 변수가 생성되지 않을 수 있기 때문에, 먼저 `db = None`으로 선언하고 예외 처리를 해야 한다.

---

## 6. MySQL Access Error

Python에서 MySQL에 연결할 때 다음 에러가 발생했다.

```text
1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```

처음에는 비밀번호가 틀린 줄 알았지만, 실제 원인은 코드 수정 후 파일을 저장하지 않아서 이전 코드가 계속 실행되고 있던 문제였다.

### What I Learned
VS Code에서 코드를 수정한 뒤 실행하기 전에는 반드시 저장해야 한다.

```text
Ctrl + S
```

작은 실수지만, 저장하지 않은 상태에서 실행하면 아무리 코드를 고쳐도 결과가 바뀌지 않는다.

---

## 7. NameError Issue

MySQL 연결 실패 후 다음 에러도 함께 발생했다.

```text
NameError: name 'db' is not defined
```

이 에러는 MySQL 연결에 실패해서 `db` 변수가 생성되지 않았는데, 마지막에 `db.is_connected()`를 실행하려고 해서 발생했다.

### Problem Code

```python
finally:
    if db.is_connected():
        db.close()
```

### Fixed Code

```python
db = None

finally:
    if db is not None and db.is_connected():
        db.close()
```

### What I Learned
DB 연결처럼 실패할 수 있는 코드는 항상 예외 상황을 고려해야 한다.

단순히 정상 실행만 생각하고 코드를 작성하면, 원래 에러에 이어서 추가 에러가 발생할 수 있다.

---

## 8. PostgreSQL Basic Setup

MySQL과 함께 PostgreSQL도 간단히 학습했다.

PostgreSQL의 기본 관리자 계정은 `postgres`, 기본 포트는 `5432`이다.

### Install

```bash
pip install psycopg2-binary
```

### PostgreSQL Basic Info

```text
관리자 계정: postgres
기본 포트: 5432
Python 드라이버: psycopg2-binary
```

### What I Learned
MySQL과 PostgreSQL은 모두 RDBMS이지만, 사용하는 명령어와 자동 증가 방식 등에서 차이가 있다.

예를 들어 MySQL에서는 데이터베이스 목록을 볼 때 다음을 사용한다.

```sql
SHOW DATABASES;
```

PostgreSQL에서는 `psql` 환경에서 다음을 사용한다.

```sql
\l
```

---

## 9. MySQL vs PostgreSQL

오늘은 MySQL과 PostgreSQL의 차이도 간단히 정리했다.

| 항목 | MySQL | PostgreSQL |
| --- | --- | --- |
| 기본 관리자 | root | postgres |
| 기본 포트 | 3306 | 5432 |
| Python 드라이버 | mysql-connector-python | psycopg2-binary |
| 자동 증가 | AUTO_INCREMENT | SERIAL |
| DB 목록 확인 | SHOW DATABASES; | \l |
| 테이블 목록 확인 | SHOW TABLES; | \dt |
| 종료 | exit; 또는 quit; | \q |

### What I Learned
DBMS마다 SQL의 큰 흐름은 비슷하지만, 세부 명령어와 문법은 다를 수 있다.

따라서 어떤 DBMS를 사용하는지 먼저 확인하고 명령어를 써야 한다.

---

## 10. Environment Variable Issue

CMD에서 `mysql` 명령어를 실행했을 때 다음 문제가 발생했다.

```text
'mysql'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.
```

원인은 MySQL 실행 파일이 있는 폴더가 Windows PATH 환경 변수에 등록되어 있지 않았기 때문이다.

### mysql.exe Path

```text
C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe
```

### PATH에 추가해야 하는 경로

```text
C:\Program Files\MySQL\MySQL Server 8.0\bin
```

### What I Learned
프로그램이 설치되어 있어도 PATH에 등록되어 있지 않으면 CMD에서 명령어로 실행할 수 없다.

환경 변수를 수정한 뒤에는 기존 CMD나 VS Code 터미널을 닫고 새로 열어야 반영된다.

---

## Trouble Shooting

### 1) MySQL Prompt `->` Issue
MySQL에서 세미콜론을 입력하지 않으면 명령이 끝나지 않은 상태로 인식된다.

```sql
SHOW DATABASES
```

위처럼 세미콜론이 없으면 `->` 상태가 된다.

해결:

```sql
\c
```

또는 명령어를 끝낼 때는 반드시 세미콜론을 붙인다.

```sql
SHOW DATABASES;
```

---

### 2) `creat database` Typo
처음에 다음처럼 입력했다.

```sql
creat database est;
```

정답은 다음이다.

```sql
CREATE DATABASE est;
```

SQL도 오타에 민감하기 때문에 명령어를 정확히 입력해야 한다.

---

### 3) MySQL PATH Issue
`mysql` 명령어가 CMD에서 인식되지 않았다.

해결:
- MySQL `bin` 폴더 위치 확인
- Windows 환경 변수 PATH에 추가
- CMD 또는 VS Code 재시작

---

### 4) Access Denied Issue
Python에서 MySQL 연결 시 1045 에러가 발생했다.

처음에는 비밀번호 문제로 생각했지만, 실제로는 코드 수정 후 저장하지 않은 것이 원인이었다.

해결:
- 코드 저장
- 접속 정보 재확인
- `host`, `user`, `password`, `database` 값 확인

---

### 5) `db is not defined`
DB 연결 실패 후 `db` 변수가 생성되지 않았는데, `finally`에서 `db.is_connected()`를 호출하여 에러가 발생했다.

해결:
- `db = None`으로 먼저 선언
- `if db is not None and db.is_connected():` 조건 사용

---

## Review

오늘은 MySQL과 PostgreSQL을 처음 다루면서, 데이터베이스 설치부터 접속, GUI 도구 사용, Python 연결까지 실습했다.

단순히 명령어를 외우는 것이 아니라, 실제 개발 환경에서 자주 만날 수 있는 문제들을 직접 겪었다.

특히 다음을 많이 배웠다.

- MySQL은 접속 후 사용할 DB를 선택해야 한다.
- SQL 명령어는 세미콜론이 중요하다.
- 환경 변수 PATH가 잡혀야 CMD에서 명령어를 사용할 수 있다.
- Python에서 DB 연결 실패를 고려한 예외 처리가 필요하다.
- 코드 수정 후 저장하지 않으면 이전 코드가 계속 실행된다.

처음에는 작은 에러가 많았지만, 에러 메시지를 하나씩 따라가면서 원인을 좁히는 연습이 되었다.

프로젝트를 하다가 다시 기본 수업으로 돌아오니 조금 낯설었지만, 오히려 기본기를 다시 확인하는 시간이 되었다.

---

## Next
- MySQL 테이블 생성과 수정 복습
- `INSERT`, `SELECT`, `UPDATE`, `DELETE` 실습
- 제약조건과 기본키, 외래키 학습
- DBeaver에서 ERD와 테이블 관계 확인
- Python에서 MySQL CRUD 연결 실습