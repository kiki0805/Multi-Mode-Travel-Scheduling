import React from 'react';
import { Menu, Row, Col, Icon } from 'antd';
import SchemeForm from './containers/SchemeForm';
import UserProfile from './containers/UserProfile';
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
      </Menu>
      {
        this.state.current === 'profile' ?
          <UserProfile /> :
          <SchemeForm />
      }
      </Col>
      </div>
    );
  }
}
