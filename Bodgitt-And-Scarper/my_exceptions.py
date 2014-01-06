

class RecordNotFoundException(Exception):
    def __str__(self):
        return 'Record with this position not found.'


class DuplicateKeyException(Exception):
    def __str__(self):
        return 'Record with this position is duplicate.'
