import React from 'react';
import ReactDOM from 'react-dom';
import { Form, DatePicker, TimePicker, Input, Tooltip, Icon, Cascader, Select, Row, Col, Checkbox, Button, InputNumber } from 'antd'
const FormItem = Form.Item;

const modes = [{
  value: 'time-first',
  label: 'Time First',
}, {
  value: 'place-first',
  label: 'Place First',
}, {
  value: 'cus1',
  label: 'Custom Mode 1',
}, {
  value: 'cus2',
  label: 'Custom Mode 2',
}, {
  value: 'cus3',
  label: 'Custom Mode 3',
}];

class FormInput extends React.Component {
  
  render() {
    
    return (
      <Form style={{ margin: 10 }}>
        <FormItem label="Orgin">
          <Input defaultValue="双河东路团桂路交叉口" />
        </FormItem>
        <FormItem label="Destination">
          <Input defaultValue="翠饰界" />
        </FormItem>
        <FormItem label="Duration">
          <InputNumber style={{ width: 337 }} />
        </FormItem>
        <FormItem label="Begin Time">
          <DatePicker style={{ width: 337 }} />
        </FormItem>
        <FormItem label="End Time">
          <DatePicker style={{ width: 337 }} />
        </FormItem>
        <FormItem label="Modes">
          <Cascader options={modes} />
        </FormItem>
        <FormItem>
          <Button style={{ width: 337 }} type="primary" htmlType="submit">Get a Scheme!</Button>
        </FormItem>
      </Form>
    );
  }
}

export default FormInput;
