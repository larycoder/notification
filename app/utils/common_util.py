import datetime, calendar


# class used to generate key
class KeyUtil:
    @staticmethod
    def get_utc_timestamp():
        current_datetime = datetime.datetime.utcnow()
        current_timetuple = current_datetime.utctimetuple()
        return calendar.timegm(current_timetuple)

    @staticmethod
    def get_key(topic:str):
        timestamp = KeyUtil.get_utc_timestamp()
        topic_hashed = hash(topic)
        return str(timestamp) + '+' + str(topic_hashed)


class DataUtil:
    @staticmethod
    def convert_data_to_dict(schema, data_list):
        dict_list = []
        for data in data_list:
            dict_data = {}
            for index, key in enumerate(schema):
                dict_data[key] = data[index]
            dict_list.append(dict_data)
        return dict_list