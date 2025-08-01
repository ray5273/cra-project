from mission2.src.grade_policy import LegacyGradePolicy
from mission2.src.user import User, MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY
monday_str = "monday"
tuesday_str = "tuesday"
wednesday_str = "wednesday"
thursday_str = "thursday"
friday_str = "friday"
saturday_str = "saturday"
sunday_str = "sunday"

def generate_point(user,target_point):
    for _ in range(target_point):
        user.add_attendance_data(monday_str)

def test_get_grade_gold():
    # Given : testuser score is 50 (minimum score of gold)
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name,test_user_id)
    generate_point(user,50)

    # When : get_grade() is called
    grade = user.get_grade()

    # Then : grade is GOLD
    assert grade == LegacyGradePolicy.GOLD

def test_get_grade_silver():
    # Given : testuser score is 30 (miminum score of silver)
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name,test_user_id)
    generate_point(user,30)

    # When : get_grade() is called
    grade = user.get_grade()

    # Then : grade is SILVER
    assert grade == LegacyGradePolicy.SILVER

def test_get_grade_normal():
    # Given : testuser score is under 30
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name,test_user_id)
    generate_point(user,29)

    # When : get_grade() is called
    grade = user.get_grade()
    # Then : grade is NORMAL
    assert grade == LegacyGradePolicy.NORMAL



def test_add_attendance_data_monday():
    # Given : testuser
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # When : add_attendance_data is called with monday
    user.add_attendance_data(monday_str)

    # Then : attendance_data is updated(monday)
    assert user._attendance[MONDAY] == 1

def test_add_attendance_data_tuesday():
    # Given : testuser
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # When : add_attendance_data is called with tuesday
    user.add_attendance_data(tuesday_str)

    # Then : attendance_data is updated(TUESDAY)
    assert user._attendance[TUESDAY] == 1

def test_add_attendance_data_wednesday():
    # Given : testuser
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # When : add_attendance_data is called with wednesday
    user.add_attendance_data(wednesday_str)

    # Then : attendance_data is updated(wednesday)
    assert user._attendance[WEDNESDAY] == 1

def test_add_attendance_data_thursday():
    # Given : testuser
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # When : add_attendance_data is called with thursday
    user.add_attendance_data(thursday_str)

    # Then : attendance_data is updated(thursday)
    assert user._attendance[THURSDAY] == 1

def test_add_attendance_data_friday():
    # Given : testuser
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # When : add_attendance_data is called with friday
    user.add_attendance_data(friday_str)

    # Then : attendance_data is updated(friday)
    assert user._attendance[FRIDAY] == 1

def test_add_attendance_data_saturday():
    # Given : testuser
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # When : add_attendance_data is called with saturday
    user.add_attendance_data(saturday_str)

    # Then : attendance_data is updated(saturday)
    assert user._attendance[SATURDAY] == 1

def test_add_attendance_data_sunday():
    # Given : testuser
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # When : add_attendance_data is called with sunday
    user.add_attendance_data(sunday_str)

    # Then : attendance_data is updated(sunday)
    assert user._attendance[SUNDAY] == 1


def test_get_points_wednesday():
    # Given : testuser is given
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # Given : add_attendance_data with wednesday
    user.add_attendance_data(wednesday_str)

    # When : get_points() is called()
    point = user.get_points()

    # Then : expected point is 3
    assert point == 3

def test_get_points_wednesday_10_times():
    # Given : testuser is given
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # Given : add_attendance_data with wednesday 10 times
    for _ in range(10):
        user.add_attendance_data(wednesday_str)

    # When : get_points() is called()
    point = user.get_points()

    # Then : expected point is 30 (base) + 10 (extra)
    assert point == 30 + 10

def test_get_points_weekend():
    # Given : testuser is given
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # Given : add_attendance_data with weekend data including saturday and sunday total 10times.
    for _ in range(5):
        user.add_attendance_data(saturday_str)
        user.add_attendance_data(sunday_str)

    # When : get_points() is called()
    point = user.get_points()

    # Then : expected point is 20 (base) + 10 (extra)
    assert point == 20 + 10

def test_get_points_weekend_10_times():
    # Given : testuser is given
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # Given : add_attendance_data with weekend data including saturday and sunday.
    user.add_attendance_data(saturday_str)
    user.add_attendance_data(sunday_str)

    # When : get_points() is called()
    point = user.get_points()

    # Then : expected point is 4 (2+2)
    assert point == 4

def test_get_points_normal_weekday():
    # Given : testuser is given
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # Given : add_attendance_data with weekend data including mon - friday (without wednesday)
    user.add_attendance_data(monday_str)
    user.add_attendance_data(tuesday_str)
    user.add_attendance_data(thursday_str)
    user.add_attendance_data(friday_str)

    # When : get_points() is called()
    point = user.get_points()

    # Then : expected point is 4 (1+1+1+1)
    assert point == 4


def test_is_remove_candidate_true():
    # Given : testuser score is under 30 (NORMAL)
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)
    user.add_attendance_data(monday_str)
    user.add_attendance_data(tuesday_str)
    user.add_attendance_data(thursday_str)
    user.add_attendance_data(friday_str)

    # When : is_remove_candidate() is called
    result = user.is_remove_candidate()

    # Then : result is False
    assert result == True

def test_is_remove_candidate_false_attend_wednesday():
    # Given : testuser score is under 30 (NORMAL), but attended wednesday
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)
    user.add_attendance_data(monday_str)
    user.add_attendance_data(tuesday_str)
    user.add_attendance_data(wednesday_str)
    user.add_attendance_data(thursday_str)
    user.add_attendance_data(friday_str)

    # When : is_remove_candidate() is called
    result = user.is_remove_candidate()

    # Then : result is False
    assert result == False

def test_is_remove_candidate_false_attend_saturday():
    # Given : testuser score is under 30 (NORMAL), but attended saturday
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)
    user.add_attendance_data(monday_str)
    user.add_attendance_data(tuesday_str)
    user.add_attendance_data(thursday_str)
    user.add_attendance_data(friday_str)
    user.add_attendance_data(saturday_str)

    # When : is_remove_candidate() is called
    result = user.is_remove_candidate()

    # Then : result is False
    assert result == False

def test_is_remove_candidate_false_attend_sunday():
    # Given : testuser score is under 30 (NORMAL), but attended sunday
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)
    user.add_attendance_data(monday_str)
    user.add_attendance_data(tuesday_str)
    user.add_attendance_data(thursday_str)
    user.add_attendance_data(friday_str)
    user.add_attendance_data(sunday_str)

    # When : is_remove_candidate() is called
    result = user.is_remove_candidate()

    # Then : result is False
    assert result == False


def test_is_remove_candidate_false_over_silver_grade():
    # Given : testuser score is equal or more than 30 (more than silver), but not attended wednesday and weekend
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)
    generate_point(user, 30)
    user.add_attendance_data(monday_str)
    user.add_attendance_data(tuesday_str)
    user.add_attendance_data(thursday_str)
    user.add_attendance_data(friday_str)

    # When : is_remove_candidate() is called
    result = user.is_remove_candidate()

    # Then : result is False
    assert result == False

def test_print_user_info(capsys):
    # Given : test user with id 1234
    test_user_name = "testuser"
    test_user_id = 1234
    user = User(test_user_name, test_user_id)

    # When : print_user_info() is called
    user.print_user_info()

    captured = capsys.readouterr()
    assert captured.out == f"NAME : {test_user_name}, POINT : {user.get_points()}, GRADE : {user.get_grade()}\n"
    assert "" in captured.err
