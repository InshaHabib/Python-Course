import speedtest

def Speed_Test():
    test = speedtest.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print(f"Download speed in Mbps is = {down_speed}")

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print(f"Upload speed in Mbps is = {up_speed}")

    # HOW FAST THE INTERNET IS: LATENCY
    ping = test.results.ping
    print(f"Ping = {ping}")

Speed_Test()
