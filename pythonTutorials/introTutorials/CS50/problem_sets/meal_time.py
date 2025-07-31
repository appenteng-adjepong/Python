def main():
    while True:
        time = input("What time is it? ").lower()
        hours = convert(time)
        print(hours)
        if 7.00 <= hours <= 8.00:
            print("breakfast time.")
        elif 12.00 <= hours <= 13.00:
            print("lunch time.")
        elif 18.00 <= hours <= 19.00:
            print("dinner time.")
        else:
            print("You shouldn't be eating at this time.")



def convert(time):
    if "a.m." in time:
        time = time.split(":")
        time[1] = time[1].split(" ")
        time[1].remove("a.m.")
        result = float(time[0]) + 1/60*float(time[1][0])
        if result == 12.00:
            result = float(0)
            
    elif "p.m." in time:
        time = time.split(":")
        time[1] = time[1].split(" ")
        time[1].remove("p.m.")
        result = 12.00 + float(time[0]) + 1/60*float(time[1][0])
        if result == 24.00:
            result = float(12)
    else:
        time = time.split(":")
        result = float(time[0]) + 1/60*float(time[1])
    return result

if __name__ == "__main__":
    main()