def convert(time):
    t1 , t2 = time.split(":")
    t1 = t1.strip()
    t2 = t2.strip()
    return float(t1) + float(t2) / 60.0

def main():
    time=input("what's the time?")
    time_float = convert(time)
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")

main()