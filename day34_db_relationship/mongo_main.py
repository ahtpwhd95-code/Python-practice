from pymongo import MongoClient

def sign_up_mongodb():
    try:
        # 1. MongoDB 연결 (기본 포트: 27017)
        # 설치 시 아이디/비번을 설정하지 않았다면 아래 주소로 바로 연결됩니다.
        client = MongoClient("mongodb://localhost:27017/")
        
        # 2. 데이터베이스 및 컬렉션 선택 (없으면 자동으로 생성됨)
        db = client["est"]           # 데이터베이스 이름
        users_col = db["users"]         # 컬렉션(테이블 역할) 이름

        print("=== MongoDB 회원가입 ===")
        username = input("아이디: ")
        email = input("이메일: ")

        # 3. 데이터 준비 (딕셔너리 형태 = JSON)
        user_data = {
            "username": username,
            "email": email
        }

        # 4. 데이터 삽입
        result = users_col.insert_one(user_data)

        print(f"\n[성공] {username}님, MongoDB에 저장되었습니다!")
        print(f"생성된 문서 ID: {result.inserted_id}")

    except Exception as e:
        print(f"오류 발생: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    sign_up_mongodb()