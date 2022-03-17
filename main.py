from speedtester import InternetSpeedTwitterBot

speed_exe = InternetSpeedTwitterBot()

speed_exe.get_internet_speed()
if speed_exe.download_get < 180 or speed_exe.upload_get < 40:
    speed_exe.tweet_at_provider()

