class Television:
    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        # Instance variables
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume_before_mute: int = 0
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power status of the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status of the television."""
        if self.__status:
            if not self.__muted:
                self.__volume_before_mute = self.__volume
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume = self.__volume_before_mute
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the current channel by 1, considering the maximum channel."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the current channel by 1, considering the minimum and maximum channel."""
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by 1 if the television is on and not muted."""
        if self.__status and not self.__muted and self.__volume < self.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by 1 if the television is on, not muted, and above the minimum volume."""
        if self.__status and not self.__muted and self.__volume > self.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """Return a string representation of the television's status, channel, and volume."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
