import datetime

def log(text):
    now = datetime.datetime.now()
    print(f"[{now.strftime("%H:%M:%S")} INFO]: {text}")