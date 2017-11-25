import React, { Component } from 'react';

// 引入 ECharts 主模块
import echarts from 'echarts/lib/echarts';
// 引入柱状图
import  'echarts/lib/chart/bar';
// 引入提示框和标题组件
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';

class EchartsTest extends Component {
  componentDidMount() {
      var myChart = echarts.init(document.getElementById('main'));
      // 绘制图表
      myChart.setOption({
          title: { text: '' },
          color: ['#339BDB'],
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
              data: ["人民广场", "南京东路", "上海科技馆", "世纪大道", "岳阳路", "地铁博物馆"],
              axisTick: {
                alignWithLabel: true
              }
          },
          yAxis: {},
          series: [{
              name: '定位频率',
              type: 'bar',
              barWidth: '60%',
              data: [5, 20, 36, 10, 10, 20]
          }]
      });
  }
    render() {
        return (
            <div id="main" style={{ width: 300, height:300 }}></div>
        );
    }
}

export default EchartsTest;
