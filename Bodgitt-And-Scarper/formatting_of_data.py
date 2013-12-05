# coding:utf-8
import data_conn


class FormattingOfData:

    def __init__(self):
        self.data_conn = data_conn.DataConn()

    def formatted_records(self):
        record  = self.data_conn.records()
        formatted_record = []

        for number_of_records in range(self.data_conn.number_of_records()):
            dicionario = {'id': number_of_records}

            for number_of_fields in range(self.data_conn.start_of_file()["number_of_fields"]):
                dicionario[self.data_conn.meta_dada[number_of_fields]['field_name']] = record[number_of_records][number_of_fields]

            dicionario["byte_flag"] =  record[number_of_records][6]
            formatted_record.append(dicionario)

        return formatted_record


