import { observable, action, runInAction } from 'mobx';
import axios from 'axios';


class GroupStore {
  @observable username = '';

  @action signin(username, password) {
    axios.get('127.0.0.1:8000/api/accounts/signin/', {username: username, password: password});
    this.username = username;
  }

}

export default new UserStore();
