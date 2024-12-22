from icecream import ic

value = "hello"
valued = value.encode(encoding="ascii",errors="ignore")

ic(valued.decode())