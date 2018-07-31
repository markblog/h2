class Validator:

    @staticmethod
    def existAndNotNone(parameters, data):
        for parameter in parameters:
            if data.get(parameter, None):
                return False