import datetime, calendar


# class used to generate key
class Key:
    @staticmethod
    def get_utc_timestamp():
        current_datetime = datetime.datetime.utcnow()
        current_timetuple = current_datetime.utctimetuple()
        return calendar.timegm(current_timetuple)

    @staticmethod
    def get_key(topic:str):
        timestamp = Key.get_utc_timestamp()
        topic_hashed = hash(topic)
        return str(timestamp) + '+' + str(topic_hashed)
