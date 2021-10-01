from datetime import datetime, date


class JsonEncoder:

    # Requirement:
    # object must include:
    # toJSON method
    @staticmethod
    def encode(obj):
        result = None
        if isinstance(obj, list):
            result = []
            for v in obj:
                result.append(JsonEncoder.encode(v))
        elif isinstance(obj, dict):
            result = {k: JsonEncoder.encode(v)
                      for k, v in obj.items()}
        elif (
                hasattr(obj, 'toJSON')
                and callable(getattr(obj, 'toJSON'))
        ):
            result = JsonEncoder.encode(obj.toJSON())
        elif isinstance(obj, (datetime, date)):
            result = obj.isoformat()
        else:
            result = obj

        if result is None:
            raise RuntimeError('Could not encode object.')
        return result
