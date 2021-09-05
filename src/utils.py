import time


def delay_ms(n: int) -> None:
    time.sleep(n / 100000.0)
