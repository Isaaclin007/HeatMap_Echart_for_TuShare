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

    if num > 10:
        num = 10
    if num < -10:
        num = -10
    if num > 0 and num < 0.8:
        num = 1
    if num > -0.8 and num < 0:
        num = -1
    num = int(round(num))
    colormap = {
        # -11: '#005824',
        -10: '#00ff00', #0,255,0
        -9: '#64ff64', #100,255,100
        -8: '#64f064', #100,240,100
        -7: '#64dc64', #100,220,100
        -6: '#64c864', #100,200,100
        -5: '#64b464', #100,180,100
        -4: '#64a064', #100,160,100
        -3: '#648c64', #100,140,100
        -2: '#647864', #100,120,100
        -1: '#646464', #100,100,100
        0: '#3c3c50', #60,60,80
        1: '#ffc8ff', #255,200,255
        2: '#ffb4f0', #255,180,240
        3: '#ffa0dc', #255,160,220
        4: '#ff8cc8', #255,140,200
        5: '#ff8ca0', #255,140,160
        6: '#ff648c', #255,100,140
        7: '#ff3c8c', #255,60,140
        8: '#ff3c64', #255,60,100
        9: '#ff0064', #255,0,100
        10: '#ff0000', #255,0,0
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

        if type_is != "d":
            value_row['open'] = '-'
            value_row['high'] = '-'
            value_row['low'] = '-'

        # if type_is == "i":
        #     name = name.split("|")[1]

        value = value_row['changepercent']
        color = gain_color(value)
        self.json = {
            "name": name,
            "id": value_row['name'],
            "value": [value_row['rate'], value, value_row['open'], value_row['high'], value_row['low']],
            "itemStyle": {"borderColor": color, "borderWidth": 5, "color": color},
            "children": []
        }

    def return_json(self):
        return self.json

    def add_child(self, item):
        self.json["children"].append(item.json)

    def return_json_str(self):
        return json.dumps(self.json)
