import mysql.connector

# 1. 데이터베이스 연결 설정
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",          # 사용자 계정
        password=r"mosejong12",      # 아까 말씀하신 비번
        database="est" # 접속할 데이터베이스 이름
    )
    cursor = db.cursor()

    # 2. 삽입할 데이터 (튜플 리스트 형태)
    users_data = [
        ('user11', 'user1@mail.com'),
        ('user12', 'user2@mail.com'),
        ('user13', 'user3@mail.com'),
        ('user14', 'user4@mail.com'),
        ('user15', 'user5@mail.com'),
        ('user16', 'user6@mail.com'),
        ('user17', 'user7@mail.com'),
        ('user18', 'user8@mail.com'),
        ('user19', 'user9@mail.com'),
        ('user20', 'user10@mail.com')
    ]

    # 3. SQL 실행 (executemany를 쓰면 성능이 훨씬 좋습니다)
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    cursor.executemany(sql, users_data)

    # 4. 데이터 확정 (Commit) - 중요!
    db.commit()

    print(f"{cursor.rowcount}개의 행이 성공적으로 삽입되었습니다.")

except mysql.connector.Error as err:
    print(f"에러 발생: {err}")

finally:
    # 5. 연결 종료
    if db.is_connected():
        cursor.close()
        db.close()