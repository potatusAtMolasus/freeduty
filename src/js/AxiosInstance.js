import axios from "axios";

const instance = axios.create({
  baseURL: 'http://bfe6e340.ngrok.io'
})

export default instance;