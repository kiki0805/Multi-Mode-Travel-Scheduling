import React from 'react';
import { Button } from 'antd';
import { Map, Marker } from 'react-amap';
import { Menu, Icon } from 'antd';
const SubMenu = Menu.SubMenu;
const MenuItemGroup = Menu.ItemGroup;

// var Map = ReactAMAP.Map;

class Amap extends React.Component {
  constructor() {
    super();
    this.state = {
      current: 'event1',
    };
    const _this = this;
    this.mapEvents1 = {
      created(map){
        _this.map = map;
        AMap.service(["AMap.Walking"], function(){
          var MWalk = new AMap.Walking({map:map});
          MWalk.search([116.379028, 39.73], [116.379028, 39.865042],
            function(status, result){});
        });
      },
    };
    this.event_event = this.mapEvents1;
    this.mapEvents2 = {
      created(map){
        _this.map = map;
        AMap.service(["AMap.Riding"], function(){
          var MWalk = new AMap.Riding({map:map});
          MWalk.search([116.379028, 39.865042], [116.427281, 39.903719],
            function(status, result){});
        });
      },
    };
    this.mapEvents3 = {
      created(map){
        _this.map = map;
        AMap.service(["AMap.Driving"], function(){
          var MWalk = new AMap.Driving({map:map});
          MWalk.search([116.427281, 39.903719], [116.428, 39.903719],
            function(status, result){});
        });
      },
    };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(e) {
    console.log('click ', e);
    this.setState({
      current: e.key,
    });
  }
  render() {
    const styleC = {
      background: `url('http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/map-marker-icon.png')`,
      backgroundSize: 'contain',
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
      width: '30px',
      height: '40px',
      color: '#000',
      textAlign: 'center',
      lineHeight: '40px'
    }
    return (
      <div>
      <Menu
        onClick={this.handleClick}
        selectedKeys={[this.state.current]}
        mode="horizontal"
      >
      <Menu.Item key="event1">
        Driving
      </Menu.Item>
      <Menu.Item key="event2">
        <Icon type="right" />Riding
      </Menu.Item>
      <Menu.Item key="event3">
        <Icon type="right" />Walking
      </Menu.Item>
      </Menu>
      {
        this.state.current === 'event1' ?
          (<div style={{ width: 600, height: 500, margin: 10 }}>
          <Map center={{ longitude: 116.427, latitude: 39.9 }} zoom={10} amapkey={'74c18f17efa4ae47b261623b67cecd4f'} events={this.mapEvents1}>
          <Marker position={{ longitude: 116.379028, latitude: 39.865042 }} />
          <Marker position={{ longitude: 116.379028, latitude: 39.73 }} />
          <Marker position={{ longitude: 116.427281, latitude: 39.903719 }} />
          <Marker position={{ longitude: 116.428, latitude: 39.903719 }} />
          </Map>
          </div>) : <div></div>
      }
      {
        this.state.current === 'event2' ?
          (<div style={{ width: 600, height: 500, margin: 10 }}>
          <Map center={{ longitude: 116.427, latitude: 39.9 }} zoom={10} amapkey={'74c18f17efa4ae47b261623b67cecd4f'} events={this.mapEvents2}>
            <Marker position={{ longitude: 116.379028, latitude: 39.865042 }} />
            <Marker position={{ longitude: 116.379028, latitude: 39.73 }} />
            <Marker position={{ longitude: 116.427281, latitude: 39.903719 }} />
            <Marker position={{ longitude: 116.428, latitude: 39.903719 }} />
          </Map>
          </div>) : <div></div>
      }
      {
        this.state.current === 'event3' ?
          (<div style={{ width: 600, height: 500, margin: 10 }}>
          <Map center={{ longitude: 116.427, latitude: 39.9 }} zoom={10} amapkey={'74c18f17efa4ae47b261623b67cecd4f'} events={this.mapEvents3}>
          <Marker position={{ longitude: 116.379028, latitude: 39.865042 }} />
          <Marker position={{ longitude: 116.379028, latitude: 39.73 }} />
          <Marker position={{ longitude: 116.427281, latitude: 39.903719 }} />
          <Marker position={{ longitude: 116.428, latitude: 39.903719 }} />
          </Map>
          </div>) : <div></div>
      }
      </div>
    );
  }
}

export default Amap;
