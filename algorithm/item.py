import json


def gain_color(num):

    # if num > 11:
    #     num = 11
    # if num < -11:
    #     num = -11
    # num = int(round(num))
    # colormap = {
    #     -11: '#005824',
    #     -10: '#005824',
    #     -9: '#1A693B',
    #     -8: '#347B53',
    #     -7: '#4F8D6B',
    #     -6: '#699F83',
    #     -5: '#83B09B',
    #     -4: '#9EC2B3',
    #     -3: '#B8D4CB',
    #     -2: '#D2E6E3',
    #     -1: '#EDF8FB',
    #     0: '#ededed',
    #     1: '#ffcfdc',
    #     2: '#ffcccc',
    #     3: '#ff8080',
    #     4: '#ff5959',
    #     5: '#ff4040',
    #     6: '#d90000',
    #     7: '#b20000',
    #     8: '#7f0000',
    #     9: '#660000',
    #     10: '#400000',
    #     11: '#400000'
    # }

    num = int(round(num))
    if num > 10:
        num = 10
    if num < -10:
        num = -10
    # if num > 0 and num < 0.8:
    #     num = 1
    # if num > -0.8 and num < 0:
    #     num = -1
    # num = int(round(num))
    colormap = {
        # -11: '#005824',
        -10: 'rgba(49,203,89,1)', #0,255,0 00ff00
        -9: 'rgba(49,203,89,0.9)', #100,255,100 64ff64
        -8: 'rgba(49,203,89,0.8)', #100,240,100 64f064
        -7: 'rgba(49,203,89,0.7)', #100,220,100 64dc64
        -6: 'rgba(49,203,89,0.6)', #100,200,100 64c864
        -5: 'rgba(49,203,89,0.5)', #100,180,100 64b464
        -4: 'rgba(49,203,89,0.4)', #100,160,100 64a064
        -3: 'rgba(49,203,89,0.3)', #100,140,100 648c64 35754E
        -2: 'rgba(49,203,89,0.2)', #100,120,100 647864 366e4e
        -1: 'rgba(49,203,89,0.1)', #100,100,100 646464 3B5A50
        # -1: 'rgba(0,255,0,0.1)', #100,100,100 646464 3B5A50
        # 0: 'rgb(60,60,80)', #60,60,80 3c3c50
        # 0: 'rgba(252,52,54,0)', #60,60,80 rgb(38,40,53)
        0: 'rgb(38,40,53)', #60,60,80 
        # 1: 'rgba(255,0,0,0.1)', #255,200,255 ffc8ff 5A4554
        1: 'rgba(252,52,54,0.1)', #255,200,255 ffc8ff 5A4554
        2: 'rgba(252,52,54,0.2)', #255,180,240 ffb4f0 634553
        3: 'rgba(252,52,54,0.3)', #255,160,220 ffa0dc 94444d
        4: 'rgba(252,52,54,0.4)', #255,140,200 ff8cc8 bf4045
        5: 'rgba(252,52,54,0.5)', #255,140,160 ff8ca0 e7393b
        6: 'rgba(252,52,54,0.6)', #255,100,140 ff648c f63638
        7: 'rgba(252,52,54,0.7)', #255,60,140 ff3c8c
        8: 'rgba(252,52,54,0.8)', #255,60,100 ff3c64
        9: 'rgba(252,52,54,0.9)', #255,0,100 ff0064
        10: 'rgba(252,52,54,1)', #255,0,0 ff0000
        # 11: '#400000'
    }

    return colormap[num]


class MapItem:
    def __init__(self, value_row, type_is='d'):
        """
        :param value_row:
        :param type_is: d, daily; m, market; i, industry; t, total
        """
        value_row = value_row.copy()
        name = value_row['name']

        if type_is != "d": # 个股
            value_row['trade'] = '-'
            value_row['open'] = '-'
            value_row['high'] = '-'
            value_row['low'] = '-'

        # if type_is == "i": # 行业
        #     value_row['changepercent'] = 0
            # value_row['trade'] = '-'
            # value_row['open'] = '-'
            # value_row['high'] = '-'
            # value_row['low'] = '-'

        # if type_is == "i":
        #     name = name.split("|")[1]

        if type_is == "t": # 全市场
            value_row['changepercent'] = 0

        value = value_row['changepercent']
        color = gain_color(value)
        self.json = {
            "name": name,
            "id": value_row['name'],
            "value": [value_row['rate'], value, value_row['trade'], value_row['open'], value_row['high'], value_row['low']],
            "itemStyle": {"borderColor": color, "borderWidth": 1, "color": color},
            "children": []
        }

    def return_json(self):
        return self.json

    def add_child(self, item):
        self.json["children"].append(item.json)

    def return_json_str(self):
        return json.dumps(self.json)
