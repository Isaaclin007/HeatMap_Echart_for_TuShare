function heat_map(data) {
    myChart.hideLoading();

    var visualMin = -100;
    var visualMax = 100;
    var visualMinBound = -40;
    var visualMaxBound = 40;

    convertData(data);

    function convertData(originList) {
        var min = Infinity;
        var max = -Infinity;

        for (var i = 0; i < originList.length; i++) {
            var node = originList[i];
            if (node) {
                var value = node.value;
                value[2] != null && value[2] < min && (min = value[2]);
                value[2] != null && value[2] > max && (max = value[2]);
            }
        }

        for (var i = 0; i < originList.length; i++) {
            var node = originList[i];
            if (node) {
                var value = node.value;

                // Scale value for visual effect
                // if (value[2] != null && value[2] > 0) {
                //     value[3] = echarts.number.linearMap(
                //         value[2], [0, max], [visualMaxBound, visualMax], true
                //     );
                // }
                // else if (value[2] != null && value[2] < 0) {
                //     value[3] = echarts.number.linearMap(
                //         value[2], [min, 0], [visualMin, visualMinBound], true
                //     );
                // }
                // else {
                //     value[3] = 0;
                // }
                //
                // if (!isFinite(value[3])) {
                //     value[3] = 0;
                // }

                if (node.children) {
                    convertData(node.children);
                }
            }
        }
    }


    function isValidNumber(num) {
        return num != null && isFinite(num);
    }

    myChart.setOption(option = {
        title: {
            left: 'center',
            text: '股价热力图',
            subtext: ''
        },
        tooltip: {
            formatter: function (info) {
                var value = info.value;

                // var rate = value[0];
                // rate = isValidNumber(rate)
                //     ? rate.toFixed(2) + '%'
                //     : '-';

                var change = value[1];
                change = isValidNumber(change)
                    ? change.toFixed(2) + '%'
                    : '-';
                var trade = value[2];
                trade = isValidNumber(trade)
                    ? echarts.format.addCommas(trade) + ''
                    : '-';
                var open = value[3];
                open = isValidNumber(open)
                    ? echarts.format.addCommas(open) + ''
                    : '-';
                var high = value[4];
                high = isValidNumber(high)
                    ? echarts.format.addCommas(high) + ''
                    : '-';
                var low = value[5];
                low = isValidNumber(low)
                    ? echarts.format.addCommas(low) + ''
                    : '-';

                return [
                    '<div class="tooltip-title">' + echarts.format.encodeHTML(info.id) + '</div>',
                    '涨幅: &nbsp;&nbsp;' + change + '<br>',
                    '开盘: &nbsp;&nbsp;' + open + '<br>',
                    '最高: &nbsp;&nbsp;' + high + '<br>',
                    '最低: &nbsp;&nbsp;' + low + '<br>',
                    '收盘: &nbsp;&nbsp;' + trade + '<br>',
                ].join('');
            }
        },
        series: [{
            name: '股价热力图 by 摸鱼大佬',
            top: 50,
            type: 'treemap',
            label: {
                show: true,
                formatter: "{b}",
                normal: {
                    textStyle: {
                        ellipsis: true
                    }
                }
            },
            upperLabel: {
                normal: {
                    show: true,//false
                    height: 20
                }
            },
            itemStyle: {
                normal: {
                    borderColor: 'grey',
                    // borderColor: 'black',

                }
            },
            levels: [
                {
                    upperLabel: {
                        normal: {
                            show: true,//false
                            height: 20
                        }
                    },
                    itemStyle: {
                        normal: {
                            borderWidth: 1,
                            gapWidth: 1
                        }
                    }

                },


            ],
            data: data
        }]
    });


}