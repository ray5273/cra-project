from .grade_policy import GradePolicy, grade_policy_factory, LEGACY_GRADE_POLICY
from .point_policy import PointPolicy, point_policy_factory, LEGACY_POINT_POLICY
from .remove_policy import RemovePolicy, remove_policy_factory
# Day Constants
MONDAY=0
TUESDAY=1
WEDNESDAY=2
THURSDAY=3
FRIDAY=4
SATURDAY=5
SUNDAY=6
DAYS=7

# User class
class User:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
        self._attendance = [0 for _ in range(DAYS)] # 월요일 ~ 일요일 데이터

    def get_points(self):
        point_policy: PointPolicy = point_policy_factory(self._attendance, LEGACY_POINT_POLICY)
        # 기본 점수 + 추가 점수
        return point_policy.get_base_point() + point_policy.get_extra_point()

    def get_grade(self):
        grade_policy:GradePolicy = grade_policy_factory(self.get_points(), LEGACY_GRADE_POLICY)
        return grade_policy.determine_grade()

    def is_remove_candidate(self)-> bool:
        grade_policy: GradePolicy = grade_policy_factory(self.get_points(), LEGACY_GRADE_POLICY)
        remove_policy = remove_policy_factory(grade_policy, self._attendance)
        return remove_policy.is_remove_candidate()

    def add_attendance_data(self, day:str):
        if day == "monday":
            self._attendance[MONDAY] += 1
        elif day == "tuesday":
            self._attendance[TUESDAY] += 1
        elif day == "wednesday":
            self._attendance[WEDNESDAY] += 1
        elif day == "thursday":
            self._attendance[THURSDAY] += 1
        elif day == "friday":
            self._attendance[FRIDAY] += 1
        elif day == "saturday":
            self._attendance[SATURDAY] += 1
        elif day == "sunday":
            self._attendance[SUNDAY] += 1

    def print_user_info(self):
        print(f"NAME : {self.name}, POINT : {self.get_points()}, GRADE : {self.get_grade()}", end="\n")