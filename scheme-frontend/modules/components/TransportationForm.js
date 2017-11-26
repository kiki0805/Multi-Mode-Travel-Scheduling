import React from 'react';
import ReactDOM from 'react-dom';
import { Card, Checkbox, Form, Input, Row, Col, Button, InputNumber } from 'antd'
const FormItem = Form.Item;


class TransportationForm extends React.Component {
  
  render() {
    
    return (
      <Row>
      <Col span={8}>
      <Form style={{ margin: 10 }}>
        <FormItem label="Name">
          <Input defaultValue="飞一般的速度" style={{ width: 337 }} />
        </FormItem>
        <FormItem label="Speed">
          <InputNumber defaultValue={666} style={{ width: 337 }} />
        </FormItem>
        <FormItem>
          <Button type="primary" style={{ width: 337 }} htmlType="submit">Create your own transportation!</Button>
        </FormItem>
      </Form>
      </Col>
      <Col span={8} style={{ marginTop:15 , marginLeft: 20 }}>
      <Card style={{height:202}} title="Your Transportations">
        <Checkbox defaultChecked={false}>步行</Checkbox>
        <br />
        <Checkbox defaultChecked>公交</Checkbox>
        <br />
        <Checkbox defaultChecked={false}>地铁</Checkbox>
        <br />
        <Checkbox defaultChecked>骑行</Checkbox>
        <br />
        <Checkbox defaultChecked>私家车</Checkbox>
        </Card>
      </Col>
      </Row>
    );
  }
}

export default TransportationForm;
