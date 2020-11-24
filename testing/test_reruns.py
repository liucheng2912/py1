import pytest


@pytest.mark.flaky(reruns=5)
def test_reruns():
    assert False
    print("aaaaaaaaaaaaaaaa")
