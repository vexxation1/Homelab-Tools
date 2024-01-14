import csv
import os
import pandas as pd



class Device:
    def __init__(self) -> None:
        self.name = "Default_Name"
        self.IP = "127.0.0.1"
    
    def update(self, name: str, IP: str) -> None:
        self.name = name
        self.IP = IP


class Database:
    def __init__(self) -> None:
        pass

    @staticmethod
    def update():
        if os.path.isfile("database.csv"):
            pass

        else:
                with open('database.csv', mode='w') as DB:
                    fields = ['UID', 'Device', 'IP']
                    init = {'UID': '0', 'Device': 'INIT', 'IP': "NONE"}
                    writer = csv.DictWriter(DB, fieldnames=fields)
                    writer.writeheader()
                    writer.writerow(init)
        
        return pd.read_csv('database.csv', index_col='UID')

    @staticmethod
    def create(frame, record: tuple):
            UID = frame.shape[0]
            device = record[0]
            IP = record[1]
            record = pd.DataFrame({'UID': [UID],
                                   'Device': [device],
                                   'IP': [IP]})
            
            record.to_csv('database.csv', mode='a', header=False, index=False)
            return Database.update()
    
    @staticmethod
    def delete(frame, index):
        return frame.drop(index)

    @staticmethod
    def alter(frame, old_record, new_record):
        return frame.replace(old_record, new_record)