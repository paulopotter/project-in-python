# coding: utf-8


class RecordNotFoundException(Exception):
    def __str__(self):
        return 'Registro não encontrado.'


class DuplicateKeyException(Exception):
    def __str__(self):
        return 'Registro com posição duplicada.'
