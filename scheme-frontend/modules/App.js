import React from 'react';
import { Menu, Row, Col, Icon } from 'antd';
import SchemeForm from './containers/SchemeForm';
import UserProfile from './containers/UserProfile';
import TransportationForm from './components/TransportationForm';
const SubMenu = Menu.SubMenu;
const MenuItemGroup = Menu.ItemGroup;
import ProfilePanel from './containers/UserProfile'

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      current: 'profile',
    };
    this.handleClick = this.handleClick.bind(this)
  }

  handleClick(e) {
    console.log('click ', e);
    this.setState({
      current: e.key,
    });
  }
  componentWillUnmount() {}
  render() {
    return (
      <div>
      <Col span={4}>
      </Col>
      <Col span={20}>
      <Menu
        onClick={this.handleClick}
        selectedKeys={[this.state.current]}
        mode="horizontal"
      >
        <Menu.Item key="profile">
          <Icon type="mail" />Profile
        </Menu.Item>
        <Menu.Item key="scheme">
          <Icon type="appstore" />Scheme
        </Menu.Item>
        <Menu.Item key="transportation">
          <Icon type="appstore" />Transportation
        </Menu.Item>
      </Menu>
      {
        this.state.current === 'profile' ?
          <UserProfile /> :
          <div></div>
      }
      {
        this.state.current === 'scheme' ?
          <SchemeForm /> :
          <div></div>
      }
      {
        this.state.current === 'transportation' ?
          <TransportationForm /> :
          <div></div>
      }
      </Col>
      </div>
    );
  }
}
