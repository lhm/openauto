import camelot
import wget

# https://www.kba.de/SharedDocs/Publikationen/DE/Fahrzeugtechnik/SV/sv222_m1_kraft_pdf.pdf?__blob=publicationFile&v=18
url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
wget.download(url, '/Users/scott/Downloads/cat4.jpg')

input = 'data/sv222_m1_kraft_pdf.pdf'
output = 'data/full.csv'
pages = '1001-1002'
table_areas = ["19.65533962264151,712.1837370697878,552.2214465408805,57.101629906405954"]
columns = ["43.990522012578616,149.75496855345912,169.4103081761006,194.68145911949685,302.3178427672956,322.9091509433962,342.5644905660377,365.02773584905657,383.74710691823896,403.4024465408805,423.057786163522,441.7771572327044,461.4324968553459,480.1518679245283,499.8072075471698,518.5265786163521"]

tables = camelot.read_pdf(input, pages=pages, flavor='stream', table_areas=table_areas, columns=columns)
tables.export(output, f='csv')
