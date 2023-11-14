# television.py
class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__volume_before_mute = self.__volume
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume = self.__volume_before_mute
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__status and not self.__muted and self.__volume < self.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self):
        if self.__status and not self.__muted and self.__volume > self.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

