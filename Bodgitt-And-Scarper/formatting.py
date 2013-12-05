# coding:utf-8
import dbSchema


class Formatting:

    def __init__(self):
        self.db_schema = dbSchema.DbSchema()

    def formatted_records(self):
        record  = self.db_schema.records()
        formatted_record = []

        for number_of_records in range(self.db_schema.number_of_records()):
            dicionario = {'id': number_of_records}

            for number_of_fields in range(self.db_schema.start_of_file()["number_of_fields"]):
                dicionario[self.db_schema.meta_dada[number_of_fields]['field_name']] = record[number_of_records][number_of_fields]

            dicionario["byte_flag"] =  record[number_of_records][6]
            formatted_record.append(dicionario)

        return formatted_record


