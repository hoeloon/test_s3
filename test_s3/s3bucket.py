import datetime
class S3_Bucket:
    def getTimeStamp(self):
        out = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        return out