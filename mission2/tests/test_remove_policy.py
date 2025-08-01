from mission2.src.remove_policy import RemovePolicy, remove_policy_factory, LegacyRemovePolicy, FourGradeRemovePolicy
from mission2.src.grade_policy import GradePolicy, LegacyGradePolicy, FourGradePolicy


def test_legacy_remove_policy_factory():
    # Given : legacy Grade Policy
    point = 0
    legacy_grade_policy = LegacyGradePolicy(point)
    attendance = []

    # When : remove_policy_factory() is called
    policy = remove_policy_factory(legacy_grade_policy, attendance)

    # Then : instance is LegacyRemovePolicy
    assert isinstance(policy, LegacyRemovePolicy)

def test_four_grade_remove_policy_factory():
    # Given : four grade policy
    point = 0
    four_grade_policy = FourGradePolicy(point)
    attendance = []

    # When : remove_policy_factory() is called
    policy = remove_policy_factory(four_grade_policy, attendance)

    # Then : instance is FourGradeRemovePolicy
    assert isinstance(policy, FourGradeRemovePolicy)

def test_legacy_policy_is_remove_candidate_false():
    # Given : legacy Grade Policy
    point = 50
    legacy_grade_policy = LegacyGradePolicy(point)
    attendance = [0 for _ in range(7)]

    # When : remove_policy_factory() is called
    policy = remove_policy_factory(legacy_grade_policy, attendance)

    # Then : instance is LegacyRemovePolicy
    assert isinstance(policy, LegacyRemovePolicy)

    # When : is_remove_candidate() is called
    # Then : result is False because grade is not normal
    assert policy.is_remove_candidate() == False

def test_legacy_policy_is_remove_candidate_true():
    # Given : legacy Grade Policy
    point = 10
    legacy_grade_policy = LegacyGradePolicy(point)
    attendance = [0 for _ in range(7)]

    # When : remove_policy_factory() is called
    policy = remove_policy_factory(legacy_grade_policy, attendance)

    # Then : instance is LegacyRemovePolicy
    assert isinstance(policy, LegacyRemovePolicy)

    # When : is_remove_candidate() is called
    # Then : result is True because grade is normal and no wednesday, weekend data
    assert policy.is_remove_candidate() == True

def test_four_grade_is_remove_candidate():
    # Given : four grade policy
    point = 0
    four_grade_policy = FourGradePolicy(point)
    attendance = []

    # When : remove_policy_factory() is called
    policy = remove_policy_factory(four_grade_policy, attendance)

    # Then : instance is FourGradeRemovePolicy
    assert isinstance(policy, FourGradeRemovePolicy)

    # When : is_remove_candidate() is called
    # Then : result is True
    assert policy.is_remove_candidate() == True
