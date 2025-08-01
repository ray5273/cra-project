from mission2.src.user import User

class Database:
    def __init__(self, filename):
        self.num_user_id = 0
        self.name_to_id = {}
        self.id_to_name = {}
        self.users_db = [] # User Class Array

        # initialize database
        self._make_database(filename)

    def _make_database(self, filename):
        with open(filename, "r") as file:
            for line in file:
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    name, day = parts[0], parts[1]
                    self._add_name_to_database(name)
                    user_id = self._get_user_id_by_name(name)
                    self._add_user_attendance_data(user_id, day)

    def _get_user_id_by_name(self, name):
        return self.name_to_id[name]

    def _add_name_to_database(self, name):
        if name not in self.name_to_id:
            self.name_to_id[name] = self.num_user_id
            self.id_to_name[self.num_user_id] = name
            self.users_db.append(User(name, self.num_user_id))
            self.num_user_id += 1 # 0부터 시작하게 바꿈

    def _add_user_attendance_data(self, id, day):
        target_user = self.users_db[id]
        target_user.add_attendance_data(day)

def run_attendance_program():
    try:
        db = Database("attendance_weekday_500.txt")
        removed_user = []
        for user in db.users_db:
            # User 이름, 점수, Grade 출력
            user.print_user_info()
            # Remove user 저장
            if user.is_remove_candidate():
                removed_user.append(user.name)
        # Remove 유저 삭제
        print("\nRemoved player")
        print("==============")
        # Remove 유저 출력
        for user in removed_user:
            print(user)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    run_attendance_program()
