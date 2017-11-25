import React from 'react';
import ReactDOM from 'react-dom';
import { Form, Icon, Input, Button } from 'antd';
const FormItem = Form.Item;
import { Row, Col } from 'antd';
import $ from 'jquery';
import FormInput from '../components/FormInput';
import Amap from '../components/Amap';

class SchemeForm extends React.Component {
  // constructor(props) {
  //   super(props);
  //   $.ajax({
  //     url: 'http://127.0.0.1:8000/api/accounts/',
  //     type: 'get',
  //     dataType: 'text',
  //     async:false,
  //     success: function(r) {
  //       console.log(eval(r));
  //     },
  //     error: function() {
  //       alert('fail');
  //       // return jsontree;
  //     }
  //   });
  // }

  render() {
    return (
      <div>
        <Row>
        <Col span={8}>
          <FormInput />
        </Col>
        <Col span={16}>
          <Amap />
        </Col>
        </Row>
      </div>
    );
  }
}

export default SchemeForm;
