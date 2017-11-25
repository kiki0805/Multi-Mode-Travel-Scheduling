import React from 'react';
import ReactDOM from 'react-dom';
import { Avatar, Col, Card, Tag, Transfer } from 'antd';
import EchartsTest from '../components/EchartsTest'
const mockData = [];
for (let i = 0; i < 20; i++) {
  mockData.push({
    key: i.toString(),
    title: `tag${i + 1}`,
    description: `description of content${i + 1}`,
  });
}
class UserProfile extends React.Component {
  constructor() {
    super();
    this.state = {targetKeys:mockData, selectedKeys: []};
    this.handleChange = this.handleChange.bind(this);
    this.handleSelectChange = this.handleSelectChange.bind(this);
    this.handleScroll = this.handleScroll.bind(this);
  }

  handleChange (nextTargetKeys, direction, moveKeys) {
    this.setState({ targetKeys: nextTargetKeys });

    console.log('targetKeys: ', targetKeys);
    console.log('direction: ', direction);
    console.log('moveKeys: ', moveKeys);
  }

  handleSelectChange(sourceSelectedKeys, targetSelectedKeys) {
    this.setState({ selectedKeys: [...sourceSelectedKeys, ...targetSelectedKeys] });

    console.log('sourceSelectedKeys: ', sourceSelectedKeys);
    console.log('targetSelectedKeys: ', targetSelectedKeys);
  }

  handleScroll(direction, e) {
    console.log('direction:', direction);
    console.log('target:', e.target);
  }

   render(){
     const state = this.state;
     return(
       <Col>
      <Card title="root" className='user-profile' style={{ width: 480, margin: 10 }}>
      <Transfer
        dataSource={mockData}
        titles={['Source', 'Target']}
        targetKeys={state.targetKeys}
        selectedKeys={state.selectedKeys}
        onChange={this.handleChange}
        onSelectChange={this.handleSelectChange}
        onScroll={this.handleScroll}
        render={item => item.title}
      />
      <EchartsTest />
      </Card>
      </Col>
     );
   }
 }
 
 export default UserProfile;

