import axios from "axios";

const instance = axios.create({
  baseURL: 'http://82b3c652.ngrok.io'
})

export default instance;