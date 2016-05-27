# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq

HOST = 'http://rutor.info'
END_POINT = HOST + '/search/0/0/000/2/%s'

def search(query):
    data = list()
    document = pq(requests.get(END_POINT % query).content)
    for item in document('div#index > table > tr:not(.backgr)'):
        data.append({
            'seed':    int(pq('td:last > span.green', item).text()),
            'leech':   int(pq('td:last > span.red', item).text()),
            'title':   pq('td:eq(1)', item).text(),
            'magnet':  pq('td:eq(1) > a:eq(1)', item).attr('href'),
            'torrent': HOST + pq('td:eq(1) > a:eq(0)', item).attr('href')
        })
    return data