from mission2.src.grade_policy import LEGACY_GRADE_POLICY, FOUR_GRADE_POLICY, grade_policy_factory, FourGradePolicy, LegacyGradePolicy

def test_grade_policy_factory_legacy():
    # Given : point and legacy grade policy constant.
    point = 0
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,LEGACY_GRADE_POLICY)
    # Then : instance is LegacyGradePolicy
    assert isinstance(policy, LegacyGradePolicy)

def test_grade_policy_factory_default():
    # Given : point without constant
    point = 0
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,"")

    # Then : instance is LegacyGradePolicy
    assert isinstance(policy, LegacyGradePolicy)

def test_grade_policy_factory_four_grade():
    # Given : point with FOUR_GRADE_POLICY
    point = 0
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,FOUR_GRADE_POLICY)

    # Then : instance is FourGradePolicy
    assert isinstance(policy, FourGradePolicy)

def test_get_policy_name_legacy():
    # Given : point without constant
    point = 0
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,"")

    # Then : instance is LegacyGradePolicy
    assert isinstance(policy, LegacyGradePolicy)

    # When : get_policy_name() is called
    # Then : policy name must be same as LEGACY_GRADE_POLICY
    assert policy.get_policy_name() == LEGACY_GRADE_POLICY

def test_get_policy_name_four_grade():
    # Given : point with FOUR_GRADE_POLICY
    point = 0
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,FOUR_GRADE_POLICY)

    # Then : instance is FourGradePolicy
    assert isinstance(policy, FourGradePolicy)

    # When : get_policy_name() is called
    # Then : policy name must be same as FOUR_GRADE_POLICY
    assert policy.get_policy_name() == FOUR_GRADE_POLICY

def test_determine_grade_legacy_determine_gold():
    # Given : point 70
    point = 70
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,"")

    # Then : instance is LegacyGradePolicy
    assert isinstance(policy, LegacyGradePolicy)

    # When : determine_grade() is called
    # Then : result must be GOLD
    assert policy.determine_grade() == LegacyGradePolicy.GOLD

def test_determine_grade_legacy_determine_silver():
    # Given : point 30
    point = 30
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,"")

    # Then : instance is LegacyGradePolicy
    assert isinstance(policy, LegacyGradePolicy)

    # When : determine_grade() is called
    # Then : result must be SILVER
    assert policy.determine_grade() == LegacyGradePolicy.SILVER

def test_determine_grade_legacy_determine_normal():
    # Given : point 20
    point = 20
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,"")

    # Then : instance is LegacyGradePolicy
    assert isinstance(policy, LegacyGradePolicy)

    # When : determine_grade() is called
    # Then : result must be NORMAL
    assert policy.determine_grade() == LegacyGradePolicy.NORMAL

def test_determine_grade_four_determine_platinum():
    # Given : point 70
    point = 70

    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,FOUR_GRADE_POLICY)

    # Then : instance is FourGradePolicy
    assert isinstance(policy, FourGradePolicy)

    # When : determine_grade() is called
    # Then : result must be PLATINUM
    assert policy.determine_grade() == FourGradePolicy.PLATINUM

def test_determine_grade_four_determine_gold():
    # Given : point 50
    point = 50

    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,FOUR_GRADE_POLICY)

    # Then : instance is FourGradePolicy
    assert isinstance(policy, FourGradePolicy)

    # When : determine_grade() is called
    # Then : result must be GOLD
    assert policy.determine_grade() == FourGradePolicy.GOLD


def test_determine_grade_four_determine_silver():
    # Given : point 30
    point = 30

    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,FOUR_GRADE_POLICY)

    # Then : instance is FourGradePolicy
    assert isinstance(policy, FourGradePolicy)

    # When : determine_grade() is called
    # Then : result must be SILVER
    assert policy.determine_grade() == FourGradePolicy.SILVER

def test_determine_grade_four_determine_normal():
    # Given : point 10
    point = 10

    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,FOUR_GRADE_POLICY)

    # Then : instance is FourGradePolicy
    assert isinstance(policy, FourGradePolicy)

    # When : determine_grade() is called
    # Then : result must be NORMAL
    assert policy.determine_grade() == FourGradePolicy.NORMAL

def test_get_policy_name_determine_normal():
    # Given : point 20
    point = 20
    # When : grade_policy_factory() is called
    policy = grade_policy_factory(point,"")

    # Then : instance is LegacyGradePolicy
    assert isinstance(policy, LegacyGradePolicy)

    # When : determine_grade() is called
    # Then : result must be NORMAL
    assert policy.determine_grade() == LegacyGradePolicy.NORMAL
