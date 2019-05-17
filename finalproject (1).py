#!/usr/bin/env python3

'''
Project Start
'''
import csv
import pandas as pd
from prettytable import PrettyTable
import fp2

fh = open('pitches.csv', encoding='utf-8-sig')
spreadsheet = csv.DictReader(fh)
df = pd.read_csv("pitches.csv", encoding='utf-8-sig')
changeup = []  #CH
curveball = [] #CU
cutter = []    #FC
fourfastball = []  #FF
twofastball = []   #FT
knucklecurve = []  #KC
sinker = []    #SI
slider = []    #SL
pitch_dict = {}
pitch_breakdown = PrettyTable()

def pitch_total(pitch):
    total = len(pitch)
    return str(total)


def main():
    for row in spreadsheet:
        if row['pitch_type'] == 'CH':
            changeup.append(row['type'])

        if row['pitch_type'] == 'CU':
            curveball.append(row['type'])

        if row['pitch_type'] == 'FC':
            cutter.append(row['type'])

        if row['pitch_type'] == 'FF':
            fourfastball.append(row['type'])

        if row['pitch_type'] == 'FT':
            twofastball.append(row['type'])

        if row['pitch_type'] == 'KC':
            knucklecurve.append(row['type'])

        if row['pitch_type'] == 'SI':
            sinker.append(row['type'])

        if row['pitch_type'] == 'SL':
            slider.append(row['type'])

    for row in spreadsheet:
        start_avg.append(row['start_speed'])

    for i, pt in enumerate(df["pitch_type"]):  # i = index, pt = pitch_type
        if pt not in pitch_dict:
            if df["type"][i] == "S":
                strike = 1
                ball = 0
                hit = 0
            if df["type"][i] == "B":
                strike = 0
                ball = 1
                hit = 0
            if df["type"][i] == "X":
                strike = 0
                ball = 0
                hit = 1
            pitch_dict[pt] = [strike, ball, hit, [df["start_speed"][i]],[df["end_speed"][i]]]
        elif pt in pitch_dict:
            if df["type"][i] == "S":
                pitch_dict[pt][0] += 1
            if df["type"][i] == "B":
                pitch_dict[pt][1] += 1
            if df["type"][i] == "X":
                pitch_dict[pt][2] += 1
            pitch_dict[pt][3].append(df["start_speed"][i])
            pitch_dict[pt][4].append(df["end_speed"][i])

    #creates table showing pitch breakdown
    pitch_breakdown.field_names = ["Pitch", "Strike", "Ball", "Hit", "Total", "Average Start Speed", "Average End Speed"]
    pitch_breakdown.add_row(["Changeup", (changeup.count('S')), (changeup.count('B')), (changeup.count('X')), pitch_total(changeup), round(sum(pitch_dict["CH"][3]) / len(pitch_dict["CH"][3]),2), round(sum(pitch_dict["CH"][4]) / len(pitch_dict["CH"][4]),2)])
    pitch_breakdown.add_row(["Curveball", (curveball.count('S')), (curveball.count('B')), (curveball.count('X')), pitch_total(curveball), round(sum(pitch_dict["CU"][3]) / len(pitch_dict["CU"][3]),2), round(sum(pitch_dict["CU"][4]) / len(pitch_dict["CU"][4]),2)])
    pitch_breakdown.add_row(["Cutter", (cutter.count('S')), (cutter.count('B')), (cutter.count('X')), pitch_total(cutter), round(sum(pitch_dict["FC"][3]) / len(pitch_dict["FC"][3]),2), round(sum(pitch_dict["FC"][4]) / len(pitch_dict["FC"][4]),2)])
    pitch_breakdown.add_row(["Four-seam Fastball", (fourfastball.count('S')), (fourfastball.count('B')), (fourfastball.count('X')), pitch_total(fourfastball), round(sum(pitch_dict["FF"][3]) / len(pitch_dict["FF"][3]),2), round(sum(pitch_dict["FF"][4]) / len(pitch_dict["FF"][4]),2)])
    pitch_breakdown.add_row(["Two-seam Fastball" , (twofastball.count('S')), (twofastball.count('B')), (twofastball.count('X')), pitch_total(twofastball), round(sum(pitch_dict["FT"][3]) / len(pitch_dict["FT"][3]),2), round(sum(pitch_dict["FT"][4]) / len(pitch_dict["FT"][4]),2)])
    pitch_breakdown.add_row(["Knuckle curve", (knucklecurve.count('S')), (knucklecurve.count('B')), (knucklecurve.count('X')), pitch_total(knucklecurve), round(sum(pitch_dict["KC"][3]) / len(pitch_dict["KC"][3]),2), round(sum(pitch_dict["KC"][4]) / len(pitch_dict["KC"][4]),2)])
    pitch_breakdown.add_row(["Sinker", (sinker.count('S')), (sinker.count('B')), (sinker.count('X')), pitch_total(sinker), round(sum(pitch_dict["SI"][3]) / len(pitch_dict["SI"][3]),2), round(sum(pitch_dict["SI"][4]) / len(pitch_dict["SI"][4]),2)])
    pitch_breakdown.add_row(["Slider", (slider.count('S')), (slider.count('B')), (slider.count('X')), pitch_total(slider), round(sum(pitch_dict["SL"][3]) / len(pitch_dict["SL"][3]),2), round(sum(pitch_dict["SL"][4]) / len(pitch_dict["SL"][4]),2)])


    print(pitch_breakdown)
    fh.seek(0) #Setting to the beginning of the file
    spreadsheet.__init__(fh) #initialising the spreadsheet object again with the handle
    p1 = fp2.Pitch("CH", "S", spreadsheet)
    p1.startpitch()
    fh.seek(0) #Setting to the beginning of the file
    spreadsheet.__init__(fh) #initialising the spreadsheet object again with the handle
    p1.endpitch()
    fh.seek(0) #Setting to the beginning of the file
    spreadsheet.__init__(fh) #initialising the spreadsheet object again with the handle    p2 = fp2.Pitch("CU", "B", spreadsheet)
    p2 = fp2.Pitch("CU", "B", spreadsheet)
    p2.startpitch()
if __name__ == '__main__':
    assert changeup.count('S') + changeup.count('B') + changeup.count('X') == int(pitch_total(changeup)), ("fail message here")
    main()
