import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power(tv):
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute(tv):
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Keeping the TV muted
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_up(tv):
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    for _ in range(Television.MAX_CHANNEL):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down(tv):
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    for _ in range(Television.MAX_CHANNEL + 1):  # Adjusted range to cover the wrap-around
        tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_up(tv):
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Keeping the TV muted while adjusting volume
    for _ in range(Television.MAX_VOLUME):
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down(tv):
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    for _ in range(Television.MAX_VOLUME):
        tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Keeping the TV muted while adjusting volume
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Ensuring volume does not go below the minimum

if __name__ == "__main__":
    pytest.main()

