import psycopg2

def sign_up_postgresql():
    try:
        # 1. DB 연결 설정
        # 포스트그레스 기본 포트는 5432입니다. (설치 시 5433으로 바꾸셨다면 수정 필요)
        conn = psycopg2.connect(
            host="localhost",
            database="postgres", # 기본 생성된 db 이름
            user="postgres",     # 포스트그레스 기본 사용자명
            password="mosejong12",     # 본인이 설정한 비밀번호
            port="5432"
        )
        cur = conn.cursor()

        # 2. 테이블 생성 (없을 경우에만)
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100)
            );
        ''')

        print("=== PostgreSQL 회원가입 ===")
        name = input("아이디: ")
        mail = input("이메일: ")

        # 3. 데이터 삽입 (%s 사용은 동일합니다)
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cur.execute(sql, (name, mail))

        # 4. 저장 및 종료
        conn.commit()
        print(f"\n[성공] {name}님, PostgreSQL서버에 저장되었습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")

    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    sign_up_postgresql()