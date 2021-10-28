import datetime


class TimeUtil:
    @staticmethod
    def str_to_second(time: str) -> int:
        return sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))

    @staticmethod
    def second_to_datetime(seconds: int):
        return datetime.timedelta(seconds=seconds)