from dataflows import Flow, load, printer, checkpoint, dump_to_path, set_type
from itertools import chain

source = 'https://www.statistik.sachsen.de/genonline/online?sequenz=tabelleDownload&selectionname=46251-001K&regionalschluessel='

skip_head = range(1, 9)
skip_tail = range(-4, 0)
skip_rows = chain(skip_head, skip_tail)

headers = [
    'Gebietscode (KRS50P)',
    'Gebietsname',
    'Stichtag',
    'Insgesamt',
    'Krafträder',
    'Personenkraftwagen',
    'Lastkraftwagen',
    'Zugmaschinen insgesamt'
]

Flow(
    load(source,
         format='csv',
         encoding='iso-8859-1',
         name='46251-001K',
         headers=headers,
         skip_rows=skip_rows
         ),
    set_type('Stichtag', type='date', format='%d.%m.%Y'),
    checkpoint('kfz-bestand-sachsen'),
    dump_to_path('./packages/kfz-bestand-sachsen'),
    printer(tablefmt='simple')
).process()
