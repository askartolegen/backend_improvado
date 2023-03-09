from abc import ABC, abstractmethod
import csv
import json


class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data, output_file):
        pass


class CSVReportGenerator(ReportGenerator):
    def generate_report(self, data, output_file):
        data_as_list = [list(d.values()) for d in data]
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(data_as_list)


class TSVReportGenerator(ReportGenerator):
    def generate_report(self, data, output_file):
        data_as_list = [list(d.values()) for d in data]
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(data_as_list)


class JSONReportGenerator(ReportGenerator):
    def generate_report(self, data, output_file):
        with open(output_file, 'w') as f:
            json.dump(data, f)
