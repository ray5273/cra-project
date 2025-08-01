# Day Constants
MONDAY=0
TUESDAY=1
WEDNESDAY=2
THURSDAY=3
FRIDAY=4
SATURDAY=5
SUNDAY=6
DAYS=7

# Grades Constants
GOLD = "GOLD"
SILVER = "SILVER"
NORMAL = "NORMAL"

# User class
class User:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
        self.attendance = [0 for _ in range(DAYS)] # 월요일 ~ 일요일 데이터
        self.points = 0
        self.grade = None

    def get_grade(self):
        if self.points >= 50:
            self.grade = GOLD
        elif self.points >= 30:
            self.grade = SILVER
        else:
            self.grade = NORMAL
        return self.grade

    def get_points(self):
        # 기본 점수
        for day in range(7):
            if day == WEDNESDAY:
                self.points += 3 * self.attendance[day]
            elif day == SATURDAY or day == SUNDAY:
                self.points += 2 * self.attendance[day]
            else:
                self.points += self.attendance[day]
        # 추가 점수
        if self.attendance[WEDNESDAY] >= 10:
            self.points += 10
        if self.attendance[SATURDAY] + self.attendance[SUNDAY] >= 10:
            self.points += 10
        return self.points

    def is_remove_candidate(self)-> bool:
        if (self.get_grade() == "NORMAL" and
                (self.attendance[SUNDAY] == 0 and self.attendance[SATURDAY] == 0 and self.attendance[WEDNESDAY] == 0)):
            return True
        return False

    def print_user_info(self):
        print(f"NAME : {self.name}, POINT : {self.get_points()}, GRADE : {self.get_grade()}", end="\n")

class Database:
    def __init__(self, filename):
        self.num_user_id = 0
        self.name_to_id = {}
        self.id_to_name = {}
        self.users = [] # User Class Array

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
            self.users.append(User(name,self.num_user_id))
            self.num_user_id += 1 # 0부터 시작하게 바꿈

    def _add_user_attendance_data(self, id, day):
        target_user = self.users[id]
        if day == "monday":
            target_user.attendance[MONDAY] += 1
        elif day == "tuesday":
            target_user.attendance[TUESDAY] += 1
        elif day == "wednesday":
            target_user.attendance[WEDNESDAY] += 1
        elif day == "thursday":
            target_user.attendance[THURSDAY] += 1
        elif day == "friday":
            target_user.attendance[FRIDAY] += 1
        elif day == "saturday":
            target_user.attendance[SATURDAY] += 1
        elif day == "sunday":
            target_user.attendance[SUNDAY] += 1

def run_attendance_program():
    try:
        db = Database("attendance_weekday_500.txt")
        removed_user = []
        for user in db.users:
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
