#!/usr/bin/env python3

'''
Project Module
'''
import csv

class Pitch:
    def __init__(self, name, result, spreadsheet):
        self.spreadsheet = spreadsheet
        self.name = name
        self.result = result

    def avg_start_speed(self): #Calculates average start speed
        startspeed = []
        for row in self.spreadsheet:
            if row['pitch_type'] == self.name and row['type'] == self.result:
                startspeed.append(float(row['start_speed']))
        return round(sum(startspeed) / len(startspeed),2)

    def avg_end_speed(self): #Calculates average end speed
        endspeed = []
        for row in self.spreadsheet:
            if row['pitch_type'] == self.name and row['type'] == self.result:
                endspeed.append(float(row['end_speed']))
        return round(sum(endspeed) / len(endspeed),2)


    def startpitch(self):  #Calls avg_start_speed and prints it
        avg_start_speed = self.avg_start_speed()
        print("The average start speed of a {} for a {} is {}".format(self.result, self.name,
            avg_start_speed))

    def endpitch(self):  #Calls avg_end_speed and prints it
        avg_end_speed = self.avg_end_speed()
        print("The average end speed of a {} for a {} is {}".format(self.result, self.name,
            avg_end_speed))

with open('pitches.csv', encoding='utf-8-sig') as fh:
    spreadsheet = csv.DictReader(fh)
    #p1 = Pitch("CH", "S", spreadsheet)
    #p1.endpitch()
    #.seek(0) #Setting to the beggining of the file
    #spreadsheet.__init__(fh) #initialising the spreadsheet object again with the handle
    #p2 = Pitch("CU", "B", spreadsheet)
    #p2.startpitch()
