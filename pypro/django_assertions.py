from django.test.testcases import SimpleTestCase

_test_case = SimpleTestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains
