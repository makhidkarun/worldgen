import pytest
import worldgenlib


@pytest.fixture
def size_gen_values():
    return list(range(10))


@pytest.fixture
def worldatmo_values():
    return list(range(16))


@pytest.fixture
def worldhyd_values():
    return list(range(11))


def test_size_gen():
    result = worldgenlib.size_gen()
    assert result in size_gen_values()


def test_atmo_gen():
    result = worldgenlib.atmo_gen(worldgenlib.size_gen())
    assert result in worldatmo_values()


def test_hyd_gen():
    result = worldgenlib.hyd_gen(worldgenlib.size_gen())
    assert result in worldhyd_values()
