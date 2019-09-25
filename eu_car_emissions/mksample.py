N = 100001
with open("CO2_passenger_cars.csv", encoding='utf_16_le') as infile:
    lines = [next(infile) for x in range(N)]

with open("100k.csv", 'w+', encoding='utf8') as outfile:
    outfile.writelines(lines)
