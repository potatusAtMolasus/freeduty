import axios from "axios";

const instance = axios.create({
  baseURL: 'https://dutyfreesochi.ru/',
  withCredentials: true,
  credentials: 'same-origin',
  crossdomain: true,
  headers: {
    'Content-Type': 'application/json',
  }
});

export default instance;