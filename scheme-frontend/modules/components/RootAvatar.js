import React from 'react';
import ReactDOM from 'react-dom';
import { Avatar, Col, Card, Tag, Transfer } from 'antd';
class RootAvatar extends React.Component {
  render(){
    const state = this.state;
    return (
      <div><Avatar style={{ color: '#f56a00', backgroundColor: '#fde3cf' }}>U</Avatar></div>
    );
  }
}

export default RootAvatar;